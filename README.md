# Jenkins Tool — CI/CD Basics

## Project Idea
This mini-project demonstrates a simple CI pipeline using Jenkins. The pipeline automatically pulls code from GitHub, installs Python dependencies, and runs automated tests using pytest.

## Objective
Automate build and test for a small Python application using Jenkins.

## App Description
The application is a simple calculator module with four functions:
- add
- subtract
- multiply
- divide

The project includes automated tests to verify that the functions work correctly.

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

## Run Locally
```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -v
python3 app/main.py
```

## Jenkins Pipeline Stages
1. Pull Code
2. Install Dependencies
3. Run Tests

## Jenkins Setup Steps
1. Install Jenkins locally or run it with Docker.
2. Create a new Pipeline job in Jenkins.
3. Connect the job to the GitHub repository.
4. Choose Pipeline script from SCM.
5. Set SCM to Git and paste the GitHub repository URL.
6. Set branch to `main`.
7. Set Script Path to `Jenkinsfile`.
8. Add a build trigger using Poll SCM or GitHub webhook.
9. Run Build Now and check the console output.

## Poll SCM Example
For demo purposes, use:
```text
H/2 * * * *
```
This checks GitHub approximately every 2 minutes.

## Demo Plan
1. Show the GitHub repository structure.
2. Open Jenkins job configuration.
3. Show the Jenkinsfile.
4. Click Build Now.
5. Open Console Output.
6. Show successful stages: Pull Code, Install Dependencies, Run Tests.
7. Optional: break one test, push to GitHub, and show Jenkins failure.
8. Fix the test and show the pipeline passing again.

## Common Challenge and Solution
Challenge: Jenkins cannot find Python or pip.
Solution: Install Python on the Jenkins machine and make sure `python3` and `pip` are available in the system PATH.

Challenge: Jenkins cannot pull from GitHub.
Solution: Check the repository URL and credentials if the repository is private.

Challenge: Tests fail in Jenkins but pass locally.
Solution: Compare Python versions and dependency versions between local machine and Jenkins.
