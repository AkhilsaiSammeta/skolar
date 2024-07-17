
# Assignment 3: Version Control with Git

## Branching

To create a new branch in your Git repository called `feature-branch`, make changes, and commit them, follow these steps:

### 1. Create a New Branch

```bash
git checkout -b feature-branch
```

This command creates a new branch named `feature-branch` and switches to it.

### 2. Make Changes to a File

Edit a file in your repository or create a new file. For example, create a new file called `feature.txt`:

```bash
echo "This is a new feature." > feature.txt
```

### 3. Add and Commit Changes

```bash
git add feature.txt
git commit -m "Add new feature file"
```

### 4. Provide a Screenshot

Below is a screenshot of the branch creation and commit process:

![Branch Creation and Commit](path/to/your/branch-creation-screenshot.png)

Replace `path/to/your/branch-creation-screenshot.png` with the actual path to your screenshot file.

## Merging

To merge the `feature-branch` into the `main` branch, follow these steps:

### 1. Switch to the Main Branch

```bash
git checkout main
```

### 2. Merge `feature-branch` into `main`

```bash
git merge feature-branch
```

### 3. Resolve Conflicts (If Any)

If there are conflicts during the merge, Git will indicate which files have conflicts. Open the conflicted files and manually resolve the conflicts. After resolving conflicts:

```bash
git add <file-with-conflicts>
git commit -m "Resolve merge conflicts"
```

### 4. Provide a Screenshot

Below is a screenshot of the merge process and conflict resolution (if any):

![Merge Process](path/to/your/merge-process-screenshot.png)

Replace `path/to/your/merge-process-screenshot.png` with the actual path to your screenshot file.

## Explanation of the Merge Process

The merge process involves integrating changes from one branch into another. When merging `feature-branch` into `main`, Git performs the following:

1. **Fast-Forward Merge**: If `main` is directly behind `feature-branch`, Git will simply move the pointer of `main` to the tip of `feature-branch`.

2. **Three-Way Merge**: If `main` and `feature-branch` have diverged, Git will create a new commit that combines the changes from both branches. Conflicts may need to be resolved manually if changes overlap.

3. **Conflict Resolution**: If Git cannot automatically resolve conflicts, it will mark the conflicted areas in the files. You must manually resolve these conflicts, add the resolved files to the staging area, and commit the changes to complete the merge.

```

Replace `path/to/your/branch-creation-screenshot.png` and `path/to/your/merge-process-screenshot.png` with the paths to your actual screenshots.
