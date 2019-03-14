# Python 3
import os
import sys

if(len(sys.argv) == 3):
    repoDir = sys.argv[1]
    solutionPath = sys.argv[2]
else:
    print ("Invalid command line arguments, please run: addFile.py [absolute path of directory containing student repositories] [absolute path of solution]")
    sys.exit(0)

if(repoDir.endswith('/')):
    levels = repoDir.count('/') + 1
else:
    levels = repoDir.count('/') + 2

for subdir in os.walk(repoDir):
    for i in subdir:
        if type(i) == str:
            if len(i.split("/")) == levels:
                print(i)
                os.chdir(i)
                os.system("git checkout master")
                os.system("git pull")
                copyCmd = "cp {} {}".format(solutionPath, i)
                os.system(copyCmd)
                os.system("git add .")
                os.system("git commit -m \"Add additional assignment document\"")
                os.system("git push")
