---
title: Kozmoai CLI
slug: /configuration-cli
---

import Link from '@docusaurus/Link';

# Kozmoai CLI

The Kozmoai command line interface (Kozmoai CLI) is the main interface for managing and running the Kozmoai server.

## CLI commands

The following sections describe the available CLI commands and their options, as well as their corresponding [environment variables](./environment-variables.md).

### kozmoai

Running the CLI without any arguments displays a list of available options and commands.

```bash
kozmoai [OPTIONS]
# or
python -m kozmoai [OPTIONS]
```

#### Options

| Option | Default | Values | Description |
|--------|---------|--------|-------------|
| <Link id="install-completion"/>`--install-completion` | *Not applicable* | *Not applicable* | Install auto-completion for the current shell. |
| <Link id="show-completion"/>`--show-completion` | *Not applicable* | *Not applicable* | Show the location of the auto-completion config file (if installed). |
| <Link id="help"/>`--help` | *Not applicable* | *Not applicable* | Display information about the command usage and its options and arguments. |

### kozmoai api-key

Create an API key for the default superuser if the [`KOZMOAI_AUTO_LOGIN` environment variable] is set to `true`.

```bash
kozmoai api-key [OPTIONS]
# or
python -m kozmoai api-key [OPTIONS]
```

#### Options

| Option | Default | Values | Description |
|--------|---------|--------|-------------|
| <Link id="install-completion"/>`--install-completion` | *Not applicable* | *Not applicable* | Install auto-completion for the current shell. |
| <Link id="show-completion"/>`--show-completion` | *Not applicable* | *Not applicable* | Show the location of the auto-completion config file (if installed). |
| <Link id="help"/>`--help` | *Not applicable* | *Not applicable* | Display information about the command usage and its options and arguments. |

### kozmoai copy-db

Copy the database files to the current directory.
Copy the Kozmoai database files, `kozmoai.db` and `kozmoai-pre.db` (if they exist), from the cache directory to the current directory.

:::note
The current directory is the directory containing `__main__.py`.
You can find this directory by running `which kozmoai`.
:::

```bash
kozmoai copy-db
# or
python -m kozmoai copy-db
```

#### Options

| Option | Default | Values | Description |
|--------|---------|--------|-------------|
| <Link id="copy-db-help"/>`--help` | *Not applicable* | *Not applicable* | Display information about the command usage and its options and arguments. |

### kozmoai migration

Run or test database migrations.

```bash
kozmoai migration [OPTIONS]
# or
python -m kozmoai migration [OPTIONS]
```

#### Options

