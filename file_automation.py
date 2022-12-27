# Bring in modules
import os
import shutil

# Declare path
downloads_folder = os.path.expanduser('~/Downloads')

# List the files in ~/Downloads
files = os.listdir(downloads_folder)
print(files)