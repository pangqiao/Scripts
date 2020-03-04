#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os

class DirUnzip(object):
	#the input is directory, unzip all the zip files recursively!
	supportList = ['.zip', '.7z', '.gz', '.tar','.xz','.bz2', '.tbz2', '.iso']

	def __init__(self):
		self.path = os.getcwd()
		
	def run(self):
		self.UnzipRecursively(self.path)
		
		#delelte empty folders, 7z have bugs, if I use e to 
		#extract,there are some empty folders...
		for (root, dirs, files) in os.walk(self.path):
			for dir in dirs:
				fullpath = os.path.join(root, dir)
				nums = os.listdir(fullpath)
				if len(nums) == 0:
					os.rmdir(fullpath)

	def UnzipRecursively(self, dir):
		prev_dir = os.getcwd()

		os.chdir(dir)
		for root, subdirs, files in os.walk("."):
			#if there are folders in the zipped file.
			for dir in subdirs:
				#substitue the space
				if dir.find(" ") != -1:
					newdir = dir.replace(' ', '_')
					cmd = "move " + "\"" + dir + "\"" + " " + newdir

					os.system(cmd)
					
					self.UnzipRecursively(newdir)
					
			for file in files:
				name, ext = os.path.splitext(file)
				if ext in self.supportList and not os.path.exists(os.path.join(root, name)):
					self.UnzipFile(root, file)

		os.chdir(prev_dir)

	def UnzipFile(self, root, file):
		# uncompress all content into ONE folder
		prev_dir = os.getcwd()
		os.chdir(root)

		#strip the space of the file name begin.
		dir = os.getcwd()
		filenospace = file.replace(' ', '_')
		#strip the space of the file name end.
		renameok = os.rename(os.path.join(dir, file) , os.path.join(dir, filenospace))
		name, ext = os.path.splitext(filenospace)
	
		command = "\"C:\\Program Files\\7-Zip\\7z.exe\"" + \
			" -pjunk x  -y -o\"" + name +"\" "+ "\"" + filenospace+ "\""  + " > NUL"
			
		print ("unzipping file ... ... %s"%filenospace)
		os.system("\""+command+"\"")

		if os.path.isdir(name):
			self.UnzipRecursively(name)
		else:
			pass
			
		os.chdir(prev_dir)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == "__main__":
	zip = DirUnzip()
	zip.run()
			
	
	
