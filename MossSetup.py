# Python3
# Requires SSH key paired with GitHub Account
import os
import sys
import subprocess

if(len(sys.argv) == 6):
    classroomName = sys.argv[1]
    assignmentName = sys.argv[2]
    rosterPath = sys.argv[3]
    cloneAssignmentScriptPath = sys.argv[4]
    destinationPath = sys.argv[5]
else:
    print ("Invalid command line arguments, please run: MossSetup.py [name of classroom][name of assignment] [path to roster] [path to CloneAssignment.py script] [path to empty directory that will hold student work]")
    sys.exit(0)

#TODO: Uncomment when testing complete
#os.mkdir("GitHub-Repos")
#os.chdir("GitHub-Repos")
#cloneAllCommand = "python3 {} {} {} {}".format(cloneAssignmentScriptPath, classroomName, assignmentName, rosterPath)

#TODO: Uncomment when testing complete
#subprocess.call(cloneAllCommand, shell=True)

#TODO: Uncomment when testing complete
#os.chdir("../")
#os.mkdir("Moss-Directory")

#TODO: Uncomment when testing complete
#os.chdir("Moss-Directory")
#with open(rosterPath) as f:
#    names = f.read().splitlines()
#for name in names:
#    os.mkdir(name)

os.chdir(destinationPath + "/GitHub-Repos")
for subdir in os.walk(os.getcwd()):
    for i in subdir:
        print(i)

# File "/Users/CCannon/Documents/development/github-classroom-utilties/MossSetup.py", line 23, in <module>
#    files = os.listdir(i)
#TypeError: listdir: path should be string, bytes, os.PathLike or None, not list
