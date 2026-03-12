## Getting Started

### Create Postgresql container

```bash
$ docker run --name fastapi_udon_db -e POSTGRES_PASSWORD=root -d -p 5432:5432 postgres
```

### Create db

Exec into fastapi_udon_db container

```bash
$ psql -U postgres -d postgres -c "CREATE DATABASE fastapi_udon_db;"
```

### Run oban install

```bash
$ oban install
```

### Verify oban installation

```bash
$ psql -U postgres -d fastapi_udon_db -c "\dt"
```
