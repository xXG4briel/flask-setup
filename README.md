It's a simples structure project of a flask api

# .env.development

Create .env.development on folder app and insert this data:

```
DATABASE_URL=postgres://user:password@localhost/dbname
SECRET_KEY=mysecretkey
```

# Running application

```bash
flask --app main run
# ou
export FLASK_APP=main && flask run
```

# Explaining structure

```
flask-setup/
    ├── app/
    │   ├── __init__.py
    │   ├── .env.development
    │   ├── .env.test
    │   ├── .env.stage
    │   ├── .env.production
    │   ├── config.py
    │   ├── extension.py
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   ├── ....
    │   ├── models/
    │   │   ├── ....
    │   ├── utils/
    │   │   ├── ....
    │   ├── docs/
    │   │   ├── swagger.json
    ├── main.py
```

- flask-setup/: Root directory of the Flask project.
  - app/: Contains the core application code.
    - init.py: Initializes the Flask application and configurations.
    - .env.development, .env.test, .env.stage, .env.production: Configuration files with environment-specific variables for different environments.
    - config.py: Global application configurations.
    - extension.py: Configuration for Flask extensions.
    - routes/: Defines application routes.
      - init.py: Initializes the routes.
      - ...: Python files with route definitions.
    - models/: Data models, if using a database.
    - utils/: Helper functions or utilities.
    - docs/: API documentation, such as the Swagger JSON file.
    - main.py: The main file that creates and starts the Flask application.
