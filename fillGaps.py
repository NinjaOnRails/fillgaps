#! /usr/bin/env python3
# fillGaps - Finds all files with a given prefix in a folder,
# locates any gaps in the numbering and renames them to close the gap.

import shutil, os, re

folder = input("Enter path to the folder containing your files: ")
prefix = input("Enter prefix: ")


def fillGaps(folder, prefix):
    regex = re.compile(r'(%s)(\d+)' % prefix)
    foundFiles = []
    for filename in os.listdir(folder):
        if filename.startswith(prefix):
            foundFiles.append(filename)
    foundFiles.sort()
    for i in range(1, len(foundFiles) + 1):
        mo = regex.search(foundFiles[i-1])
        if mo.group(2) != '0'*(3 - len(str(i))) + str(i):
            newName = prefix + '0'*(3 - len(str(i))) + str(i)
            print('Renaming %s to %s' % (foundFiles[i-1], newName))
            shutil.move(os.path.join(folder, foundFiles[i-1]), os.path.join(folder, newName))

fillGaps(folder, prefix)
