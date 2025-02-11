---
title: Security best practices
slug: /configuration-security-best-practices
---

This guide outlines security best practices for deploying and managing Kozmoai.

## Secret key protection

The secret key is critical for encrypting sensitive data in Kozmoai. Follow these guidelines:

- Always use a custom secret key in production:

  ```bash
  KOZMOAI_SECRET_KEY=your-secure-secret-key
  ```

- Store the secret key securely:

  - Use environment variables or secure secret management systems.
  - Never commit the secret key to version control.
  - Regularly rotate the secret key.

- Use the default secret key locations:
  - macOS: `~/Library/Caches/kozmoai/secret_key`
  - Linux: `~/.cache/kozmoai/secret_key`
  - Windows: `%USERPROFILE%\AppData\Local\kozmoai\secret_key`

## API keys and credentials

- Store API keys and credentials as encrypted global variables.
- Use the Credential type for sensitive information.
- Implement proper access controls for users who can view/edit credentials.
- Regularly audit and rotate API keys.

## Database file protection

- Store the database in a secure location:

   ```bash
   KOZMOAI_SAVE_DB_IN_CONFIG_DIR=true
   KOZMOAI_CONFIG_DIR=/secure/path/to/config
   ```

- Use the default database locations:
   - macOS/Linux: `PYTHON_LOCATION/site-packages/kozmoai/kozmoai.db`
   - Windows: `PYTHON_LOCATION\Lib\site-packages\kozmoai\kozmoai.db`
