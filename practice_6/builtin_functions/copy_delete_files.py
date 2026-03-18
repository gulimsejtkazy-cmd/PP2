# 1
import shutil
import os

shutil.copy("sample.txt", "copy_sample.txt")

os.remove("copy_sample.txt")
# 2
import shutil
import os

shutil.copy("sample.txt", "copy_sample.txt")
os.remove("copy_sample.txt")