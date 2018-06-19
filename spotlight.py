from pathlib import Path
import os
import shutil

user = str(Path.home())
spotlight = "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
path = user + spotlight
os.chdir(path)
print("Working directory has been set to: " + os.getcwd())

newdir = user + "\\Desktop\\Spotlight"
os.mkdir(newdir)

for files in os.listdir():
	if os.path.isfile(files):
		shutil.copy(files, newdir)

os.chdir(newdir)
os.system('ren * *.jpg')

for image in os.listdir():
	if os.stat(image).st_size / 1024 < 350:
		os.remove(image)
