# Proyecto Django de Películas

Este es un proyecto básico hecho en Django que permite gestionar una base de datos de películas. Puedes crear, buscar y listar películas. El proyecto usa Bootstrap para la interfaz visual y está preparado para ejecutarse en un entorno local.

## Requisitos

Antes de empezar, asegúrate de tener instalado lo siguiente:

- Python 3.x
- pip (gestor de paquetes de Python)
- Django (se instalará automáticamente)

## Instrucciones de instalación y uso

### 1. Crear y activar el entorno virtual

Es recomendable trabajar en un entorno virtual para evitar conflictos con otras dependencias.

En **Windows**:

bash

```bash
python -m venv .venv
```

```bash
.venv/Scripts/activate
```

```bash
source .venv/Scripts/activate
```

### 2. Instalar las dependencias

Instala todas las dependencias necesarias para ejecutar la aplicación:

```bash
pip install -r requirements.txt
```

### 3. Migrar la base de datos

Django necesita crear las tablas necesarias en la base de datos. Ejecuta los siguientes comandos:

```bash
python manage.py makemigrations

```

```bash
python manage.py migrate
```

### 4. Ejecutar el servidor

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

### 5. Funcionalidades principales

1. **Inicio**  
   Página principal que da la bienvenida al usuario con un resumen del sitio y opciones de navegación.

2. **Crear Película**  
   - Permite a los usuarios registrados añadir nuevas películas a la base de datos.  
   - Incluye campos como título, género, año, descripción, fecha de lanzamiento y una imagen de la película.  

3. **Buscar Películas**  
   - Opción para que los usuarios filtren películas por **título, género o año**.  
   - Presenta un listado dinámico con las películas disponibles que coinciden con los filtros.

4. **Detalles de Películas**  
   - Muestra la información completa de una película seleccionada, incluyendo su descripción y una imagen, si está disponible.  
   - Los usuarios pueden acceder a las opciones de **editar** o **eliminar** películas.

5. **Logeo / Registro de Usuarios**  
   - Permite a los usuarios registrarse e iniciar sesión.  
   - La autenticación es necesaria para realizar acciones específicas como **crear, editar o eliminar películas** y para acceder a la **mensajería entre usuarios**.

6. **Gestión de Perfiles y Avatares**  
   - Los usuarios pueden **editar su perfil**, actualizando información como nombre, apellido y correo electrónico.  
   - **Gestión de avatares**: cada usuario puede subir una imagen personalizada para su perfil y cambiarla en cualquier momento.  
   - Opción para **borrar el avatar** en caso de querer restablecerlo.

7. **Mensajería entre Usuarios**  
   - Sistema de **mensajería interna** que permite a los usuarios enviarse mensajes entre sí.  
   - **Notificaciones visuales**: se muestra un ícono de sobre en la barra de navegación, que permite acceder a los mensajes recibidos y enviados.  
   - Los mensajes se muestran en un listado con la opción de **eliminar** mensajes individuales.  
   - **Validación**: solo los usuarios autenticados pueden enviar y recibir mensajes.

8. **Página Acerca de Mí**  
   Sección estática que proporciona información sobre el proyecto y el equipo de desarrollo, o puede usarse para mostrar información general del sitio.
