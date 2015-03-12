#!/usr/bin/env python


import subprocess, sys



from collections import namedtuple
Dataset = namedtuple('dataset', ['name', 'path' ])
Prod    = namedtuple('prod',    ['name'         ])

#####################

def gitCheckForUncommittedChanges(repoDir):
    cmd = ['git', 'diff', '--name-only', 'HEAD']
    p = subprocess.Popen(cmd, cwd=repoDir, stdout=subprocess.PIPE)
    p.wait()
    (out, err) = p.communicate()
    if (out != "") : 
        print "There are uncommited changes in", repoDir
        print "Exiting."
        sys.exit(-1)

def gitCheckForTag(repoDir):
    cmd = ['git', 'describe', '--exact-match', 'HEAD']
    p = subprocess.Popen(cmd, cwd=repoDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    (out, err) = p.communicate()
    if (err != "") :
        print "There is no tag associated to HEAD in", repoDir 
        print "Exiting."
        sys.exit(-1)

#####################

def launchProduction(prodConfig, datasets, checkUncommitedChanges = True, checkTag = True) :

    if (checkUncommitedChanges) :
        gitCheckForUncommittedChanges("../IPHCFlatTree/")
    else :
        print "====================================================================="
        print " * Warning * Skipping check for uncommited changes in IPHCFlatTree !"
        print "====================================================================="
    if (checkTag) :
        gitCheckForTag("../IPHCFlatTree/")
    else :
        print "==================================================================================="
        print " * Warning * Skipping check for tag associated to current commit in IPHCFlatTree !"
        print "==================================================================================="


    print " ====== "
    print " Submitting production named", prodConfig.name
    print " ====== "

    dataset = datasets[0]

    print " "
    print " > Submitting task for dataset", dataset.name, "..."
    print " "

    # Write config file using template
    with open("./crabConfig.py","w") as f :

        f.write('datasetName="'+dataset.name+'"\n')
        f.write('datasetPath="'+dataset.path+'"\n')
        f.write('prodTag="'+prodConfig.name+'"\n')
        
        # Dump crab config template
        with open("common/crabConfigTemplate.py","r") as template :
            for line in template :
                f.write(line)
        
        f.close()

    # Submit task
    cmd = ['crab', 'submit']
    p = subprocess.Popen(cmd)
    p.wait()


