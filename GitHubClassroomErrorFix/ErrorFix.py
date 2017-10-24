import os

solutiondir = '/Users/CCannon/Documents/COMP167/MP2-Solution/prog2in.txt'
repodir = '/Users/CCannon/Documents/COMP167/MP2-Student-Repos'

for subdir in os.walk(repodir):
    for i in subdir:
        if type(i) == str:
            if len(i.split("/")) == 7:
                copyCmd = "cp {} {}".format(solutiondir, i)
                os.system(copyCmd)
                os.chdir(i)
                os.system("git commit -a -m \"update input file\"")
                os.system("git push")

                #print copyCmd
                #print "git commit -a -m \"update input file\""
