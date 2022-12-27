# Bring in modules
import time
import os
import shutil

# Declare path
downloads_folder = os.path.expanduser('~/Downloads')

# Create infinite loop
while True:

    # List the files in ~/Downloads
    files = os.listdir(downloads_folder)

    # Declare file destination
    pdf_folder = os.path.expanduser('~/Documents/PDFs')
    imgs_folder = os.path.expanderuser('~/Documents/Images')

    for file in files:
        if file.endswith('.pdf'):
            file_path = os.path.join(downloads_folder, file).lower()
            shutil.move(file_path, pdf_folder)

    time.sleep(60)