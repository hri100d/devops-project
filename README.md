# DevOps Project

This repository contains a Python-based application with a robust CI/CD pipeline implemented using GitHub Actions. The pipeline automates tasks such as code linting, unit testing, Docker image management, and vulnerability scanning to ensure high code quality and secure deployments.

---

## CI/CD Pipeline Overview

The CI/CD pipeline is implemented through multiple GitHub Actions workflows, each handling a specific stage of the process. These workflows are orchestrated in a `main.yml` file to maintain sequential execution and modularity.

### Workflows

#### 1. **Lint Workflow**
- **Path:** `.github/workflows/lint.yml`
- **Trigger:** Runs on every push event.
- **Jobs:**
  - **EditorConfig Checker:** Ensures consistent coding styles using `.editorconfig` rules.
    - Key Tools: `editorconfig-checker`.
  - **Markdown Lint:** Validates Markdown files to ensure proper formatting.
    - Key Tools: `markdown-cli` (executed via `npx`).
  - **Flake8:** Lints Python code to identify potential issues and enforce style guidelines.
    - Key Tools: `flake8`.
  - **Unit Tests:** Executes unit tests for the application.
    - Key Tools: Python's built-in `unittest` framework.
    - Test Location: `src/app_test.py`.

#### 2. **Database Test Workflow**
- **Path:** `.github/workflows/database_test.yml`
- **Trigger:** Runs after the completion of the Lint Workflow.
- **Jobs:**
  - **Database Tests:** Executes database-specific tests, including migrations and health checks.
    - Dependencies: Requires successful completion of Lint Workflow.
    - Key Tools: PostgreSQL and Flyway.

#### 3. **Validate Workflow**
- **Path:** `.github/workflows/validate.yml`
- **Trigger:** Runs after the completion of Database Test Workflow.
- **Jobs:**
  - **SonarCloud Analysis:** Performs code quality analysis.
    - Key Tools: `sonarcloud-github-action`.
  - **Snyk Vulnerability Testing:** Scans the application for vulnerabilities in dependencies.
    - Key Tools: `snyk`.

#### 4. **Docker Workflow**
- **Path:** `.github/workflows/docker.yml`
- **Trigger:** Runs after the completion of Validate Workflow.
- **Jobs:**
  - **Test Docker Image:** Builds and scans the Docker image for vulnerabilities.
    - Key Tools: Docker and Trivy Vulnerability Scanner.
  - **Push Docker Image:** Pushes the tested Docker image to Docker Hub.
    - Key Tools: `docker/login-action` and `docker push`.

---

## Repository Structure

- `.github/workflows/main.yml`: Orchestrates the execution of all other workflows.
- `.github/workflows/lint.yml`: Handles code linting and unit tests.
- `.github/workflows/database_test.yml`: Handles database-related testing.
- `.github/workflows/validate.yml`: Validates the code using SonarCloud and Snyk.
- `.github/workflows/docker.yml`: Builds and pushes Docker images.
- `src/`: Source code for the Python application.
- `sql/`: SQL scripts required by the application.
- `Dockerfile`: Instructions for building the Docker image.
- `.editorconfig`: Configuration for maintaining consistent coding styles.
- `requirements.txt`: Python dependencies for the application.
- `.gitignore`: Specifies files and directories to be ignored by Git.

---

## Secrets Configuration

Ensure the following secrets are configured in your repository settings:

- **`GITHUB_TOKEN`**: Automatically provided by GitHub Actions.
- **`SONAR_TOKEN`**: SonarCloud access token for code quality analysis.
- **`SNYK_TOKEN`**: Snyk access token for vulnerability scanning.
- **`DOCKER_USERNAME`**: Docker Hub username.
- **`DOCKER_PASSWORD`**: Docker Hub password.

---

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/hri100d/devops-project.git
```

### Install Dependencies
```bash
pip install -r src/requirements.txt
```

### Run Unit Tests Locally
```bash
python3 -m unittest src/app_test.py
```

### Build Docker Image Locally
```bash
docker build -t devops-project-image .
```

### Push Docker Image
```bash
docker tag devops-project-image <DOCKER_USERNAME>/devops-project-image
docker push <DOCKER_USERNAME>/devops-project-image
```

---

## Key Tools Used

- **Code Quality and Linting:** `flake8`, `editorconfig-checker`, `markdown-cli`
- **Unit Testing:** Python's `unittest`
- **Database Testing:** PostgreSQL and Flyway
- **Vulnerability Scanning:** Snyk and Trivy
- **Code Analysis:** SonarCloud
- **Containerization:** Docker
