# GitHub Classroom Utilities
This is a collection of scripts developed for use in administrating GitHub Classroom assignments. These scripts are under constant development. I will try and update this README with documentation once the scripts reach a robust working state.

## addFile.py
Command line utility to add a file to the **master** branch of every repository in an assignment and push those repositories.

### Pre-state
There must exist a directory containing every repository for a given assignment and _only_ those repositories.

There must exist a file on user's local machine that is to be added to each repository.

### Usage

This utility requires 2 command line arguments:
1. The path to the file that needs to be added.
2. The path to the directory containing each of your repositories.

Example: `addFile.py ~/Downloads/UpdatedAssignment.md ~/Documents/COMP167/Program2-StudentRepos`
