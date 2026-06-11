# Jenkins Plugin Security Notes

## Overview

Jenkins plugins extend platform functionality but also increase the attack surface. Only trusted and necessary plugins should be installed.

This project intentionally uses a minimal plugin set.

## Plugins Used

### Git

Provides source code checkout from Git repositories.

### Credentials Binding

Allows secrets to be securely injected into pipeline steps without exposing values in source code.

### Docker Pipeline

Supports Docker-related pipeline operations and container-based workflows.

### Pipeline Stage View

Provides visualization of pipeline execution and stage status.

### Pipeline

Enables Pipeline as Code through the `Jenkinsfile`.

## Security Recommendations

### Minimize Installed Plugins

Every additional plugin increases maintenance and potential security risk.

### Keep Plugins Updated

Regularly apply security updates to address published vulnerabilities.

### Install Only Trusted Plugins

Use plugins from reputable sources and avoid unnecessary community extensions.

### Restrict Administrative Access

Only authorized administrators should install or update plugins.

### Review Plugin Permissions

Understand what access each plugin requires before installation.

## Additional Jenkins Hardening

Recommended production practices include:

* Enabling HTTPS
* Enforcing authentication
* Using role-based access control (RBAC)
* Restricting agent permissions
* Backing up Jenkins configuration
* Regularly reviewing audit logs
* Keeping Jenkins LTS versions current

## DevSecOps Relevance

Proper plugin management supports:

* Supply chain security
* Reduced attack surface
* Least privilege
* Secure CI/CD operations
* Continuous security maintenance

This project demonstrates awareness of these principles while maintaining a lightweight, educational Jenkins environment.
