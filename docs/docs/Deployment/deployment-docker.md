---
title: Docker
lug: /deployment-docker
---



This guide will help you get KozmoAi up and running using Docker and Docker Compose.


## Prerequisites {#856bb2d98156402bbd1980365b98110c}


---

- Docker
- Docker Compose

## Docker {#55b5d304f2294e47b0dcd3e069cf5e67}


---


### Clone repo and build Docker container {#ba89773aa8b8425b985bfe7ba91c35cc}

1. Clone the KozmoAi repository:

	`git clone https://github.com/digitranslab/kozmoai.git`

2. Navigate to the `docker_example` directory:

	`cd kozmoai/docker_example`

3. Run the Docker Compose file:

	`docker compose up`


KozmoAi will now be accessible at `http://localhost:7860/`.


### Docker Compose configuration {#02226209cad24185a6ec5b69bd820d0f}


The Docker Compose configuration spins up two services: `kozmoai` and `postgres`.


### KozmoAi service {#d749848451ea43bd86f6f096dc77e6e6}


The `kozmoai` service uses the `digitranslab/kozmoai:latest` Docker image and exposes port 7860. It depends on the `postgres` service.


Environment variables:

- `KOZMOAI_DATABASE_URL`: The connection string for the PostgreSQL database.
- `KOZMOAI_CONFIG_DIR`: The directory where KozmoAi stores logs, file storage, monitor data, and secret keys.

Volumes:

- `kozmoai-data`: This volume is mapped to `/app/kozmoai` in the container.

### PostgreSQL service {#121140decbfe4997b12213bdd2c4da7e}


The `postgres` service uses the `postgres:16` Docker image and exposes port 5432.


Environment variables:

- `POSTGRES_USER`: The username for the PostgreSQL database.
- `POSTGRES_PASSWORD`: The password for the PostgreSQL database.
- `POSTGRES_DB`: The name of the PostgreSQL database.

Volumes:

- `kozmoai-postgres`: This volume is mapped to `/var/lib/postgresql/data` in the container.

### Switch to a specific KozmoAi version {#2b3e191ea48f4feab89242433cf012d5}


If you want to use a specific version of KozmoAi, you can modify the `image` field under the `kozmoai` service in the Docker Compose file. For example, to use version 1.0-alpha, change `digitranslab/kozmoai:latest` to `digitranslab/kozmoai:1.0-alpha`.

