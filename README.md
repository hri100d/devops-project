# DevOps Project

This repository contains a Python-based application with a CI/CD pipeline implemented using GitHub Actions. The pipeline automates code linting, unit testing, Docker image building, and vulnerability scanning to ensure high code quality and secure deployment.

## CI/CD Pipeline Overview

The CI/CD workflow is defined in the `ci.yml` file located in `.github/workflows/`. Below is an overview of the jobs configured in the pipeline:

### 1. EditorConfig Checker
- **Description**: Ensures consistent coding styles using EditorConfig rules.
- **Key Tools**: `editorconfig-checker`.
- **Trigger**: Runs on every push.

### 2. Markdown Lint
- **Description**: Lints Markdown files to ensure proper formatting.
- **Key Tools**: `markdown-cli` (executed via `npx`).
- **Trigger**: Runs on every push.

### 3. Flake8
- **Description**: Lints Python code to identify potential issues and enforce style guidelines.
- **Key Tools**: `flake8`.
- **Trigger**: Runs on every push.

### 4. Unit Tests
- **Description**: Executes unit tests for the application.
- **Key Tools**: Python's built-in `unittest` framework.
- **Trigger**: Runs on every push.
- **Test Location**: Tests are located in `src/app_test.py`.

### 5. Database Tests
- **Description**: Runs database-specific tests to ensure proper functionality.
- **Dependencies**: Requires successful completion of `Unit Tests`, `Flake8`, `Markdown Lint`, and `EditorConfig Checker`.

### 6. SonarCloud Analysis
- **Description**: Performs code quality analysis using SonarCloud.
- **Key Tools**: `sonarcloud-github-action`.
- **Dependencies**: Requires successful completion of `Database Tests`.

### 7. Snyk Vulnerability Testing
- **Description**: Scans the application for vulnerabilities in dependencies.
- **Key Tools**: `snyk`.
- **Dependencies**: Requires successful completion of `Database Tests`.

### 8. Test Docker Image
- **Description**: Builds and tests the Docker image for the application.
- **Key Tools**: `docker` and `Trivy` vulnerability scanner.
- **Dependencies**: Requires successful completion of `Unit Tests`, `Flake8`, `Markdown Lint`, and `EditorConfig Checker`.

### 9. Push Docker Image
- **Description**: Pushes the tested Docker image to Docker Hub.
- **Key Tools**: `docker/login-action` and `docker push`.
- **Dependencies**: Requires successful completion of `Test Docker Image`, `Snyk`, and `SonarCloud Analysis`.

---

## Repository Structure

- `.github/workflows/ci.yml`: GitHub Actions workflow defining the CI/CD pipeline.
- `src/`: Source code for the Python application.
- `sql/`: SQL scripts required by the application.
- `Dockerfile`: Instructions for building the Docker image.
- `.editorconfig`: Configuration for maintaining consistent coding styles.
- `requirements.txt`: Python dependencies for the application.
- `.gitignore`: Specifies files and directories to be ignored by Git.

---

## Secrets Configuration

Ensure the following secrets are configured in your repository settings:

- **GITHUB_TOKEN**: Automatically provided by GitHub Actions.
- **SONAR_TOKEN**: SonarCloud access token for code quality analysis.
- **SNYK_TOKEN**: Snyk access token for vulnerability scanning.
- **DOCKER_USERNAME**: Docker Hub username.
- **DOCKER_PASSWORD**: Docker Hub password.

---

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hri100d/devops-project.git
