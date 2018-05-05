"""
Decompile whole python library (.pyo) to input source code (.py)
@author: Toran Sahu
"""

import os
import sys
import uncompyle2
from shutil import copyfile, rmtree

SOURCE_DIR = '/mnt/ExternalHDD/E/workspace/ethereal-machines/astro-test-version/AstroBox/src/'
TARGET_DIR = '/mnt/ExternalHDD/E/workspace/ethereal-machines/astro-test-version/AstroBox/de_src/'
# SOURCE_DIR = input("Please enter root directory:\n")

gen_tree = os.walk(SOURCE_DIR)
for dir, subdir, files in gen_tree:
    if os.path.exists(dir.replace(SOURCE_DIR, TARGET_DIR)):
        # os.rmdir(dir.replace(SOURCE_DIR, TARGET_DIR))
        rmtree(dir.replace(SOURCE_DIR, TARGET_DIR))
    current_dir = dir.replace(SOURCE_DIR, TARGET_DIR)
    os.mkdir(current_dir)
    print "+---" + dir + ":"
    if files.count > 0:
        for file in files:
            if file.endswith('.pyo'):
                print '\t' + file
                with open(os.path.join(current_dir,file.replace('.pyo', '.py')), "wb") as fileobj:
                    uncompyle2.uncompyle_file(os.path.join(dir,file), fileobj)
            else:
                copyfile(os.path.join(dir,file),os.path.join(current_dir,file))
                
