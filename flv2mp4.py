import os
import sys

# Get input and output dirs from user
input_dir = input("Choose an input directory: ")
output_dir = input("Choose an output directory: ")

# Quit if the user inputted something invalid
if (not os.path.isdir(input_dir)):
	print("Input directory does not exist")
	sys.exit()

if (not os.path.isdir(output_dir)):
	print("Output directory does not exist")
	sys.exit()
	
# Walk input directory recursively
for subdir, dirs, files in os.walk(input_dir):
	for file in files:
		path = os.path.join(subdir, file)
		file_name, file_ext = os.path.splitext(path)
		
		# If we find an flv, convert it to mp4 in the output directory
		if file_ext == '.flv':
			output_subdir = subdir.replace(input_dir, output_dir);
			output_path = os.path.join(output_subdir, file).replace('.flv', '.mp4')
			
			
			if not os.path.exists(output_subdir):
				os.makedirs(output_subdir)
	
			# Call ffmpeg with the appropriate arguments
			os.system('ffmpeg -i ' + path + ' ' + output_path)
			
			