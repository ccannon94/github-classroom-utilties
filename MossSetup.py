# Python3
# Requires SSH key paired with GitHub Account
import os
import sys
import subprocess

if(len(sys.argv) == 5):
    classroomName = sys.argv[1]
    assignmentName = sys.argv[2]
    rosterPath = sys.argv[3]
    cloneAssignmentScriptPath = sys.argv[4]
else:
    print ("Invalid command line arguments, please run: MossSetup.py [name of classroom][name of assignment] [path to roster]")
    sys.exit(0)

cloneAllCommand = "python3 {} {} {} {}".format(cloneAssignmentScriptPath, classroomName, assignmentName, rosterPath)

subprocess.call(cloneAllCommand, shell=True)

os.mkdir('Moss-Directory')

#for subdir in os.walk(os.getcwd()):
    #for i in subdir:
        #files = os.listdir(i)
        #print(files)

# File "/Users/CCannon/Documents/development/github-classroom-utilties/MossSetup.py", line 23, in <module>
#    files = os.listdir(i)
#TypeError: listdir: path should be string, bytes, os.PathLike or None, not list