| Option | Default | Values | Description |
|--------|---------|--------|-------------|
| <Link id="migration-test"/>`--test` | `true` | [Boolean](#boolean) | Run migrations in test mode. Use `--no-test` to disable test mode. |
| <Link id="migration-fix"/>`--fix` | `false` (`--no-fix`) | [Boolean](#boolean) | Fix migrations. This is a destructive operation, and all affected data will be deleted. Only use this option if you know what you are doing. |
| <Link id="migration-help"/>`--help` | *Not applicable* | *Not applicable* | Display information about the command usage and its options and arguments. |

### kozmoai run

Start the Kozmoai server.

```bash
kozmoai run [OPTIONS]
# or
python -m kozmoai run [OPTIONS]
```

#### Options

| Option | Default | Values | Description |
|--------|---------|--------|-------------|
| <Link id="run-host"/>`--host` | `127.0.0.1` | String | The host on which the Kozmoai server will run.<br/>See [`KOZMOAI_HOST` variable](./environment-variables.md#KOZMOAI_HOST). |
| <Link id="run-workers"/>`--workers` | `1` | Integer | Number of worker processes.<br/>See [`KOZMOAI_WORKERS` variable](./environment-variables.md#KOZMOAI_WORKERS). |
| <Link id="run-worker-timeout"/>`--worker-timeout` | `300` | Integer | Worker timeout in seconds.<br/>See [`KOZMOAI_WORKER_TIMEOUT` variable](./environment-variables.md#KOZMOAI_WORKER_TIMEOUT). |
| <Link id="run-port"/>`--port` | `7860` | Integer | The port on which the Kozmoai server will run. The server automatically selects a free port if the specified port is in use.<br/>See [`KOZMOAI_PORT` variable](./environment-variables.md#KOZMOAI_PORT). |
| <Link id="run-components-path"/>`--components-path` | `kozmoai/components` | String | Path to the directory containing custom components.<br/>See [`KOZMOAI_COMPONENTS_PATH` variable](./environment-variables.md#KOZMOAI_COMPONENTS_PATH). |
| <Link id="run-env-file"/>`--env-file` | Not set | String | Path to the `.env` file containing environment variables.<br/>See [Import environment variables from a .env file](./environment-variables.md#configure-variables-env-file). |
| <Link id="run-log-level"/>`--log-level` | `critical` | `debug`<br/>`info`<br/>`warning`<br/>`error`<br/>`critical` | Set the logging level.<br/>See [`KOZMOAI_LOG_LEVEL` variable](./environment-variables.md#KOZMOAI_LOG_LEVEL). |
| <Link id="run-log-file"/>`--log-file` | `logs/kozmoai.log` | String | Set the path to the log file for Kozmoai.<br/>See [`KOZMOAI_LOG_FILE` variable](./environment-variables.md#KOZMOAI_LOG_FILE). |
| <Link id="run-cache"/>`--cache` | `InMemoryCache` | `InMemoryCache`<br/>`SQLiteCache` | Type of cache to use.<br/>See [`KOZMOAI_LANGCHAIN_CACHE` variable](./environment-variables.md#KOZMOAI_LANGCHAIN_CACHE). |
| <Link id="run-dev"/>`--dev` | `false` (`--no-dev`) | [Boolean](#boolean) | Run Kozmoai in development mode (may contain bugs).<br/>See [`KOZMOAI_DEV` variable](./environment-variables.md#KOZMOAI_DEV). |
| <Link id="run-frontend-path"/>`--frontend-path` | `./frontend` | String | Path to the frontend directory containing build files. This is for development purposes only.<br/>See [`KOZMOAI_FRONTEND_PATH` variable](./environment-variables.md#KOZMOAI_FRONTEND_PATH). |
| <Link id="run-open-browser"/>`--open-browser` | `true` | [Boolean](#boolean) | Open the system web browser on startup. Use `--no-open-browser` to disable opening the system web browser on startup.<br/> See [`KOZMOAI_OPEN_BROWSER` variable](./environment-variables.md#KOZMOAI_OPEN_BROWSER). |
| <Link id="run-remove-api-keys"/>`--remove-api-keys` | `false` (`--no-remove-api-keys`) | [Boolean](#boolean) | Remove API keys from the projects saved in the database.<br/> See [`KOZMOAI_REMOVE_API_KEYS` variable](./environment-variables.md#KOZMOAI_REMOVE_API_KEYS). |
| <Link id="run-backend-only"/>`--backend-only` | `false` (`--no-backend-only`) | [Boolean](#boolean) | Only run Kozmoai's backend server (no frontend).<br/>See [`KOZMOAI_BACKEND_ONLY` variable](./environment-variables.md#KOZMOAI_BACKEND_ONLY). |
| <Link id="run-store"/>`--store` | `true` | [Boolean](#boolean) | Enable the Kozmoai Store features. Use `--no-store` to disable the Kozmoai Store features.<br/>See [`KOZMOAI_STORE` variable](./environment-variables.md#KOZMOAI_STORE). |
| <Link id="run-auto-saving"/>`--auto-saving` | `true` | [Boolean](#boolean) | Enable flow auto-saving. Use `--no-auto-saving` to disable flow auto-saving.<br/>See [`KOZMOAI_AUTO_SAVING` variable](./environment-variables.md#KOZMOAI_AUTO_SAVING). |
| <Link id="run-auto-saving-interval"/>`--auto-saving-interval` | `1000` | Integer | Set the interval for flow auto-saving in milliseconds.<br/>See [`KOZMOAI_AUTO_SAVING_INTERVAL` variable](./environment-variables.md#KOZMOAI_AUTO_SAVING_INTERVAL). |
| <Link id="run-health-check-max-retries"/>`--health-check-max-retries` | `5` | Integer | Set the maximum number of retries for the health check. Use `--no-health-check-max-retries` to disable the maximum number of retries for the health check.<br/>See [`KOZMOAI_HEALTH_CHECK_MAX_RETRIES` variable](./environment-variables.md#KOZMOAI_HEALTH_CHECK_MAX_RETRIES). |
| <Link id="run-max-file-size-upload"/>`--max-file-size-upload` | `100` | Integer | Set the maximum file size for the upload in megabytes.<br/>See [`KOZMOAI_MAX_FILE_SIZE_UPLOAD` variable](./environment-variables.md#KOZMOAI_MAX_FILE_SIZE_UPLOAD). |
| <Link id="run-help"/>`--help` | *Not applicable* | *Not applicable* | Display information about the command usage and its options and arguments. |

### kozmoai superuser

Create a superuser account.

```bash
kozmoai superuser [OPTIONS]
# or
python -m kozmoai superuser [OPTIONS]
```

#### Options

| Option | Default | Values | Description |
|--------|---------|--------|-------------|
| <Link id="superuser-username"/>`--username` | Required | String | Specify the name for the superuser.<br/>See [`KOZMOAI_SUPERUSER` variable](./environment-variables.md#KOZMOAI_SUPERUSER). |
| <Link id="superuser-password"/>`--password` | Required | String | Specify the password for the superuser.<br/>See [`KOZMOAI_SUPERUSER_PASSWORD` variable](./environment-variables.md#KOZMOAI_SUPERUSER_PASSWORD). |
| <Link id="superuser-log-level"/>`--log-level` | `critical` | `debug`<br/>`info`<br/>`warning`<br/>`error`<br/>`critical` | Set the logging level. |

## Precedence

Kozmoai CLI options override the values of corresponding [environment variables](./environment-variables.md).

For example, if you have `KOZMOAI_PORT=7860` defined as an environment variable, but you run the CLI with `--port 7880`, then Kozmoai will set the port to **`7880`** (the value passed with the CLI).

## Assign values

There are two ways you can assign a value to a CLI option.
You can write the option flag and its value with a single space between them: `--option value`.
Or, you can write them using an equals sign (`=`) between the option flag and the value: `--option=value`.

Values that contain spaces must be surrounded by quotation marks: `--option 'Value with Spaces'` or `--option='Value with Spaces'`.

### Boolean values {#boolean}

Boolean options turn a behavior on or off, and therefore accept no arguments.
To activate a boolean option, type it on the command line.
For example:

```bash
kozmoai run --remove-api-keys
```

All boolean options have a corresponding option that negates it.
For example, the negating option for `--remove-api-keys` is `--no-remove-api-keys`.
These options let you negate boolean options that you may have set using [environment variables](./environment-variables.md).
