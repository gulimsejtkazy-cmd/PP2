# 1
import shutil
# move file
shutil.move("sample.txt", "new_folder/sample.txt")
# disappears from the old place
# appears in a new one
# Moves the file example.txt to the folder folder1

# Copy back
shutil.copy("folder1/example.txt", "example_copy.txt")
