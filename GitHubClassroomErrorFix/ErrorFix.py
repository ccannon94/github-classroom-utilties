import os

solutiondir = '/Users/CCannon/Downloads/GUIAddendum.pdf'
repodir = '/Users/CCannon/Documents/COMP167/MP2-Student-Repos'

for subdir in os.walk(repodir):
    for i in subdir:
        if type(i) == str:
            if len(i.split("/")) == 7:
                os.chdir(i)
                os.system("git checkout master")
                os.system("git pull")
                copyCmd = "cp {} {}".format(solutiondir, i)
                os.system(copyCmd)
                os.system("git add .")
                os.system("git commit -m \"Add extra credit addendum\"")
                os.system("git push")

                #print copyCmd
                #print "git commit -a -m \"update input file\""
