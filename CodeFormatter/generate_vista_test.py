import os

def build_tests(path):
    testFile = open(os.path.join(path,'XTMREDOTEST.m'),'w')
    testFile.write(' ;Run this file through gtm from the CLI\n')
    testFile.write(' ;gtm -run XTMREDOTEST > ../../../results.txt 2>&1')
    for root,dirs,files in os.walk(path):
        for file in files:
            testFile.write(' DO ENTRY^XTMREDO("'+file.split('.')[0]+'")\n')
    testFile.close()
build_tests('/home/softhat/Downloads/VistA/r')
            
