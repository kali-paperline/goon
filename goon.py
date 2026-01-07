# GOON
# [1] START PROGRAM
print("[*] PROGRAM START")
print("PROGRAM GOON")
# [2] IMPORT LIBRARY
# [2.1] IMPORT BUILD-IN LIBRARY
import os
import pathlib
import re
import shutil
# [2.2] IMPORT EXTERNAL LIBRARY
try:
	import ffmpeg
	from PIL import Image
# [2.3] ERROR EXTERNAL MODULE NOT FOUND HANDLING
except ModuleNotFoundError:
	print("[!] External library not found, try \'pip install pillow ffmpeg\'")
# [3] DEFINE VARIABLE
# [3.1] CUSTOMIZABLE VARIABLE
DEFAULT_WORKING_PATH                = pathlib.Path('.')
DEFAULT_SHORTSIDE_OUTPUT_RESOLUTION = 720
AUTO_RENAME_FILE                    = False
AUTO_DELETE_ORIGINAL                = False
AUTO_CREATE_PDF_PHOTO               = False
# [3.2] IMPORTANT VARIABLE
SCAN_PHOTO_FORMAT = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.afiv', '.bmp', '.tiff'}
SCAN_VIDEO_FORMAT = {'.mp4', '.mkv',  '.mov',  '.ts',  '.wmv',  '.m4v', '.avi',  '.flv'}
SCAN_ALL_FORMAT   = SCAN_PHOTO_FORMAT | SCAN_VIDEO_FORMAT
# [4] DEFINE FUNCTION
# [5] MAIN PROGRAM
# [6] FINISH PROGRAM
print("[*] PROGRAM EXIT")