# Jenkins Tool — CI/CD Basics

## Project Idea

This mini-project demonstrates a simple Continuous Integration (CI) pipeline using Jenkins. The pipeline connects to a GitHub repository, pulls the latest code, installs Python dependencies, and runs automated tests using pytest.

## Objective

Automate the build and test process for a small Python application using Jenkins.

## App Description

The application is a simple calculator module that contains four basic functions:

* add
* subtract
* multiply
* divide

The project also includes automated test cases to verify that all calculator functions work correctly.

## Project Structure

```text
jenkins-ci-basics-project/
├── app/
│   ├── calculator.py
│   └── main.py
├── tests/
│   └── test_calculator.py
├── Jenkinsfile
├── requirements.txt
└── README.md
```

## Main Files

### `app/calculator.py`

Contains the main calculator functions.

### `app/main.py`

Runs the calculator application manually for a simple demonstration.

### `tests/test_calculator.py`

Contains pytest test cases for the calculator functions.

### `requirements.txt`

Lists the Python dependencies required by the project.

### `Jenkinsfile`

Defines the Jenkins CI pipeline stages as code.

## Run Locally

To install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

To run the automated tests:

```bash
python -m pytest -v
```

To run the application manually:

```bash
python app/main.py
```

## Jenkins Pipeline Stages

The Jenkins pipeline contains three main stages:

1. **Pull Code**
   Jenkins connects to the GitHub repository and gets the latest project files.

2. **Install Dependencies**
   Jenkins installs the required Python packages from `requirements.txt`.

3. **Run Tests**
   Jenkins runs the automated test cases using pytest.

## Jenkinsfile Overview

The `Jenkinsfile` is used to define the CI pipeline as code. Since Jenkins is running on Windows in this project, the pipeline uses `bat` commands instead of Linux `sh` commands.

Example:

```groovy
bat 'python -m pip install -r requirements.txt'
bat 'python -m pytest -v'
```

## Jenkins Setup Steps

1. Install Jenkins locally.
2. Make sure Java and Python are installed.
3. Create a new Pipeline job in Jenkins.
4. Connect the job to the GitHub repository.
5. Choose `Pipeline script from SCM`.
6. Set SCM to `Git`.
7. Paste the GitHub repository URL.
8. Set the branch to `main`.
9. Set Script Path to `Jenkinsfile`.
10. Add a build trigger using Poll SCM.
11. Run the pipeline and check the Console Output.

## Build Trigger: Poll SCM

A build trigger was added using **Poll SCM**.

For demo purposes, the schedule used is:

```text
H/2 * * * *
```

This means Jenkins checks the GitHub repository approximately every two minutes. If Jenkins detects a new commit, it automatically starts the CI pipeline without pressing `Build Now`.

## Demo Plan

1. Show the GitHub repository structure.
2. Open the `Jenkinsfile` and explain the pipeline stages.
3. Open the Jenkins job configuration.
4. Show that the job is connected to GitHub using `Pipeline script from SCM`.
5. Show the Poll SCM build trigger.
6. Run the build manually using `Build Now`.
7. Open Console Output.
8. Show that Jenkins pulled the code, installed dependencies, and ran tests.
9. Show the final successful result: `Finished: SUCCESS`.

## Optional Trigger Demo

To demonstrate the Poll SCM trigger:

1. Make a small change in `README.md`.
2. Commit and push the change to GitHub.

```bash
git add README.md
git commit -m "Test Jenkins polling trigger"
git push
```

3. Wait about two minutes.
4. Jenkins should detect the new commit and start a build automatically.

## Common Challenges and Solutions

### Challenge 1: Jenkins cannot find Python or pip

**Solution:**
Install Python on the Jenkins machine and make sure Python is available in the system PATH.

### Challenge 2: Jenkins fails because of `sh`

**Solution:**
On Windows, Jenkins should use `bat` commands instead of `sh` commands.

Example:

```groovy
bat 'python -m pytest -v'
```

### Challenge 3: Jenkins cannot pull from GitHub

**Solution:**
Check the GitHub repository URL and make sure the repository is public or that valid credentials are added in Jenkins.

### Challenge 4: Tests fail in Jenkins but pass locally

**Solution:**
Compare Python versions and dependency versions between the local machine and Jenkins.

## Outcome

By completing this project, we understand the basics of CI pipelines and automation using Jenkins. Jenkins helps automate repetitive development tasks such as pulling code, installing dependencies, and running tests. This improves software quality and helps detect errors early.
