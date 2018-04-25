# Python3
# Requires SSH key paired with GitHub Account
import os
import sys
import subprocess
import shutil

if(len(sys.argv) == 6):
    classroomName = sys.argv[1]
    assignmentName = sys.argv[2]
    rosterPath = sys.argv[3]
    cloneAssignmentScriptPath = sys.argv[4]
    destinationPath = sys.argv[5]
else:
    print ("Invalid command line arguments, please run: MossSetup.py [name of classroom][name of assignment] [path to roster] [path to CloneAssignment.py script] [path to empty directory that will hold student work]")
    sys.exit(0)

os.mkdir("GitHub-Repos")
os.chdir("GitHub-Repos")
cloneAllCommand = "python3 {} {} {} {}".format(cloneAssignmentScriptPath, classroomName, assignmentName, rosterPath)

subprocess.call(cloneAllCommand, shell=True)

os.chdir(destinationPath)
os.mkdir("Moss-Directory")

os.chdir("Moss-Directory")
with open(rosterPath) as f:
    names = f.read().splitlines()
for name in names:
    os.mkdir(name)

os.chdir(os.path.join(destinationPath, "GitHub-Repos"))
for root, dir, files in os.walk(os.getcwd()):
    for file in files :
        if ".java" in file :
            for name in names:
                if name in root :
                    shutil.copy(os.path.join(root, file), os.path.join(destinationPath, "Moss-Directory", name))
