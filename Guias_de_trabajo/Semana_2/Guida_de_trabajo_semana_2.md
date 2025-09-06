
# Análisis Espacial de Cambios de Población y Terreno en Costa Rica

Este proyecto realiza un análisis geoespacial detallado de los cambios poblacionales por cantón en Costa Rica entre los años 2000 y 2011. Además, se generan modelos digitales del terreno (DEM) a partir de curvas de nivel, incluyendo interpolación mediante IDW y sombreado topográfico (hillshade). El análisis se representa mediante mapas estáticos e interactivos con herramientas de visualización geográfica.

---

##  Contenido del Proyecto

1. **Carga de datos vectoriales (GeoJSON/Shapefile).**
2. **Cálculo de población total por cantón en 2000 y 2011.**
3. **Cálculo de cambio absoluto, porcentaje y tendencia poblacional.**
4. **Visualización comparativa y temática con escala gráfica, norte y grilla.**
5. **Clasificación temática con Jenks, Cuantiles e Intervalos Iguales.**
6. **Extracción de puntos desde curvas de nivel (Shapefile).**
7. **Interpolación de elevación usando IDW.**
8. **Generación de modelos raster, hillshade y visualización integrada.**
9. **Exportación en formatos GeoTIFF, PNG, y GeoJSON.**

---

##  Requisitos

Instala las dependencias ejecutando:

```python
%pip install geopandas folium branca rasterio shapely matplotlib numpy fiona pyproj mapclassify matplotlib-scalebar
```

---

##  Estructura esperada de carpetas

```
├── Datos/
│   └── Semana_2/
│       ├── Cantones2014.shp
│       ├── Cantones2014ctm05.geojson
│       └── curvas_10m_clip.shp
├── Resultados/
│   └── Semana_2/
│       ├── cantones_cambio_poblacion.geojson
│       ├── cambio_abs.png
│       ├── cambio_pct.png
│       ├── tendencia.png
│       ├── idw_elevacion_4326.tif
│       ├── dem.tif
│       ├── hillshade.tif
│       └── mapa_sombras.png
```

---

##  Funcionalidades principales

###  Cálculo de población y cambios

```python
def calcular_totales_poblacion(gdf)
def calcular_cambios(gdf)
```

- Suma los campos `POB_2000_H/M` y `POB_2011_H/M` para obtener totales.
- Calcula:
  - Cambio absoluto (`cambio_abs`)
  - Cambio porcentual (`cambio_pct`)
  - Clasificación de tendencia: `"Ganancia"` o `"Pérdida"`.

---

###  Mapas estáticos con elementos cartográficos

```python
def mapa_comparativo(...)
def mapa_tematico(...)
```

- Visualiza comparaciones entre años o variables temáticas.
- Agrega elementos clave al mapa:
  - Escala en metros (`matplotlib-scalebar`)
  - Flecha de norte
  - Grilla de coordenadas UTM o lat/lon

---

###  Clasificación temática de datos

```python
def generar_mapa_por_clasificacion(...)
def generar_grilla_mapas(...)
```

Clasificación de variables usando métodos:

- **Jenks (Natural Breaks)** – minimiza varianza dentro de clases.
- **Cuantiles** – divide datos en grupos con igual cantidad de elementos.
- **Intervalos Iguales** – separa rangos uniformemente.

🔗 Referencias ArcGIS:
- [Jenks](https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/data-classification-methods.htm#ESRI_SECTION1_22E1A1FAE9B94665A7C5F6DDA55ECA12)
- [Cuantiles](https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/data-classification-methods.htm#ESRI_SECTION2_410546DF3C954CE08B6F23E9FA0A5F35)
- [Intervalos iguales](https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/data-classification-methods.htm#ESRI_SECTION0_B4C07B6A241046DB96B46B69FBD4E6E7)

---

###  Procesamiento de curvas de nivel y generación DEM

```python
def sample_points_from_contours(...)
def idw_interpolation(...)
def save_raster_to_tiff(...)
```

- Extrae vértices de líneas de curvas (LineString) y los convierte en puntos con valores de elevación.
- Interpola una superficie raster usando **IDW (Inverse Distance Weighting)**.
- Exporta el resultado en formato GeoTIFF (`.tif`).

🔗 [Método IDW en ArcGIS](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/idw.htm)

---

###  Sombreado del terreno y visualización

```python
def calculate_hillshade(...)
def create_dem_hillshade_map(...)
def crear_mapa_estatico_con_norte_escala(...)
```

- Crea mapas de **sombreado topográfico** (hillshade) desde el DEM.
- Superpone la elevación sobre un fondo sombreado.
- Genera mapas `.png` y `.tif` con simbología, leyenda, escala y orientación.

🔗 [¿Qué es Hillshade?](https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/hillshade-function.htm)

---

##  Flujo general de ejecución

```python
# 1. Cargar datos geoespaciales
gdf = cargar_datos(ruta_geojson)

# 2. Cálculo de métricas de población
gdf = calcular_totales_poblacion(gdf)
gdf = calcular_cambios(gdf)

# 3. Visualización estática
mapa_comparativo(...)
mapa_tematico(...)

# 4. Clasificación y comparación
generar_grilla_mapas(ruta_shp)

# 5. Curvas y TIN (opcional)
generar_tin_desde_curvas(ruta_curvas)

# 6. Interpolación raster
puntos = sample_points_from_contours(...)
raster, transform = idw_interpolation(...)
save_raster_to_tiff(...)

# 7. Hillshade y visualización
hillshade = calculate_hillshade(...)
create_dem_hillshade_map(...)
crear_mapa_estatico_con_norte_escala(...)
```

---

##  Resultados esperados

- Archivos `.geojson` con atributos enriquecidos.
- Mapas interactivos HTML con `folium`.
- Mapas estáticos `.png` con leyendas, escala y simbología clara.
- Rasters de elevación `.tif` con sombreado topográfico.

---

##  Recursos y créditos

- [GeoPandas](https://geopandas.org/)
- [Folium](https://python-visualization.github.io/folium/)
- [Shapely](https://shapely.readthedocs.io/)
- [Mapclassify](https://pysal.org/mapclassify/)
- [Rasterio](https://rasterio.readthedocs.io/)
- [Matplotlib Scalebar](https://github.com/ppinard/matplotlib-scalebar)
- [ArcGIS Hillshade](https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/hillshade-function.htm)
