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
