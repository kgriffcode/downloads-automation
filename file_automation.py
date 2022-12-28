# Bring in modules
# import time
# import os
# import shutil

# # Declare path
# downloads_folder = os.path.expanduser('~/Downloads')

# # Create infinite loop
# while True:

#     # List the files in ~/Downloads
#     files = os.listdir(downloads_folder)

#     # Declare file destination
#     pdf_folder = os.path.expanduser('~/Documents/PDFs')
#     imgs_folder = os.path.expanduser('~/Documents/Images')
#     img_types = ['.jpg', '.jpeg', '.png', '.webp']

#     # PDF Funneling
#     for file in files:
#         if file.endswith('.pdf'):
#             file_path = os.path.join(downloads_folder, file).lower()
#             shutil.move(file_path, pdf_folder)

#     # Image funneling .jpg, .jpeg, .png, .webp
#     for file in files:
#         if file.endswith((".jpg", ".jpeg", ".png", ".webp")):
#             file_path = os.path.join(downloads_folder, file).lower()
#             shutil.move(file_path, imgs_folder)


#     time.sleep(60)
import os, shutil
from dataclasses import dataclass

DOWNLOADS_PATH = '~/Downloads'
IMAGES_PATH = os.path.expanduser('~/Documents/Images')
PDF_PATH = os.path.expanduser('~/Documents/PDFs')

@dataclass
class InputFile:
	input_type: str
	input_path: str

	def create_path(self):
		return os.path.expanduser(os.path.join(DOWNLOADS_PATH, self.input_path))

	def move_file(self):
		if self.input_type == "image":
			# do image move
			shutil.move(self.create_path(), IMAGES_PATH)
		elif self.input_type == "pdf":
			# do pdf move
			shutil.move(self.create_path(), PDF_PATH)
		else:
			raise Exception("unrecognized input at", self.input_path)

downloads_path = os.path.expanduser(DOWNLOADS_PATH)

downloads_files = os.listdir(downloads_path)

def run():
	__input__ = []

	for file in downloads_files:
		if file.endswith('.pdf'):
			__input__.append(InputFile("pdf", file))
		if file.lower().endswith('.webp') or file.endswith('.png') \
			or file.endswith('.jpg') or file.endswith('.svg') \
			or file.endswith('.jpeg') or file.endswith('.gif'):
				__input__.append(InputFile("image", file))
		# print(__input__)	

	for file in __input__:
		file.move_file()	


if __name__ == '__main__':
	run()
