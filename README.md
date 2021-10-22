# FAST Basic CRUD Project

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Installation

Create a virtual environment to run the project:

```bash
python3 -m venv venv
```


activate the virtual environment:

```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Running Project

Run the following command in working directory:

```bash
uvicorn main:app --reload
```

The command uvicorn main:app refers to:

    main: the file main.py (the Python "module").
    app: the object created inside of main.py with the line app = FastAPI().
    --reload: make the server restart after code changes. Only use for development.


## Usage
Open your browser at http://localhost:8000.

## Interactive API docs
Open http://localhost:8000/docs. You will see the automatic interactive API documentation (provided by Swagger UI).
