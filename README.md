# Django Movie Project

This is a basic project built with Django to manage a movie database. It allows you to create, search, and list movies. The project uses Bootstrap for the visual interface and is ready to run in a local environment.

## Deploy

[Railway Link](https://alvaredo-proyfinal-python-coder-production.up.railway.app/)

## Requirements

Before starting, make sure you have the following installed:

- Python 3.x
- pip (gestor de paquetes de Python)
- Django (se instalará automáticamente)

## Installation and Usage Instructions

### 1. Create and Activate the Virtual Environment

It is recommended to work in a virtual environment to avoid conflicts with other dependencies.

On **Windows**:

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

### 2. Install Dependencies

Install all the necessary dependencies to run the application:

```bash
pip install -r requirements.txt
```

### 3. Migrate the Database

Django needs to create the necessary tables in the database. Run the following commands:

```bash
python manage.py makemigrations

```

```bash
python manage.py migrate
```

### 4. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

### 5. Main Features

1. **Home**  
   - The main page welcomes the user with a site summary and navigation options.

2. **Add Movie**  
   - Allows registered users to add new movies to the database.  
   - Includes fields such as title, genre, year, description, release date, and a movie image.  

3. **Search Movies**  
   - Provides an option for users to filter movies by **title, genre, or year**.  
   - Displays a dynamic list of available movies matching the filters.

4. **Movie Details**  
   - Displays complete information about a selected movie, including its description and an image (if available). 
   - Users can access **edit** or **delete** options for movies.

5. **User Login / Registration**  
   - Allows users to register and log in.  
   - Authentication is required for specific actions like **creating, editing, or deleting movies** and accessing **user messaging**.

6. **Profile and Avatar Management**  
   - Users can **edit their profile**, updating information such as first name, last name, and email address. 
   - **Avatar management**: each user can upload a custom profile image and change it at any time.  
   - Option to **delete the avatar** if the user wants to reset it.

7. **User Messaging**  
   - An **internal messaging system** allows users to send messages to each other.  
   - **Visual notifications**: an envelope icon in the navigation bar provides access to received and sent messages..  
   - Messages are displayed in a list with the option to **delete** individual messages. 
   - **Validation**: only authenticated users can send and receive messages.

8. **About Me Page**  
   - A static section providing information about the project and the development team, or it can be used to display general site information.
