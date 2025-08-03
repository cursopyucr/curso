# Introducción a Python para Análisis Espacial y Geoprocesamiento

**Autor:** Emmanuel Jesús Céspedes Rivera

---

## Guía de instalación: Git, VS Code y Python

Para llevar a cabo este curso trabajaremos usando **Git**, **Visual Studio Code** (VS Code) y **Python**.  
Estas herramientas nos servirán para programar, manejar versiones, colaborar en equipo y realizar tareas relacionadas con el manejo de datos espaciales.

---

## 1. Git

Git es un sistema de control de versiones usado principalmente en desarrollo de código para registrar y gestionar cambios en el código fuente a lo largo del tiempo.

**Ejemplo:**

> Imagina que hoy trabajaste en una nueva versión de tu proyecto y después de varias horas notas que los cambios no funcionan como esperabas.  
> Con Git puedes regresar a una versión anterior sin perder tu progreso previo.  
> Es como tener un botón de **"deshacer"** para todo tu proyecto.

**Ventajas de usar Git:**

- Guardar versiones de tus archivos (puntos de control).
- Volver a versiones anteriores si algo falla.
- Trabajar en paralelo con otras personas sin sobrescribir su trabajo.
- Combinar cambios de varias personas de forma ordenada.

---

## 2. GitHub

GitHub es una plataforma en línea que se basa en Git y funciona como una red social para desarrolladores. Permite:

- Guardar proyectos en la nube.
- Ver el historial de cambios.
- Colaborar con otras personas en el mismo código.
- Revisar, comentar y fusionar cambios.

**Relación entre Git y GitHub:**

- **Git:** Herramienta local para gestionar cambios.
- **GitHub:** Espacio remoto para respaldar y compartir cambios.

---

## 3. VS Code y Python

**Ejemplo de uso en análisis espacial:**

- Cargar y visualizar un **DEM** (Modelo Digital de Elevación).
- Aplicar filtros de dirección de flujo o corregir errores.
- Identificar depresiones o cuencas.
- Dibujar el cauce estimado de un río.

En VS Code podrás:

- Escribir scripts en Python.
- Ver metadatos de archivos raster.
- Controlar cambios con Git.
- Subir código a GitHub directamente.

---

## 4. Pasos de instalación

### 4.1 Crear cuenta en GitHub

