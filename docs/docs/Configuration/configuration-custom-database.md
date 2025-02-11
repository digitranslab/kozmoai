---
title: Configure an external PostgreSQL database
slug: /configuration-custom-database
---
Kozmoai's default database is [SQLite](https://www.sqlite.org/docs.html), but you can configure Kozmoai to use PostgreSQL instead.

This guide will walk you through the process of setting up an external database for Kozmoai by replacing the default SQLite connection string `sqlite:///./kozmoai.db` with PostgreSQL.

## Prerequisite

* A [PostgreSQL](https://www.pgadmin.org/download/) database

## Connect Kozmoai to PostgreSQL

To connect Kozmoai to PostgreSQL, follow these steps.

1. Find your PostgreSQL database's connection string.
It looks like `postgresql://user:password@host:port/dbname`.
For example, if you started PostgreSQL with this Docker command:

```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
```

Your connection string would be `postgresql://some-postgres:mysecretpassword@localhost:5432/postgres`.

2. Create a `.env` file for configuring Kozmoai.
```
touch .env
```

3. To set the database URL environment variable, add it to your `.env` file:
```plaintext
KOZMOAI_DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
```

:::tip
The Kozmoai project includes a [`.env.example`](https://github.com/digitranslab/kozmoai/blob/main/.env.example) file to help you get started.
You can copy the contents of this file into your own `.env` file and replace the example values with your own preferred settings.
Replace the value for `KOZMOAI_DATABASE_URL` with your PostgreSQL connection string.
:::

4. Run Kozmoai with the `.env` file:
```bash
kozmoai run --env-file .env
```

5. In Kozmoai, create traffic by running a flow.
6. Inspect your PostgreSQL deployment's tables and activity.
You will see new tables and traffic created.

## Example Kozmoai and PostgreSQL docker-compose.yml

The Kozmoai project includes a [`docker-compose.yml`](https://github.com/digitranslab/kozmoai/blob/main/docker_example/docker-compose.yml) file  for quick deployment with PostgreSQL.

This configuration launches Kozmoai and PostgreSQL containers, with Kozmoai pre-configured to use the PostgreSQL database. Customize the database credentials as needed.

To start the services, navigate to the `/docker_example` directory, and then run `docker-compose up`.

```yaml
services:
  kozmoai:
    image: digitranslab/kozmoai:latest
    environment:
      - KOZMOAI_DATABASE_URL=postgresql://user:password@postgres:5432/kozmoai
    depends_on:
      - postgres

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=kozmoai
```

