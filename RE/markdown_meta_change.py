import os
filedir = r"C:\Users\hcwang\Dropbox\obsidian\化合物\group\guideline"
files = os.listdir(filedir)
files = [file for file in files if file.endswith("md")]
for file in files:
    filename = f"{filedir}/{file}"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content.replace("tags", "subtype"))
