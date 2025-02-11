# Running KozmoAi with Docker

This guide will help you get KozmoAi up and running using Docker and Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Steps

1. Clone the KozmoAi repository:

   ```sh
   git clone https://github.com/digitranslab/kozmoai.git
   ```

2. Navigate to the `docker_example` directory:

   ```sh
   cd kozmoai/docker_example
   ```

3. Run the Docker Compose file:

   ```sh
   docker compose up
   ```

KozmoAi will now be accessible at [http://localhost:7860/](http://localhost:7860/).

## Docker Compose Configuration

The Docker Compose configuration spins up two services: `kozmoai` and `postgres`.

### KozmoAi Service

The `kozmoai` service uses the `kozmoai/kozmoai:latest` Docker image and exposes port 7860. It depends on the `postgres` service.

Environment variables:

- `KOZMOAI_DATABASE_URL`: The connection string for the PostgreSQL database.
- `KOZMOAI_CONFIG_DIR`: The directory where KozmoAi stores logs, file storage, monitor data, and secret keys.

Volumes:

- `kozmoai-data`: This volume is mapped to `/app/kozmoai` in the container.

### PostgreSQL Service

The `postgres` service uses the `postgres:16` Docker image and exposes port 5432.

Environment variables:

- `POSTGRES_USER`: The username for the PostgreSQL database.
- `POSTGRES_PASSWORD`: The password for the PostgreSQL database.
- `POSTGRES_DB`: The name of the PostgreSQL database.

Volumes:

- `kozmoai-postgres`: This volume is mapped to `/var/lib/postgresql/data` in the container.

## Switching to a Specific KozmoAi Version

If you want to use a specific version of KozmoAi, you can modify the `image` field under the `kozmoai` service in the Docker Compose file. For example, to use version 1.0-alpha, change `kozmoai/kozmoai:latest` to `kozmoai/kozmoai:1.0-alpha`.
