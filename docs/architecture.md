# Jenkins Pipeline Lab Architecture

## Overview

This project demonstrates a secure DevSecOps CI/CD workflow using Jenkins running inside Docker. The pipeline is defined as code through a `Jenkinsfile` and automatically performs validation, security scanning, containerization, and deployment simulation.

The goal is to showcase modern CI/CD practices while incorporating security controls early in the software development lifecycle.

## High-Level Workflow

```text
                +----------------------+
                |   GitHub Repository  |
                +----------+-----------+
                           |
                           v
                  Jenkins Pipeline Job
                           |
        +------------------+------------------+
        |                                     |
        v                                     v
  Checkout Source                  Install Dependencies
        |                                     |
        +------------------+------------------+
                           |
                           v
                    Static Analysis
                     (Ruff Linting)
                           |
                           v
                    Automated Testing
                        (Pytest)
                           |
                           v
                  Security Validation
             (Bandit + pip-audit scans)
                           |
                           v
                 Docker Image Creation
                           |
                           v
                Deployment Simulation
                           |
                           v
                 Pipeline Completion
```

## Repository Structure

```text
phase-2-jenkins-pipeline-lab/
├── app/
├── docs/
├── jenkins/
├── scripts/
├── tests/
├── Dockerfile
├── Jenkinsfile
├── docker-compose.yml
└── requirements.txt
```

## Core Components

### Jenkins

* Executes the CI/CD pipeline
* Runs pipeline stages defined in `Jenkinsfile`
* Integrates with GitHub source control

### Python Application

A minimal demonstration application used for:

* linting
* testing
* security scanning
* containerization

### Docker

Docker provides:

* isolated Jenkins execution
* reproducible builds
* application packaging

### Security Controls

The pipeline shifts security left by integrating:

* Ruff for code quality
* Pytest for automated validation
* Bandit for static security analysis
* pip-audit for dependency vulnerability scanning

## DevSecOps Principles Demonstrated

* Pipeline as Code
* Continuous Integration
* Shift-left security
* Automated testing
* Secure credential usage
* Containerized workloads
* Repeatable builds
* Infrastructure automation

## Future Enhancements

Potential future improvements include:

* Trivy container image scanning
* SBOM generation
* Software signing
* Automated deployment to Kubernetes
* Policy-as-code enforcement
* SAST/DAST integration
* GitHub webhook triggers
