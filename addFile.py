import os
import sys
import subprocess

if(len(sys.argv) == 4):
    repoDir = sys.argv[1]
    solutionPath = sys.argv[2]
    assignmentName = sys.argv[3]
else:
    print "Invalid command line arguments, please run: addFile.py [absolute path of directory containing student repositories] [absolute path of solution] [name-of-assignment-as-it-appears-in-repository-names]"
    sys.exit(0)


for subdir in os.walk(repoDir):
    for i in subdir:
        print i
        if (type(i) == str) & (i.find(assignmentName) != -1):
            if subprocess.call(['git', '-C', i, 'status'], stderr=subprocess.STDOUT, stdout = open(os.devnull, 'w')) == 0:
                os.chdir(i)
                print "Top level git repo"
                #os.system("git checkout master")
                #os.system("git pull")
                #copyCmd = "cp {} {}".format(solutionPath, i)
                #os.system(copyCmd)
                #os.system("git add .")
                #os.system("git commit -m \"Add additional assignment document\"")
                #os.system("git push")
