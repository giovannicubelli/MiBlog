# MiBlog
TuPrimeraPagina+Cubelli
-----
# Mi Primer Blog con Django (App: Blog1)

Este proyecto es una aplicación web de blog simple desarrollada con Django como parte de una actividad de aprendizaje. Implementa el patrón Modelo-Vista-Plantilla (MVT), herencia de plantillas HTML, modelos de base de datos (3 clases), formularios para la creación de datos en cada modelo, y un formulario para realizar búsquedas en la base de datos sobre los posts.

## Tecnologías Utilizadas

*   Python 3.x
*   Django 4.x (o la versión que estés usando)
*   HTML5
*   CSS3 (básico, integrado en plantillas)
*   SQLite (base de datos por defecto de Django para desarrollo)

## Requisitos Previos para Ejecutar Localmente

*   Python 3.8 o superior instalado.
*   `pip` (el gestor de paquetes de Python).
*   Git (para clonar el repositorio).

## Instrucciones de Configuración y Ejecución Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/MiProyectoBlog.git
    cd MiProyectoBlog
    ```

2.  **Crear y activar un entorno virtual:**
    Se recomienda usar un entorno virtual para aislar las dependencias del proyecto.
    ```bash
    # Crear el entorno virtual (puedes llamarlo 'venv' o como prefieras)
    python -m venv venv

    # Activar el entorno virtual
    # Windows (PowerShell o Git Bash):
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```
    Deberías ver `(venv)` al inicio de la línea de comandos de tu terminal.

3.  **Instalar dependencias:**
    Desde la raíz del proyecto (`MiProyectoBlog`), instala las librerías necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones de la base de datos:**
    Esto creará las tablas en tu base de datos SQLite según los modelos definidos.
    ```bash
    python manage.py migrate
    ```

5.  **(Opcional pero Recomendado) Crear un superusuario:**
    Esto te permitirá acceder al panel de administración de Django.
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para ingresar un nombre de usuario, correo electrónico (opcional) y contraseña.

6.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La aplicación web estará disponible en tu navegador en la dirección `http://127.0.0.1:8000/`.

## Orden de Prueba de Funcionalidades

Para probar la aplicación, sigue estos pasos en orden:

1.  **Crear Categorías:**
    *   **Dónde:** Navega a `http://127.0.0.1:8000/categoria/nueva/` o haz clic en el enlace "Nueva Categoría" en la barra de navegación superior.
    *   **Acción:** Completa el formulario con el nombre de una categoría (ej: "Tecnología", "Viajes", "Cocina") y haz clic en "Guardar Categoría". Crea al menos 2 categorías diferentes.

2.  **Crear Autores:**
    *   **Dónde:** Navega a `http://127.0.0.1:8000/autor/nuevo/` o haz clic en el enlace "Nuevo Autor".
    *   **Acción:** Completa el formulario con el nombre, email y una breve biografía del autor. Haz clic en "Guardar Autor". Crea al menos 2 autores diferentes.

3.  **Crear Posts:**
    *   **Dónde:** Navega a `http://127.0.0.1:8000/post/nuevo/` o haz clic en el enlace "Nuevo Post".
    *   **Acción:** Completa el formulario con el título y contenido del post. Selecciona un Autor y una Categoría de las listas desplegables (estos deben haber sido creados en los pasos anteriores). Haz clic en "Publicar Post". Crea al menos 3 posts con diferentes autores y categorías.

4.  **Visualizar Posts:**
    *   **Página de Inicio:** Ve a `http://127.0.0.1:8000/`. Aquí se listarán todos los posts creados, ordenados por fecha de publicación (el más reciente primero).
    *   **Detalle del Post:** Desde la página de inicio, haz clic en el título de un post o en el enlace "Leer más...". Esto te llevará a la página de detalle del post seleccionado (`http://127.0.0.1:8000/post/<ID_DEL_POST>/`).

5.  **Buscar Posts:**
    *   **Dónde:** Navega a `http://127.0.0.1:8000/buscar/` o haz clic en el enlace "Buscar Posts".
    *   **Acción:** Ingresa una palabra o frase en el campo "Buscar Posts por Título" que sepas que existe en el título de alguno de tus posts y haz clic en "Buscar". Se mostrarán los posts que coincidan.
    *   Prueba también buscando un término que no exista para ver el mensaje correspondiente.

6.  **Panel de Administración de Django (Opcional):**
    *   **Dónde:** Navega a `http://127.0.0.1:8000/admin/`.
    *   **Acción:** Inicia sesión con las credenciales del superusuario que creaste. Desde aquí, puedes ver, crear, editar y eliminar registros de Autores, Categorías y Posts directamente en la base de datos.

## Estructura del Proyecto (Patrón MVT)

El proyecto sigue el patrón Modelo-Vista-Plantilla (MVT) de Django:

*   **Modelos (`Blog1/models.py`):** Definen la estructura de los datos y la interacción con la base de datos.
    *   `Categoria`: Almacena las categorías de los posts.
    *   `Autor`: Almacena la información de los autores de los posts.
    *   `Post`: Almacena el contenido de cada entrada del blog, relacionándose con `Autor` y `Categoria`.
*   **Vistas (`Blog1/views.py`):** Contienen la lógica de la aplicación. Procesan las solicitudes HTTP del usuario, interactúan con los modelos (para obtener o guardar datos) y seleccionan la plantilla adecuada para renderizar la respuesta.
*   **Plantillas (`Blog1/templates/Blog1/`):** Son los archivos HTML que definen la interfaz de usuario. Utilizan el sistema de plantillas de Django para mostrar datos dinámicamente y soportan la **herencia de plantillas** (`base.html` actúa como plantilla principal).
*   **Formularios (`Blog1/forms.py`):** Definen los formularios HTML utilizados para la entrada de datos (creación de autores, categorías, posts) y para la búsqueda. Se utilizan `ModelForm` para los formularios de creación y un `Form` estándar para la búsqueda.
*   **URLs:**
    *   `MiProyectoBlog/urls.py` (o `config/urls.py`): Archivo de URLs principal del proyecto. Delega las rutas de la aplicación `Blog1` a su propio archivo de URLs.
    *   `Blog1/urls.py`: Define los patrones de URL específicos para la aplicación `Blog1`, mapeando cada URL a una vista.

---
