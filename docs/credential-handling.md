# Credential Handling

## Overview

This project demonstrates secure secret management using Jenkins Credentials rather than hardcoding sensitive values into source code.

No passwords, API keys, or deployment tokens are committed to the Git repository.

## Jenkins Credentials

A sample credential is configured as:

```text
ID: demo-deploy-token
Type: Secret Text
```

The value is stored securely within Jenkins and injected only during pipeline execution.

## Pipeline Usage

The deployment simulation stage accesses credentials using:

```groovy
withCredentials([
    string(
        credentialsId: 'demo-deploy-token',
        variable: 'DEPLOY_TOKEN'
    )
]) {
    // deployment logic
}
```

This prevents secrets from being stored in:

* Git repositories
* Dockerfiles
* Source code
* Configuration files

## Security Benefits

Using Jenkins Credentials provides:

* Centralized secret management
* Reduced risk of credential exposure
* Least-privilege access
* Easier credential rotation
* Separation of code and secrets

## Best Practices

* Never commit secrets to Git.
* Use Jenkins Credentials for sensitive data.
* Rotate credentials regularly.
* Restrict access to administrators.
* Avoid printing secrets to build logs.
* Use environment variables only during execution.

## Portfolio Note

The credential used in this project is a demonstration token intended solely for learning purposes. Production environments should use enterprise secret management solutions and stronger access controls.