1. Accede a: [https://github.com/signup](https://github.com/signup)  
   ![Figura 1. Página de creación de cuenta de GitHub](/Guias_de_trabajo/Semana_1/images/figura1.png)

2. Sigue los pasos de creación y recuerda tu **nombre de usuario**.

3. Puedes verificar tu usuario en la página de GitHub:  
   ![Figura 2. Nombre de usuario en GitHub](/Guias_de_trabajo/Semana_1/images/figura2.png)  
   Ejemplo: `cursopyucr`  
   Correo de ejemplo: `jcespedesc461@gmail.com`

### 4.2 Configuración de Git Bash

Una vez instalado **Git**, debemos configurarlo con nuestro nombre de usuario y correo electrónico de **GitHub**.

Primero abre **Git Bash** (Figura 3) y ejecuta los siguientes comandos:

![Figura 3. Abrir Git Bash](/Guias_de_trabajo/Semana_1/images/figura3.png)  

```bash
# Configurar el nombre de usuario *(cambiar por tu nombre de usuario)*
git config --global user.name "cursopyucr"

# Configurar el correo electrónico *(cambiar por tu correo electrónico)*
git config --global user.email "jcespedesc461@gmail.com"

```
Debe verse de la siguiente manera:

![Figura 4. Configurar Git Bash](/Guias_de_trabajo/Semana_1/images/figura4.png)   

Podemos verificar que todo ande bien usando el siguiente comando


```bash
# Asegurarse que la configuración se haya aplicado
git config --global --list

```

Y debe aparecer algo similar a esto su ventana de Git Bash:

![Figura 5. Verificar configurar Git Bash](/Guias_de_trabajo/Semana_1/images/figura5.png)

## 5. ¿Qué es un repositorio?

Un **repositorio** es como una carpeta especial en la que guardas tu proyecto junto con el historial de cambios.  
En Git, un repositorio contiene:

- **Archivos del proyecto** (código, datos, imágenes, etc.).
- **Historial de cambios** (commits).
- **Configuración del proyecto**.

Hay dos tipos:

1. **Repositorio local:** Guardado en tu computadora.
2. **Repositorio remoto:** Guardado en plataformas como GitHub, GitLab o Bitbucket.

---

## 6. Abrir Visual Studio Code

Una vez instalado **VS Code**, ábrelo y verás una interfaz similar a la siguiente:

![Figura 6. Visual Studio Code interfaz inicial](/Guias_de_trabajo/Semana_1/images/figura6.png)

En la imagen se destacan:

1. **Menú superior:** Acceso a opciones como abrir carpetas, ejecutar código, abrir terminal, etc.
2. **Barra lateral:** Atajos para explorador de archivos, búsqueda, control de versiones (Git), depuración, extensiones, etc.
3. **Barra inferior:** Acceso rápido a configuración, cuenta de usuario y estado del editor.

> Desde aquí podremos crear o abrir carpetas para nuestros proyectos, y posteriormente conectar con Git y GitHub.

## 7. Creación de un repositorio en Git (local)

Ahora que tenemos **Git** configurado, podemos crear nuestro primer repositorio local.  
Esto servirá como base para organizar código, datos y cualquier archivo de nuestro proyecto.

---

### 7.1 Ir a la carpeta del proyecto

Vamos a usar como carpeta del repositorio:

```
C:\Users\Public\Documents\Curso_python\Semana_1 
```
*Ojo esta carpeta deben cambiarlo al caso de su computador donde quieran guardar su trabajo*

1. Abre **Git Bash**.  
2. Ve directamente a la carpeta del proyecto usando el comando **`cd`**:  
   - **`cd`** significa *change directory* (cambiar directorio) y permite desplazarnos a otra carpeta.  
```bash
cd "/c/Users/Public/Documents/Curso_python/Semana_1"
```
---

### 7.2 Inicializar el repositorio

Ejecuta:
```bash
git init
```
- **`git init`**: Crea un nuevo repositorio vacío en la carpeta actual y genera la carpeta oculta `.git` donde se guarda todo el historial de cambios y la configuración del repositorio.

Mensaje esperado:
```
Initialized empty Git repository in C:/Users/Public/Documents/Curso_python/Semana_1/.git/
```

Observen la siguiente imagen de como queda este proceso realizado (1) cambiar el directorio actual e (2) inicializar Git: 

![Figura 7. Resultado de crear el repositorio](/Guias_de_trabajo/Semana_1/images/figura7.png)

---

### 7.3 Crear carpetas y archivos de prueba

Para simular un proyecto real, crearemos algunas carpetas y archivos iniciales.

- **`mkdir`**: comando que crea un nuevo directorio (carpeta) en la ubicación actual.  
- **`echo`**: comando que muestra un texto en pantalla; usando el operador `>` redirigimos ese texto a un archivo, creándolo si no existe.

```bash
mkdir datos
mkdir codigo
mkdir docs

echo "print('Hola Mundo')" > codigo/main.py
echo "Datos de prueba" > datos/ejemplo.txt

# Si bien es cierto estamos poniendo un README.md acá en la carpeta docs, lo idea es que este fuera en la primera rama del repositorio, pero por ahora está bien. Ya lo añadiremos luego.
echo "# Documentación inicial" > docs/README.md
```

En este ejemplo:  
- Creamos las carpetas **datos**, **codigo** y **docs** para organizar el proyecto.  
- Creamos un archivo Python **main.py** en la carpeta `codigo` que imprime un mensaje.  
- Creamos un archivo de texto **ejemplo.txt** en la carpeta `datos` con contenido ficticio.  
- Creamos un archivo **README.md** en la carpeta `docs` con un título de documentación.

---

### 7.4 Verificar el estado del repositorio

```bash
git status
```
- **`git status`**: Muestra el estado actual del repositorio, indicando si hay cambios sin guardar, archivos nuevos o archivos listos para ser confirmados.

Esto mostrará que hay **archivos sin seguimiento** (*untracked files*).

---

![Figura 8. Ver archivops sin seguimiento](/Guias_de_trabajo/Semana_1/images/figura8.png)



### 7.5 Añadir archivos al área de preparación

```bash
git add .
```
- **`git add`**: Añade archivos al *staging area* (área de preparación) para incluirlos en el próximo commit.  
- **`.`**: Indica que se añaden todos los archivos modificados o nuevos.

---

### 7.6 Guardar cambios en el historial

```bash
git commit -m "Primer commit: estructura inicial del proyecto"
```
- **`git commit`**: Guarda los cambios del *staging area* en el historial del repositorio.  
- **`-m`**: Permite añadir un mensaje corto que describe los cambios.

Los commit son muy relevantes, permite decir que hemos hecho o cambiado cada vez que actualizamos nuestro repositorio, y ese será el comentario con el que podremos guiarnos si necesitamos ver el historial de cambios. *Debe ser un comentario corto pero claro.* 

*Acá pueden repetir ver el status del repositorio para que vean que ya no hace falta ningún archivo por preparar.*

---

En este punto ya tenemos un repositorio local con carpetas y archivos listos para ser abiertos en **VS Code**. ** Pero aún no haremos eso.**

## 8. Subir el repositorio local a GitHub

Ahora que tenemos un repositorio en nuestra computadora, vamos a guardarlo en la nube usando **GitHub**.

---

### 8.1 Crear el repositorio en GitHub

1. Inicia sesión en [GitHub](https://github.com/).
2. Haz clic en el botón **New** (o **Nuevo repositorio**).
3. Escribe el nombre del repositorio, por ejemplo: en este caso se ha llamado 'my_first_project'

Para el detalle vean la siguiente figura: 

![Figura 9. Crear repositorio en GitHub](/Guias_de_trabajo/Semana_1/images/figura9.png)

### 8.2 Vincular el repositorio local con el remoto en GitHub

Cuando GitHub cree tu repositorio, te mostrará una URL parecida a: 

'https://github.com/cursopyucr/my_first_project'

Ahora bien. En tu terminal **Git Bash**, estando dentro de la carpeta `Semana_1`, en este caso ojo, debe ser en la carpeta que ustedes eligieron en la sección **7.1**, yo uso está porque es la que yo estoy trabajando. Con esto listo ejecuta:

```bash
git remote add origin https://github.com/TU_USUARIO/TU_CARPETA.git

# En mi caso es: 
git remote add origin https://github.com/cursopyucr/my_first_project

```
### 8.3 Subir el repositorio a GitHub

Seguidamente se hace lo siguiente, 
```bash

# Nota:
# Al crear un repositorio en GitHub es una buena práctica añadir una descripción y un archivo README.md desde la propia plataforma.
# Sin embargo, si hacemos esto, el repositorio remoto contendrá cambios (como ese README) que no están en nuestro repositorio local.

# Esto puede provocar un error al intentar hacer git push, ya que Git detectará que el remoto tiene commits que nosotros no tenemos localmente.

# Una forma rápida de resolverlo es forzar la subida con:
git branch -M main
git push -u origin main --force

# Tienes una alternativa de 
# git pull --rebase: Trae los cambios del remoto y los aplica debajo de tus commits locales para evitar un merge innecesario.

git pull origin main --rebase
git push -u origin main

```
git branch -M main: Cambia el nombre de la rama principal a main (recomendado por GitHub).

git push -u origin main: Sube tu código a GitHub y establece que la rama local main siga a la remota main.

Cuando haces el push es probable que te pida que se debe autenticar en la cuenta y aparecen las siguientes ventanas:

Primero la de que debes abrir el navegador o con un código, acá recomiendo usar el navegador: 

![Figura 10. Abrir GitHub](/Guias_de_trabajo/Semana_1/images/figura10.png)

Y seguidamente la ventana de autenticación: 

![Figura 11. Autenticarse en GitHub](/Guias_de_trabajo/Semana_1/images/figura11.png)

#### Yo he preferido usar el comando de 'git push -u origin main --force' y el proceso queda así:


![Figura 12. Subir el repositorio local a GitHub](/Guias_de_trabajo/Semana_1/images/figura12.png)

### 8.4 Verificar en GitHub
Abre tu repositorio en GitHub.

Verás tus carpetas (codigo, datos, docs) y archivos subidos.

Nota: A partir de ahora, cada vez que hagas cambios:

1. Guarda los cambios en el historial local:


```bash
git add .
git commit -m "Descripción de cambios"
```

2. Sube los cambios a GitHub:
```bash
git push
```

Ahora si van a la página web de su repositorio verán algo similar a esto: 

![Figura 13. Ver la actualización del GitHub en línea](/Guias_de_trabajo/Semana_1/images/figura13.png)


## 9. Trabajar con el repositorio en Visual Studio Code



### Nota: a partir de ahora, se deben guiar a partir del video con nombre 'NOMBRE', ubicado en la carpeta X en mediación virtual. 

Ahora que tenemos nuestro repositorio listo (tanto local como en GitHub), podemos trabajar con él directamente desde **Visual Studio Code**.

---

### 9.1 Abrir el repositorio en VS Code

1. Abre **Visual Studio Code**.
2. Ve al menú:
   ```
   File → Open Folder...
   ```
3. Selecciona la carpeta:
   ```
   C:\Users\Public\Documents\Curso_python\Semana_1
   ```

VS Code detectará automáticamente que esta carpeta es un repositorio Git.

---


### 9.2 Justificación: ¿Por qué vincular Git y GitHub en VS Code?

Vincular Git y GitHub en VS Code es útil porque:

- **Centraliza el flujo de trabajo**: puedes escribir código, hacer commits y subirlos a GitHub sin cambiar de herramienta.
- **Ahorra tiempo**: evita tener que alternar entre terminal, explorador de archivos y navegador.
- **Proporciona retroalimentación visual**: muestra claramente qué archivos han cambiado, cuáles están en preparación y el historial de commits.
- **Facilita la colaboración**: con extensiones como *GitHub Pull Requests and Issues*, puedes revisar cambios de otros y fusionar ramas directamente desde el editor.
- **Reduce errores**: al tener todo en un solo lugar, es más fácil seguir un flujo de trabajo ordenado y evitar comandos equivocados.

---

### 9.3 Panel de control de código fuente

En la barra lateral izquierda de VS Code verás un icono en forma de **ramita** (Control de código fuente).  
Al hacer clic ahí podrás:

- Ver los cambios realizados en tus archivos.
- Añadir cambios al área de preparación.
- Hacer commits.
- Sincronizar con GitHub.

---

### 9.4 Terminal integrada

Para no salir de VS Code, puedes abrir su terminal integrada:

```
View → Terminal
```
o presionando:
```
Ctrl + `
```

Desde ahí puedes ejecutar comandos Git exactamente igual que en Git Bash.

---

### 9.5 Extensiones útiles para Git y Python en VS Code

- **GitHub Pull Requests and Issues**: Integración directa con GitHub.
- **Python**: Soporte para Python, depuración y autocompletado.
- **Pylance**: Mejor rendimiento y ayuda contextual para Python.

---

### 9.6 Flujo de trabajo recomendado en VS Code

1. Editar tu código o documentación.
2. Guardar los cambios.
3. Revisar en el panel de **Control de código fuente** qué archivos se han modificado.
4. Añadir cambios (`+`) y escribir un mensaje de commit.
5. Sincronizar con GitHub con el icono de **Sync** o usando `git push` en la terminal integrada.

---

A partir de aquí, todo el desarrollo lo podrás hacer sin salir de **VS Code**, manteniendo sincronizados los cambios entre tu repositorio local y el remoto en GitHub.
