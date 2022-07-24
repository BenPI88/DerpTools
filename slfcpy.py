import os
files = []

for file in os.listdir(~/derptools-tmp/DerpTools):
  if file == "slfcpy.py":
    continue
  if os.path.isfile(file):
    files.append(file)
print(files)
print("Press enter to verify that copying these files is ok with you.")
input("")
print("Copying Files...")
i = 0
os.system("cd ~ && mkdir DerpTools")
while not i == len(files):
  os.system("cp " + str(files[i]) + " ~/DerpTools")
  i = i + 1
