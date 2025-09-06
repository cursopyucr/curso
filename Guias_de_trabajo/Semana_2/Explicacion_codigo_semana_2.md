# Guía del Script semana 2
> **Propósito**: documentar, paso a paso y con detalle, cada función y bloque del notebook que analiza cambios de población a nivel cantonal y modela el terreno a partir de curvas de nivel, generando salidas estáticas e interactivas.

---

## Tabla de contenidos
- [1. Visión general del flujo](#1-visión-general-del-flujo)
- [2. Requisitos y preparación](#2-requisitos-y-preparación)
- [3. Estructura de carpetas](#3-estructura-de-carpetas)
- [4. Datos de entrada esperados](#4-datos-de-entrada-esperados)
- [5. Funciones auxiliares (demografía y mapas estáticos)](#5-funciones-auxiliares-demografía-y-mapas-estáticos)
  - [5.1 `cargar_datos`](#51-cargar_datos)
  - [5.2 `calcular_totales_poblacion`](#52-calcular_totales_poblacion)
  - [5.3 `calcular_cambios`](#53-calcular_cambios)
  - [5.4 `agregar_norte`](#54-agregar_norte)
  - [5.5 `agregar_escala`](#55-agregar_escala)
  - [5.6 `mapa_comparativo`](#56-mapa_comparativo)
  - [5.7 `mapa_tematico`](#57-mapa_tematico)
  - [5.8 `guardar_resultados`](#58-guardar_resultados)
- [6. Bloque principal `if __name__ == "__main__":`](#6-bloque-principal-if-__name__--__main__)
- [7. Visualización interactiva de cambio porcentual (`folium`)](#7-visualización-interactiva-de-cambio-porcentual-folium)
- [8. Clasificación temática (Jenks, Cuantiles, Intervalos iguales)](#8-clasificación-temática-jenks-cuantiles-intervalos-iguales)
- [9. Curvas de nivel → TIN](#9-curvas-de-nivel--tin)
- [10. Interpolación IDW → DEM + Hillshade](#10-interpolación-idw--dem--hillshade)
- [11. Consejos de calidad, CRS y rendimiento](#11-consejos-de-calidad-crs-y-rendimiento)
- [12. Errores comunes y cómo evitarlos](#12-errores-comunes-y-cómo-evitarlos)

---

## 1. Visión general del flujo

1) **Cargar datos vectoriales** (cantones).
2) **Calcular métricas demográficas** (totales 2000/2011, cambio absoluto/porcentual, tendencia).
3) **Mapear** resultados: comparativos lado a lado y temáticos.
4) **Exportar** resultados como GeoJSON/PNG.
5) **Visualización interactiva** en `folium` (cambio porcentual).
6) **Clasificación temática** (Jenks, Cuantiles, Intervalos iguales) sobre `POB_2000_H`.
7) **Terreno**: curvas de nivel → TIN → IDW → DEM → hillshade.
8) **Mapas** interactivos/estáticos de DEM + sombras.

---

## 2. Requisitos y preparación

**Paquetes** (mínimo):
```bash
pip install geopandas matplotlib matplotlib-scalebar contextily pandas numpy fiona shapely pyproj folium branca mapclassify rasterio scipy
```

**Importante**:
- `rasterio` y `scipy` son necesarios para IDW/hillshade.
- Windows: verificar instalación de dependencias nativas (e.g., GDAL). 

**Cambiar directorio de trabajo** (opcional, como en tu notebook):
```python
import os
os.chdir("C:/Users/Public/Documents/Curso_python/GitHub/curso")
print(os.getcwd())
```

---

## 3. Estructura de carpetas

```
curso/
├─ Datos/
│  └─ Semana_2/
│     ├─ Cantones2014ctm05.geojson
│     ├─ Cantones2014.shp (+ .dbf/.shx/.prj)
│     └─ curvas_10m_clip.shp (+ .dbf/.shx/.prj)
├─ Figuras/
│  └─ Semana_2/
└─ Resultados/
   └─ Semana_2/
```

> Crea las subcarpetas `Figuras/Semana_2` y `Resultados/Semana_2` antes de exportar.

---

## 4. Datos de entrada esperados

**Capa de cantones** debe incluir (nombres pueden variar pero el código los usa así):
- `POB_2000_H`, `POB_2000_M`, `POB_2011_H`, `POB_2011_M` (numéricos).
- `NCANTON` (nombre del cantón) para tooltips.
- CRS original **CRTM05** (EPSG:5367) en shapefile; para GeoJSON suele venir en WGS84 (EPSG:4326). 

**Curvas de nivel**:
- Geometrías `LineString`.
- Atributo de elevación `HIGH` (en metros).
- CRS conocido (idealmente **EPSG:4326** para `folium`, o re-proyectar).

## 5. Funciones auxiliares (demografía y mapas estáticos)

### 5.1 `cargar_datos`
Lee archivos geoespaciales y devuelve un `GeoDataFrame`. Usa internamente `gpd.read_file(ruta_geojson)`. Este método detecta el formato (GeoJSON, Shapefile, etc.) automáticamente. Si el archivo no tiene CRS, debes asignarlo manualmente con `.set_crs()`.

---

### 5.2 `calcular_totales_poblacion`
Suma columnas de población masculina y femenina. Ejemplo clave:
```python
gdf["POB_2000_TOT"] = gdf["POB_2000_H"] + gdf["POB_2000_M"]
```
Esto genera una nueva columna con el total por cantón. La operación se repite para 2011. Usa aritmética vectorizada de pandas: aplica la suma a todas las filas sin necesidad de `for`.

---

### 5.3 `calcular_cambios`
Agrega tres columnas nuevas:
- **Cambio absoluto**: diferencia de población.
- **Cambio porcentual**: `(cambio_abs / POB_2000_TOT) * 100`.
- **Tendencia**: evalúa cada fila con `lambda x: 'Ganancia' if x > 0 else 'Pérdida'`.

Ejemplo:
```python
gdf["tendencia"] = gdf["cambio_abs"].apply(lambda x: "Ganancia" if x > 0 else "Pérdida")
```
El método `.apply()` aplica la función fila por fila, retornando cadenas en función del valor.

---

### 5.4 `agregar_norte`
Dibuja la flecha de norte usando `ax.annotate`. Punto clave:
```python
ax.annotate('N', xy=ubicacion, xytext=ubicacion, xycoords='axes fraction',
            arrowprops=dict(facecolor='black', width=5, headwidth=15))
```
- `xycoords='axes fraction'` → coloca la flecha en proporción a la figura (0–1).
- `arrowprops` → define estilo de la flecha (color, ancho, forma de la cabeza).

---

### 5.5 `agregar_escala`
Crea un objeto `ScaleBar(1, units=unidad, location='lower left')`. Aquí `1` es el factor de conversión: 1 unidad del CRS → 1 unidad en la barra. Si estás en grados, la escala no representa metros reales.

---

### 5.6 `mapa_comparativo`
Genera dos mapas lado a lado:
```python
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
gdf.plot(column=col1, ax=axes[0], ...)
gdf.plot(column=col2, ax=axes[1], ...)
```
- Añade grilla: `axes[0].grid(True, linestyle='--')`.
- Inserta norte y escala llamando a las funciones auxiliares.

---

### 5.7 `mapa_tematico`
Similar a `mapa_comparativo` pero con un único `Axes`. Guarda con:
```python
fig.savefig(guardar, dpi=300, bbox_inches="tight")
```
- `dpi=300`: alta resolución.
- `bbox_inches="tight"`: ajusta márgenes al contenido.

---

### 5.8 `guardar_resultados`
Exporta el `GeoDataFrame` como GeoJSON con:
```python
gdf.to_file(ruta_salida, driver="GeoJSON")
```
- El `driver` define el formato.
- Imprime confirmación con `print`.

---

## 7. Visualización interactiva de cambio porcentual (`folium`)

### 7.1 `mapa_interactivo_cambio_pct_shp`

Fragmentos clave:
```python
gdf = gdf.set_crs(epsg=5367, allow_override=True)
gdf = gdf.to_crs(epsg=4326)
```
Esto asegura que el shapefile (en proyección métrica CRTM05) se convierta a WGS84 (necesario en `folium`).

El colormap se crea así:
```python
colormap = cm.linear.RdYlGn_11.scale(min_val, max_val)
```
Y se asigna el color por cada cantón:
```python
"fillColor": colormap(feature["properties"]["cambio_pct"])
```

---

## 8. Clasificación temática

### 8.1 `generar_mapa_por_clasificacion`

Uso de `mapclassify`:
```python
scheme = mapclassify.NaturalBreaks(gdf["POB_2000_H"], k=k)
gdf["clase"] = scheme.find_bin(gdf["POB_2000_H"])
```
- `find_bin` devuelve el índice de clase según el valor.
- `cmap.colors[int(c)]` asigna color desde `ListedColormap`.

La leyenda HTML se construye manualmente concatenando bloques `<div>`.

### 8.2 `generar_grilla_mapas`
Muestra tres mapas con distintos métodos de clasificación. Reutiliza la función anterior, cambiando `metodo_nombre`.

---

## 9. Curvas de nivel → TIN

### 9.1 `generar_tin_desde_curvas`

Fragmentos críticos:
```python
for _, row in curvas.iterrows():
    for x, y in geom.coords:
        puntos.append((x, y, elev))
```
Esto convierte cada línea en un conjunto de puntos `(x, y, elev)`.

La triangulación:
```python
delaunay = Delaunay(puntos_np[:, :2])
```
Usa solo XY, elevaciones quedan en `puntos_np[:,2]`.

Visualización 3D:
```python
ax.plot_trisurf(..., triangles=delaunay.simplices, cmap="terrain")
```

---

## 10. Interpolación IDW → DEM + Hillshade

### 10.1 `sample_points_from_contours`
Genera puntos interpolados a lo largo de cada curva con:
```python
sampled = [line.interpolate(dist) for dist in np.linspace(0, line.length, num_points)]
```
Cada punto hereda la elevación de la curva (`row["HIGH"]`).

### 10.2 `idw_interpolation`
Construcción de grilla:
```python
grid_x, grid_y = np.meshgrid(x_coords, y_coords)
```
Consulta de vecinos:
```python
distances, indices = tree.query(np.c_[grid_x.ravel(), grid_y.ravel()], k=8)
```
Ponderación inversa:
```python
weights = 1 / (distances ** power + 1e-12)
weights /= weights.sum(axis=1)[:, None]
```
Esto evita divisiones por cero (`+ 1e-12`).

### 10.5 `calculate_hillshade`
Cálculo de gradientes:
```python
dzdx = np.gradient(array, axis=1) / xres
dzdy = np.gradient(array, axis=0) / yres
```
Pendiente y orientación:
```python
slope = np.pi / 2 - np.arctan(np.sqrt(dzdx**2 + dzdy**2))
aspect = np.arctan2(-dzdx, dzdy)
```
Iluminación según azimut y altura solar.

---

## 12. Errores comunes y cómo evitarlos

- `allow_override=True`: fuerza CRS, puede ocultar errores si la proyección real es otra.
- Divisiones por cero: al calcular porcentajes o pesos en IDW.
- Escalas métricas: en WGS84, no son válidas. Reproyecta a CRS métrico.

---

> Con estas explicaciones adicionales, ahora cada línea clave dentro de las funciones está documentada para que tengas claridad sobre qué hace cada fragmento de código y por qué.



---

## 13. Explicación línea por línea de las partes más complejas

A continuación se detallan las líneas y expresiones más **densas** de cada función, para que tengas claro qué hace cada trozo del código y por qué.

### 13.1 `calcular_cambios(gdf)`
- `gdf["cambio_abs"] = gdf["POB_2011_TOT"] - gdf["POB_2000_TOT"]`
  - **Resta vectorizada**: calcula, fila a fila, el cambio absoluto de población.
- `gdf["cambio_pct"] = (gdf["cambio_abs"] / gdf["POB_2000_TOT"]) * 100`
  - **División por columna**: si `POB_2000_TOT` tiene ceros, se producirán `inf`/`NaN`. Manejar antes o después (e.g., con `np.where`).
- `gdf["tendencia"] = gdf["cambio_abs"].apply(lambda x: "Ganancia" if x > 0 else "Pérdida")`
  - **Función lambda** aplicada a cada celda: crea una etiqueta categórica en base al signo del cambio.

### 13.2 `mapa_comparativo(...)`
- `fig, axes = plt.subplots(1, 2, figsize=(16, 8))`
  - Crea **dos** ejes lado a lado para comparar variables en el mismo `gdf`.
- `gdf.plot(column=col1, cmap=cmap, legend=True, ax=axes[0], edgecolor="black")`
  - Traza polígonos coloreados por `col1`. `legend=True` construye una barra/leyenda por clases o rango continuo.
- `axes[i].grid(True, linestyle='--', linewidth=0.5)`
  - Activa la **grilla** de fondo en ambos paneles.
- `plt.tight_layout()`
  - Ajusta márgenes para que las leyendas/títulos no se solapen.

### 13.3 `mapa_tematico(...)`
- `fig, ax = plt.subplots(figsize=(10, 8))` + `gdf.plot(...)`
  - Crea un mapa único con **leyenda** continua/discreta según la naturaleza de `columna`.
- `agregar_norte(ax)` / `agregar_escala(ax, unidad="m")`
  - Inserta **anotaciones** en coordenadas relativas al eje; no dependen del CRS para posicionamiento, pero **la escala sí** depende del CRS.
- `if guardar: fig.savefig(guardar, dpi=300, bbox_inches="tight")`
  - Exporta el PNG con calidad de impresión; `bbox_inches="tight"` recorta espacios en blanco.

### 13.4 `mapa_interactivo_cambio_pct_shp(ruta_shp)`
- `gdf = gdf.set_crs(epsg=5367, allow_override=True)`
  - **Fija** el CRS *sin reproyectar coordenadas*. Úsalo solo si sabes que **esa** es la proyección real del archivo.
- `gdf = gdf.to_crs(epsg=4326)`
  - **Reproyecta** a WGS84 (lat/lon) para que `folium` muestre correctamente.
- `bounds = gdf.total_bounds`
  - Extensión `[minx, miny, maxx, maxy]` de todos los polígonos; se usa para validar y centrar el mapa.
- `colormap = cm.linear.RdYlGn_11.scale(min_val, max_val)`
  - Escala una paleta discreta a tu rango **real** de valores para colorear homogéneamente.
- `folium.GeoJson(..., style_function=..., tooltip=folium.GeoJsonTooltip(...))`
  - `style_function` recibe cada *feature* y retorna un dict de estilo (color de relleno, borde, opacidad).
  - `GeoJsonTooltip` muestra **campos** elegidos de `properties` con etiquetas amigables.

### 13.5 `generar_mapa_por_clasificacion(gdf, metodo_nombre, k)`
- `scheme = metodo(gdf["POB_2000_H"], k=k)`
  - Ajusta un **esquema de clasificación** (Jenks/Cuantiles/Intervalos) y calcula límites de clase.
- `bins = scheme.bins`
  - **Umbrales superiores** de cada clase (longitud `k`).
- `gdf["clase"] = scheme.find_bin(gdf["POB_2000_H"])`
  - Devuelve el **índice de clase** por observación (0..k-1).
- `gdf["fillColor"] = gdf["clase"].apply(lambda c: cmap.colors[int(c)] if ... else "#cccccc")`
  - Traduce índice de clase a **color** discreto (fallback gris si falta).

### 13.6 `generar_tin_desde_curvas(ruta_shp)`
- `for _, row in curvas.iterrows(): ... for x, y in geom.coords: puntos.append((x, y, elev))`
  - Extrae **todos** los vértices de cada `LineString` y les asigna la elevación constante de la curva (`HIGH`).
- `delaunay = Delaunay(puntos_np[:, :2])`
  - Triangulación de Delaunay **solo en XY**; la Z (elevación) se usa después para pintar la superficie.
- `ax.plot_trisurf(..., triangles=delaunay.simplices, cmap="terrain", edgecolor="gray")`
  - Renderiza una superficie 3D por **triángulos**; `simplices` son los índices (i,j,k) por triángulo.

### 13.7 `sample_points_from_contours(shapefile_path, spacing)`
- `num_points = int(np.floor(line.length / spacing))`
  - Calcula cuántos puntos caben a lo largo de la línea, dados los **pasos** uniformes.
- `sampled = [line.interpolate(dist) for dist in np.linspace(0, line.length, num_points)]`
  - Interpola puntos **equiespaciados** a lo largo del *arco*; devuelve geometrías `Point`.

### 13.8 `idw_interpolation(gdf_points, resolution=0.0001, power=2)`
- `xmin, ymin, xmax, ymax = gdf_points.total_bounds`
  - Caja que delimita los puntos para construir la malla de interpolación.
- `x_coords = np.arange(xmin, xmax, res)` / `y_coords = np.arange(ymax, ymin, -res)`
  - Genera **coordenadas** del grid; nota el eje Y decreciente para que el raster quede con **origen arriba**.
- `grid_x, grid_y = np.meshgrid(x_coords, y_coords)`
  - Crea matrices 2D con la **retícula** de evaluación.
- `tree = cKDTree(np.c_[x, y])` y `distances, indices = tree.query(np.c_[grid_x.ravel(), grid_y.ravel()], k=8)`
  - Estructura espacial para consultas rápidas de **k vecinos** por celda de la grilla.
- `weights = 1 / (distances ** power + 1e-12)`
  - Ponderación **IDW**; `1e-12` evita división por cero.
- `weights /= weights.sum(axis=1)[:, None]`
  - **Normaliza** las ponderaciones por fila (cada celda).
- `zi = np.sum(weights * z[indices], axis=1)` y `interpolated = zi.reshape(grid_x.shape)`
  - Promedio ponderado y **reformado** a la grilla 2D.
- `transform = from_origin(xmin, ymax, res, res)`
  - Affine que define el **origen** (esquina sup. izq.) y el tamaño de píxel en X/Y.

### 13.9 `save_raster_to_tiff(array, transform, out_path)`
- El bloque `with rasterio.open(..., driver='GTiff', count=1, dtype=array.dtype, crs='EPSG:4326', transform=transform)`
  - Crea un **GeoTIFF** de 1 banda usando el `dtype` del array y la geo-referenciación provista. Cambia `crs` si estás en CRTM05.

### 13.10 `raster_to_folium(raster_path)`
- `array = src.read(1)`
  - Lee la **banda 1** del raster.
- `array = np.ma.masked_equal(array, 0)`
  - Enmascara los ceros (tratados como **NoData** aquí). Ajusta si 0 es válido.
- `norm = colors.Normalize(vmin=array.min(), vmax=array.max())`
  - Escala valores reales a [0,1] para mapear colores.
- `rgba_img = cmap(norm(array))` → `rgb_img = (... * 255).astype(np.uint8)`
  - Convierte el DEM a imagen **RGB** para el overlay.
- `folium.raster_layers.ImageOverlay(image=png_path, bounds=[[bottom,left],[top,right]], opacity=0.65)`
  - Superpone la imagen **georreferenciada** con los límites del GeoTIFF.

### 13.11 `calculate_hillshade(array, transform, azimuth, altitude)`
- `dzdx = np.gradient(array, axis=1) / xres` y `dzdy = np.gradient(array, axis=0) / yres`
  - Derivadas **espaciales** estimadas por diferencias finitas, ajustadas por el **tamaño de píxel**.
- `slope = π/2 - arctan(√(dzdx² + dzdy²))`
  - Convierte gradiente a **pendiente** (radianes), donde 0 = plano, π/2 = vertical.
- `aspect = arctan2(-dzdx, dzdy)`
  - Dirección de máxima pendiente (0 = norte, rotación estándar raster).
- `shaded = sin(alt)*sin(slope) + cos(alt)*cos(slope)*cos(az - aspect)`
  - **Modelo de iluminación** lambertiano clásico para hillshade.

### 13.12 `raster_overlay_folium(raster_path, name, cmap, opacity)`
- `mask = np.ma.masked_equal(data, 0)`
  - Misma lógica de **NoData**; si tu NoData es otro valor, cámbialo.
- `norm = colors.Normalize(vmin=mask.min(), vmax=mask.max())` → `rgba = cmap(norm(mask))`
  - Normaliza y colorea los datos para generar el PNG del overlay.

### 13.13 `create_dem_hillshade_map(dem_array, transform)`
- **Flujo correcto esperado**:
  1. Guardar `dem_array` con `save_raster_to_tiff(..., ruta_dem)`.
  2. Calcular y guardar `hillshade` con `save_raster_to_tiff`.
  3. Cargar ambos con `raster_overlay_folium` y añadirlos al mapa.
- **Detalle**: asegura que el **nombre de archivo** de DEM sea el mismo al guardar y al leer (evitar `DEM.tif` vs `dem.tif`).

### 13.14 `crear_mapa_estatico_con_norte_escala(...)`
- **Extensión geográfica a partir de `Affine`**:
  - `x_min = transform.c`; `y_max = transform.f`
  - `x_max = x_min + transform.a * ncols`
  - `y_min = y_max + transform.e * nrows` (nota: `transform.e` es negativo en rasters TOP→DOWN)
  - `extent = [x_min, x_max, y_min, y_max]` usado por `imshow`.
- **Leyenda de elevación**:
  - `norm = colors.Normalize(vmin=np.nanmin(dem_array), vmax=np.nanmax(dem_array))`
  - `sm = cm.ScalarMappable(cmap=cmap, norm=norm)`
  - `plt.colorbar(sm, ...)` crea la barra con **rango real** de elevaciones.
- **Flecha norte** con `ax.annotate('N', ... arrowprops=...)` y grilla `ax.grid(...)` para lectura cartográfica.

---

