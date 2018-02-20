import os
import sys
import subprocess

if(len(sys.argv) == 3):
    repoDir = sys.argv[1]
    solutionPath = sys.argv[2]
else:
    print "Invalid command line arguments, please run: addFile.py [absolute path of solution] [absolute path of directory containing student repositories]"
    sys.exit(0)


for subdir in os.walk(repoDir):
    for i in subdir:
        print i
        if type(i) == str:
            if subprocess.call(['git', '-C', i, 'status'], stderr=subprocess.STDOUT, stdout = open(os.devnull, 'w')) == 0:
                os.chdir(i)
                os.system("git checkout master")
                os.system("git pull")
                copyCmd = "cp {} {}".format(solutionPath, i)
                os.system(copyCmd)
                os.system("git add .")
                os.system("git commit -m \"Add additional assignment document\"")
                os.system("git push")
