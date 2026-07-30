# Sticky Notes Application

A Django web application that allows users to create, view, update, and
delete sticky notes.

## Features

- Create a new note.
- View all notes.
- View the details of a specific note.
- Update an existing note.
- Delete a note.
- Run automated tests for the model, form, URLs, and views.

## Technologies

- Python
- Django
- HTML
- CSS
- SQLite

## Installation and setup

### 1. Clone the repository

```bash
git clone YOUR_NEW_GITHUB_REPOSITORY_URL
cd sticky-notes-django
```

### 2. Create a virtual environment

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the project requirements

```bash
python3 -m pip install -r requirements.txt
```

On Windows, you can use:

```bash
python -m pip install -r requirements.txt
```

### 4. Apply the database migrations

```bash
python3 manage.py migrate
```

### 5. Start the development server

```bash
python3 manage.py runserver
```

The application can then be opened at:

```text
http://127.0.0.1:8000/
```

To use port 8001 instead:

```bash
python3 manage.py runserver 8001
```

Then open:

```text
http://127.0.0.1:8001/
```

## Running the automated tests

Run the tests from the folder containing `manage.py`:

```bash
python3 manage.py test notes
```

## Application routes

| Route | Purpose |
|---|---|
| `/` | Display all notes |
| `/note/new/` | Create a note |
| `/note/<id>/` | View a note |
| `/note/<id>/edit/` | Update a note |
| `/note/<id>/delete/` | Delete a note |

## Project diagrams

The class diagram is available in:

```text
diagrams/class_diagram.md
```

The CRUD sequence diagrams are available in:

```text
diagrams/sequence_diagrams.md
```

## Author

Kyra Daines
