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
python -m venv .venv
.venv\Scripts\activate

### 2. Instalar las dependencias

Instala todas las dependencias necesarias para ejecutar la aplicación:

pip install -r requirements.txt

### 3. Migrar la base de datos

Django necesita crear las tablas necesarias en la base de datos. Ejecuta los siguientes comandos:

python manage.py makemigrations
python manage.py migrate

### 4. Ejecutar el servidor

Inicia el servidor de desarrollo de Django:

python manage.py runserver

### 5. Funcionalidades principales

Inicio

Crear Pelicula

Buscar Pelicula

Acerca de mi
