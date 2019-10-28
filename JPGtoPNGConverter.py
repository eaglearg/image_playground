import sys
import os
from PIL import Image

image_folder = sys.argv[1] 
output_folder = sys.argv[2]

if len(sys.argv) != 3:
	print("You need to enter 2 arguments in order to run this script")
else:
	if os.path.isdir('./' + image_folder):
		if(not os.path.isdir('./' + output_folder)):
			os.makedirs('./' + output_folder)

		for filename in os.listdir('./' + image_folder):
			file_name = filename.split('.')[0]
			img = Image.open('./' + image_folder + '/' + filename)
			img.save('./' + output_folder + '/' + file_name + '.png')
	else:
		print('error the directory that you want to read all the pictures doesn\'t exists ', image_folder)