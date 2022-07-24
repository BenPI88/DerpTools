files = []

for file in os.listdir():
  if file == "slfcpy.py":
    continue
  if os.path.isfile(file):
    files.append(file)
print(files)
