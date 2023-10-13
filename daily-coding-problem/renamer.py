from os import listdir, getcwd, rename
from os.path import isfile, join

files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f)) and f != "renamer.py"]

for file in files:
  if len(file) == 4:
    rename(file, "00" + file)
  elif len(file) == 5:
    rename(file, "0" + file)
