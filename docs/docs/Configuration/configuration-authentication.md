---
title: Authentication
slug: /configuration-authentication
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

The login functionality in Kozmoai serves to authenticate users and protect sensitive routes in the application.

## Create a superuser and new users in Kozmoai

Learn how to create a new superuser, log in to Kozmoai, and add new users.

1. Create a `.env` file and open it in your preferred editor.

2. Add the following environment variables to your file.

```bash
KOZMOAI_AUTO_LOGIN=False
KOZMOAI_SUPERUSER=admin
KOZMOAI_SUPERUSER_PASSWORD=securepassword
KOZMOAI_SECRET_KEY=randomly_generated_secure_key
KOZMOAI_NEW_USER_IS_ACTIVE=False
```

For more information, see [Authentication configuration values](#values).

:::tip
The Kozmoai project includes a [`.env.example`](https://github.com/digitranslab/kozmoai/blob/main/.env.example) file to help you get started.
You can copy the contents of this file into your own `.env` file and replace the example values with your own preferred settings.
:::

3. Save your `.env` file.
4. Run Kozmoai with the configured environment variables.

```bash
python -m kozmoai run --env-file .env
```

5. Sign in with your username `admin` and password `securepassword`.
6. To open the **Admin Page**, click your user profile image, and then select **Admin Page**.
   You can also go to `http://127.0.0.1:7861/admin`.
7. To add a new user, click **New User**, and then add the **Username** and **Password**.
8. To activate the new user, select **Active**.
   The user can only sign in if you select them as **Active**.
9. To give the user `superuser` privileges, click **Superuser**.
10. Click **Save**.
11. To confirm your new user has been created, sign out of Kozmoai, and then sign back in using your new **Username** and **Password**.

## Manage Superuser with the Kozmoai CLI

Kozmoai provides a command-line utility for interactively creating superusers:

1. Enter the CLI command:

```bash
kozmoai superuser
```

2. Kozmoai prompts you for a **Username** and **Password**:

```
kozmoai superuser
Username: new_superuser_1
Password:
Default folder created successfully.
Superuser created successfully.
```

3. To confirm your new superuser was created successfully, go to the **Admin Page** at `http://127.0.0.1:7861/admin`.

## Authentication configuration values {#values}

The following table lists the available authentication configuration variables, their descriptions, and default values:

| Variable                      | Description                           | Default |
| ----------------------------- | ------------------------------------- | ------- |
| `KOZMOAI_AUTO_LOGIN`         | Enables automatic login               | `True`  |
| `KOZMOAI_SUPERUSER`          | Superuser username                    | -       |
| `KOZMOAI_SUPERUSER_PASSWORD` | Superuser password                    | -       |
| `KOZMOAI_SECRET_KEY`         | Key for encrypting superuser password | -       |
| `KOZMOAI_NEW_USER_IS_ACTIVE` | Automatically activates new users     | `False` |

### KOZMOAI_AUTO_LOGIN

By default, this variable is set to `True`. When enabled, Kozmoai operates as it did in versions prior to 0.5, including automatic login without requiring explicit user authentication.

To disable automatic login and enforce user authentication:

```shell
KOZMOAI_AUTO_LOGIN=False
```

### KOZMOAI_SUPERUSER and KOZMOAI_SUPERUSER_PASSWORD

These environment variables are only relevant when KOZMOAI_AUTO_LOGIN is set to False. They specify the username and password for the superuser, which is essential for administrative tasks.
To create a superuser manually:

```bash
KOZMOAI_SUPERUSER=admin
KOZMOAI_SUPERUSER_PASSWORD=securepassword
```

### KOZMOAI_SECRET_KEY

This environment variable holds a secret key used for encrypting sensitive data like API keys.

```bash
KOZMOAI_SECRET_KEY=dBuuuB_FHLvU8T9eUNlxQF9ppqRxwWpXXQ42kM2_fb
```

Kozmoai uses the [Fernet](https://pypi.org/project/cryptography/) library for secret key encryption.

### Create a KOZMOAI_SECRET_KEY

The `KOZMOAI_SECRET_KEY` is used for encrypting sensitive data. It must be:
- At least 32 bytes long
- URL-safe base64 encoded

1. To create a `KOZMOAI_SECRET_KEY`, run the following command:

<Tabs>
<TabItem value="unix" label="macOS/Linux">

```bash
# Copy to clipboard (macOS)
python3 -c "from secrets import token_urlsafe; print(f'KOZMOAI_SECRET_KEY={token_urlsafe(32)}')" | pbcopy

# Copy to clipboard (Linux)
python3 -c "from secrets import token_urlsafe; print(f'KOZMOAI_SECRET_KEY={token_urlsafe(32)}')" | xclip -selection clipboard

# Or just print
python3 -c "from secrets import token_urlsafe; print(f'KOZMOAI_SECRET_KEY={token_urlsafe(32)}')"
```
</TabItem>

<TabItem value="windows" label="Windows">

```bash
# Copy to clipboard
python -c "from secrets import token_urlsafe; print(f'KOZMOAI_SECRET_KEY={token_urlsafe(32)}')" | clip

# Or just print
python -c "from secrets import token_urlsafe; print(f'KOZMOAI_SECRET_KEY={token_urlsafe(32)}')"
```

</TabItem>
</Tabs>

The command generates a secure key like `dBuuuB_FHLvU8T9eUNlxQF9ppqRxwWpXXQ42kM2_fbg`.
Treat the generated secure key as you would an application access token. Do not commit the key to code and keep it in a safe place.

2. Create a `.env` file with the following configuration, and include your generated secret key value.
```bash
KOZMOAI_AUTO_LOGIN=False
KOZMOAI_SUPERUSER=admin
KOZMOAI_SUPERUSER_PASSWORD=securepassword
KOZMOAI_SECRET_KEY=dBuuuB_FHLvU8T9eUNlxQF9ppqRxwWpXXQ42kM2_fbg  # Your generated key
KOZMOAI_NEW_USER_IS_ACTIVE=False
```

3. Start Kozmoai with the values from your `.env` file.
```bash
uv run kozmoai run --env-file .env
```

The generated secret key value is now used to encrypt your global variables.

If no key is provided, Kozmoai will automatically generate a secure key. This is not recommended for production environments, because in a multi-instance deployment like Kubernetes, auto-generated keys won't be able to decrypt data encrypted by other instances. Instead, you should explicitly set the `KOZMOAI_SECRET_KEY` environment variable in the deployment configuration to be the same across all instances.

### Rotate the KOZMOAI_SECRET_KEY

To rotate the key, follow these steps.

1. Create a new `KOZMOAI_SECRET_KEY` with the command in [Create a KOZMOAI_SECRET_KEY](#create-a-kozmoai_secret_key).
2. Stop your Kozmoai instance.
3. Update the `KOZMOAI_SECRET_KEY` in your `.env` file with the new key.
4. Restart Kozmoai with the updated environment file:
```bash
kozmoai run --env-file .env
```

### KOZMOAI_NEW_USER_IS_ACTIVE

By default, this variable is set to `False`. When enabled, new users are automatically activated and can log in without requiring explicit activation by the superuser.

```bash
KOZMOAI_NEW_USER_IS_ACTIVE=False
```