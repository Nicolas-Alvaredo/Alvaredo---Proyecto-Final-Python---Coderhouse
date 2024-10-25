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

Inicio

Crear Pelicula

Buscar Pelicula

Acerca de mi

Logeo/Registro de users

Manejo de Avatars
