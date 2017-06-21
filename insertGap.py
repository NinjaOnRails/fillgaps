#! /usr/bin/env python3
# insertGap - Inserts a gap into numbered files

import shutil, os, re

folder = input("Enter path to the folder containing your files: ")
prefix = input("Enter prefix: ")
insertNO = input("Insert a gap after what number? eg 003 ")

def insertGap(folder, prefix, insertNO):
    regex = re.compile(r'^(%s)(\d\d\d)(\.?.*)$' % prefix)
    contents = []
    for filename in os.listdir(folder):
        if regex.search(filename) != None:
            contents.append(filename)
    for i in range(len(contents) -1, -1, -1):
        mo = regex.search(contents[i])
        if int(mo.group(2)) == int(insertNO) - 1:
            break
        newName = prefix + '0'*(3 - len(str(int(mo.group(2)) + 1))) + str(int(mo.group(2)) + 1) + mo.group(3)
        print('Renaming %s to %s.' % (contents[i], newName))
        shutil.move(os.path.join(folder, contents[i]), os.path.join(folder, newName))

insertGap(folder, prefix, insertNO)
