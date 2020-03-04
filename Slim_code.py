
import os

Extlists = [".c",".config",".cpp", ".cmake", ".h", ".hpp", ".in", ".inc", ".mk", ".m", ".s", ".py",".cc","asm"]
FileMax = 1024*1024*1.2

try:
	RootDir = os.getcwd()
	for (root, dirs, files) in os.walk(RootDir):
		for filename in files:
			filename = os.path.join(root,filename)
			(shotname,extension) = os.path.splitext(filename); 
			size = os.path.getsize(filename)
			#print (size)
			if not extension in Extlists:
				os.remove(filename)
			elif size > FileMax:
				os.remove(filename)

except PermissionError as err:
	print('PermissionError:', err)