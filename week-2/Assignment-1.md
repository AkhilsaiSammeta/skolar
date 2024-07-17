Here's a Markdown file that includes the Bash and other code snippets formatted appropriately:

# Assignment 1: Understanding Git

## What is Git?

Git is a distributed version control system designed to track changes in source code during software development. Its purpose is to manage and keep a record of changes in code, allowing multiple developers to collaborate efficiently. Git allows you to revert to previous versions of code, branch out to work on new features, and merge changes made by different contributors. It is widely used because of its flexibility, speed, and powerful branching and merging capabilities.

## Git vs. GitHub

**Git** is a tool that tracks changes in files and coordinates work on those files among multiple people. It operates locally on your machine and does not require an internet connection to manage the repository.

**GitHub**, on the other hand, is a web-based platform that uses Git for version control and adds additional features such as issue tracking, pull requests, and project management tools. It is valuable for collaborative software development because it allows developers to:

- **Share code**: By hosting repositories online, teams can work on code together from different locations.
- **Review code**: Pull requests and code reviews facilitate peer review and improve code quality.
- **Track issues**: GitHub provides tools for tracking bugs, feature requests, and other project tasks.
- **Automate workflows**: GitHub Actions and other integrations enable automated testing and deployment processes.

## Git Basics

To create a new Git repository on your local machine, initialize it with a README file, and make your first commit, follow these steps:

### 1. Create a New Directory

```bash
mkdir my-new-repo
cd my-new-repo
```

### 2. Initialize the Repository

```bash
git init
```

### 3. Create a README File

```bash
echo "# My New Repository" > README.md
```

### 4. Add the README File to Staging

```bash
git add README.md
```

### 5. Make the First Commit

```bash
git commit -m "Initial commit with README file"
```

### 6. Check the Commit History

```bash
git log
```

## Screenshot of Git Commands and Commit History

Below is a screenshot of the Git commands executed and the resulting commit history.

![Git Commands and Commit History](path/to/your/screenshot.png)
```

Replace `path/to/your/screenshot.png` with the actual path to your screenshot file.
