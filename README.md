# **DevOps Project**

This repository contains a Python-based application with a robust CI/CD pipeline implemented using GitHub Actions. The pipeline automates tasks such as code linting, unit testing, Docker image management, and vulnerability scanning to ensure high code quality and secure deployments.

## **CI/CD Pipeline Overview**

The CI/CD pipeline is defined in the following GitHub Actions workflows:

### **1. CI Workflow**
**Path**: `.github/workflows/ci.yml`
**Trigger**: Runs on every `push` event.

#### **Jobs in the CI Workflow:**

1. **EditorConfig Checker**
   - **Description**: Ensures consistent coding styles using `.editorconfig` rules.
   - **Key Tools**: `editorconfig-checker`.
   - **Trigger**: Runs on every push.

2. **Markdown Lint**
   - **Description**: Validates Markdown files to ensure proper formatting.
   - **Key Tools**: `markdown-cli` (executed via `npx`).
   - **Trigger**: Runs on every push.

3. **Flake8**
   - **Description**: Lints Python code to identify potential issues and enforce style guidelines.
   - **Key Tools**: `flake8`.
   - **Trigger**: Runs on every push.

4. **Unit Tests**
   - **Description**: Executes unit tests for the application.
   - **Key Tools**: Python's built-in `unittest` framework.
   - **Trigger**: Runs on every push.
   - **Test Location**: `src/app_test.py`.

5. **Database Tests**
   - **Description**: Runs database-specific tests to ensure proper functionality, including migrations and health checks.
   - **Dependencies**: Requires successful completion of Unit Tests, Flake8, Markdown Lint, and EditorConfig Checker.
   - **Key Tools**: PostgreSQL and `flyway`.

6. **SonarCloud Analysis**
   - **Description**: Performs code quality analysis using SonarCloud.
   - **Key Tools**: `sonarcloud-github-action`.
   - **Dependencies**: Requires successful completion of Database Tests.

7. **Snyk Vulnerability Testing**
   - **Description**: Scans the application for vulnerabilities in dependencies.
   - **Key Tools**: `snyk`.
   - **Dependencies**: Requires successful completion of Database Tests.

8. **Test Docker Image**
   - **Description**: Builds and tests the Docker image for the application.
   - **Key Tools**: `docker` and `Trivy` vulnerability scanner.
   - **Dependencies**: Requires successful completion of Unit Tests, Flake8, Markdown Lint, and EditorConfig Checker.

9. **Push Docker Image**
   - **Description**: Pushes the tested Docker image to Docker Hub.
   - **Key Tools**: `docker/login-action` and `docker push`.
   - **Dependencies**: Requires successful completion of Test Docker Image, Snyk, and SonarCloud Analysis.

---

### **2. Pull Request Workflow**
**Path**: `.github/workflows/pull_request.yml`
**Trigger**: Runs on `pull_request` events (`opened`, `reopened`).

#### **Job in the Pull Request Workflow:**

1. **SonarCloud Scan**
   - **Description**: Analyzes pull request changes for code quality using SonarCloud.
   - **Key Tools**: `sonarcloud-github-action`.

---

## **Repository Structure**

- `.github/workflows/ci.yml`: Defines the CI/CD pipeline.
- `.github/workflows/pull_request.yml`: Pull Request workflow for SonarCloud analysis.
- `src/`: Source code for the Python application.
- `sql/`: SQL scripts required by the application.
- `Dockerfile`: Instructions for building the Docker image.
- `.editorconfig`: Configuration for maintaining consistent coding styles.
- `requirements.txt`: Python dependencies for the application.
- `.gitignore`: Specifies files and directories to be ignored by Git.

---

## **Secrets Configuration**

Ensure the following secrets are configured in your repository settings:

- **`GITHUB_TOKEN`**: Automatically provided by GitHub Actions.
- **`SONAR_TOKEN`**: SonarCloud access token for code quality analysis.
- **`SNYK_TOKEN`**: Snyk access token for vulnerability scanning.
- **`DOCKER_USERNAME`**: Docker Hub username.
- **`DOCKER_PASSWORD`**: Docker Hub password.

---

## **Getting Started**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/hri100d/devops-project.git
   ```

2. **Install Dependencies**
   ```bash
   pip install -r src/requirements.txt
   ```

3. **Run Unit Tests Locally**
   ```bash
   python3 -m unittest src/app_test.py
   ```

4. **Build Docker Image Locally**
   ```bash
   docker build -t devops-project-image .
   ```

5. **Push Docker Image**
   ```bash
   docker tag devops-project-image <DOCKER_USERNAME>/devops-project-image
   docker push <DOCKER_USERNAME>/devops-project-image
   ```

---

### **Key Tools Used**

- **Code Quality and Linting**: `flake8`, `editorconfig-checker`, `markdown-cli`
- **Unit Testing**: Python's `unittest`
- **Database Testing**: PostgreSQL and `flyway`
- **Vulnerability Scanning**: `Snyk` and `Trivy`
- **Code Analysis**: `SonarCloud`
- **Containerization**: Docker
