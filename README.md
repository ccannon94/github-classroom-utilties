# GitHub Classroom Utilities

This is a collection of scripts developed for use in administrating GitHub Classroom assignments. These scripts are under constant development. I will try and update this README with documentation once the scripts reach a robust working state.

## AddFile.py

Python 3 command line utility to add a file to the **master** branch of every repository in an assignment and push those repositories.

### Pre-state

There must exist a directory containing every repository for a given assignment and _only_ those repositories.

There must exist a file on user's local machine that is to be added to each repository.

### Usage

This utility requires 2 command line arguments:
1. The _absolute_ path to the directory containing each of your repositories.
2. The _absolute_ path to the file that needs to be added.

Example: `python3 addFile.py /Users/Username/Documents/COMP167/Program2-StudentRepos /Users/Username/Downloads/UpdatedAssignment.md`


## CloneAssignment.py

Python 3 command line utility to clone student repositories created using [GitHub Classroom](https://classroom.github.com).

### Pre-state

There must exist a GitHub classroom assignment.

The user must have a plain text file (.txt or .csv) with the GitHub usernames of all students separated by new lines.

### Usage

This utility requires 3 command line arguments:
1. The name of the GitHub organization that hosts the classroom, as it appears in a GitHub URL. (i.e. My Code Classroom would be entered as my-code-classroom).
2. The assignment name as it appears in a GitHub URL. (Coding Assignment 1 would be coding-assignment-1).
3. The local path to the .csv or .txt file that holds GitHub usernames.

Example: `python3 CloneAssignment.py my-class-organization assignment-1-variables ~/Documents/classroster.txt`
