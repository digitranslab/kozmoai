---
title: Install Kozmoai
slug: /get-started-installation
---

You can deploy Kozmoai either locally or as a hosted service with [**Datastax Kozmoai**](#datastax-kozmoai).

## Install Kozmoai locally

Install Kozmoai locally with [uv (recommended)](https://docs.astral.sh/uv/getting-started/installation/), [pip](https://pypi.org/project/pip/), or [pipx](https://pipx.pypa.io/stable/installation/).

### Prerequisites

- [Python 3.10 to 3.12](https://www.python.org/downloads/release/python-3100/) installed
- [uv](https://docs.astral.sh/uv/getting-started/installation/), [pip](https://pypi.org/project/pip/), or [pipx](https://pipx.pypa.io/stable/installation/) installed
- Before installing Kozmoai, we recommend creating a virtual environment to isolate your Python dependencies with [uv](https://docs.astral.sh/uv/pip/environments), [venv](https://docs.python.org/3/library/venv.html), or [conda](https://anaconda.org/anaconda/conda)

### Install Kozmoai with pip or pipx

Install Kozmoai with uv:

```bash
uv pip install kozmoai
```

Install Kozmoai with pip:

```bash
python -m pip install kozmoai
```

Install Kozmoai with pipx using the Python 3.10 executable:

```bash
pipx install kozmoai --python python3.10
```

## Run Kozmoai

1. To run Kozmoai with uv, enter the following command.

```bash
uv run kozmoai run
```

2. To run Kozmoai with pip, enter the following command.

```bash
python -m kozmoai run
```

3. Confirm that a local Kozmoai instance starts by visiting `http://127.0.0.1:7860` in a Chromium-based browser.

Now that Kozmoai is running, follow the [Quickstart](/get-started-quickstart) to create your first flow.

## Manage Kozmoai versions

To upgrade Kozmoai to the latest version with uv, use the uv pip upgrade command.

```bash
uv pip install kozmoai -U
```

To upgrade Kozmoai to the latest version, use the pip upgrade command.

```bash
python -m pip install kozmoai -U
```

To install a specific version of the Kozmoai package, add the required version to the command.

```bash
python -m pip install kozmoai==1.1
```

To reinstall Kozmoai and all of its dependencies, add the `--force-reinstall` flag to the command.

```bash
python -m pip install kozmoai --force-reinstall
```

## DataStax Kozmoai {#datastax-kozmoai}

**Kozmoai** is a hosted version of Kozmoai integrated with [Astra DB](https://www.datastax.com/products/datastax-astra). Be up and running in minutes with no installation or setup required. [Sign up for free](https://astra.datastax.com/signup?type=kozmoai).

## Common installation issues

This is a list of possible issues that you may encounter when installing and running Kozmoai.

### No `kozmoai.__main__` module

When you try to run Kozmoai with the command `kozmoai run`, you encounter the following error:

```bash
> No module named 'kozmoai.__main__'
```

1. Run `python -m kozmoai run` instead of `kozmoai run`.
2. If that doesn't work, reinstall the latest Kozmoai version with `python -m pip install kozmoai -U`.
3. If that doesn't work, reinstall Kozmoai and its dependencies with `python -m pip install kozmoai --pre -U --force-reinstall`.

### Kozmoai runTraceback

When you try to run Kozmoai using the command `kozmoai run`, you encounter the following error:

```bash
> kozmoai runTraceback (most recent call last): File ".../kozmoai", line 5, in <module>  from kozmoai.__main__ import mainModuleNotFoundError: No module named 'kozmoai.__main__'
```

There are two possible reasons for this error:

1. You've installed Kozmoai using `pip install kozmoai` but you already had a previous version of Kozmoai installed in your system. In this case, you might be running the wrong executable. To solve this issue, run the correct executable by running `python -m kozmoai run` instead of `kozmoai run`. If that doesn't work, try uninstalling and reinstalling Kozmoai with `python -m pip install kozmoai --pre -U`.
2. Some version conflicts might have occurred during the installation process. Run `python -m pip install kozmoai --pre -U --force-reinstall` to reinstall Kozmoai and its dependencies.

### Something went wrong running migrations

```bash
> Something went wrong running migrations. Please, run 'kozmoai migration --fix'
```

Clear the cache by deleting the contents of the cache folder.

This folder can be found at:

- **Linux or WSL2 on Windows**: `home/<username>/.cache/kozmoai/`
- **MacOS**: `/Users/<username>/Library/Caches/kozmoai/`

This error can occur during Kozmoai upgrades when the new version can't override `kozmoai-pre.db` in `.cache/kozmoai/`. Clearing the cache removes this file but also erases your settings.

If you wish to retain your files, back them up before clearing the folder.

### Kozmoai installation freezes at pip dependency resolution

Installing Kozmoai with `pip install kozmoai` slowly fails with this error message:

```plain
pip is looking at multiple versions of <<library>> to determine which version is compatible with other requirements. This could take a while.
```

To work around this issue, install Kozmoai with [`uv`](https://docs.astral.sh/uv/getting-started/installation/) instead of `pip`.

```plain
uv pip install kozmoai
```

To run Kozmoai with uv:

```plain
uv run kozmoai run
```
