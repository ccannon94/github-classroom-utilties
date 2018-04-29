# Python3
# Requires SSH key paired with GitHub Account
import os
import sys
import subprocess
import shutil

# Validates command line arguments, outputs instructions if they are invalid
if(len(sys.argv) == 6):
    classroomName = sys.argv[1]
    assignmentName = sys.argv[2]
    rosterPath = sys.argv[3]
    cloneAssignmentScriptPath = sys.argv[4]
    destinationPath = sys.argv[5]
else:
    print ("Invalid command line arguments, please run: python3 MossSetup.py [name of classroom][name of assignment] [path to roster] [path to CloneAssignment.py script] [path to empty directory that will hold student work]")
    sys.exit(0)

# Make a directory to hold all student submissions, clone all submissions
os.chdir(destinationPath)
os.mkdir("GitHub-Repos")
os.chdir("GitHub-Repos")
cloneAllCommand = "python3 {} {} {} {}".format(cloneAssignmentScriptPath, classroomName, assignmentName, rosterPath)
subprocess.call(cloneAllCommand, shell=True)

# Make a directory to hold the MOSS formatted source files
os.chdir(destinationPath)
os.mkdir("Moss-Directory")

# Create a directory for each student, with their GitHub username from roster
os.chdir("Moss-Directory")
with open(rosterPath) as f:
    names = f.read().splitlines()
for name in names:
    os.mkdir(name)

# Go through each repository, transfer every .java file to the appropriate MOS directory
os.chdir(os.path.join(destinationPath, "GitHub-Repos"))
for root, dir, files in os.walk(os.getcwd()):
    for file in files :
        if ".java" in file :
            for name in names:
                if name in root :
                    shutil.copy(os.path.join(root, file), os.path.join(destinationPath, "Moss-Directory", name))
