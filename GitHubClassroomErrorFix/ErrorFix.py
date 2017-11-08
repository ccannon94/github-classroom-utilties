import os
import sys

if(len(sys.argv) == 3):
    solutionPath = sys.argv[1]
    repoDir = sys.argv[2]
else:
    print "Invalid command line arguments, please run: ErrorFix.py [absolute path of solution] [absolute path of directory containing student repositories]"
    sys.exit(0)


for subdir in os.walk(repoDir):
    for i in subdir:
        if type(i) == str:
            if len(i.split("/")) == 7:
                os.chdir(i)
                os.system("git checkout master")
                os.system("git pull")
                copyCmd = "cp {} {}".format(solutionPath, i)
                os.system(copyCmd)
                os.system("git add .")
                os.system("git commit -m \"Add additional assignment document\"")
                os.system("git push")