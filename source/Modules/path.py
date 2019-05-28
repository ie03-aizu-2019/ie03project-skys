import os
cwd = os.getcwd()

project_path = ""

for dir in cwd.split("/")[1:]:
    if dir == "Modules":
        break
    project_path = f"{project_path}/{dir}"

input_path = f"{project_path}/static/input.txt"
figure_path = f"{project_path}/static/figure.png"
testdata_path = f"{project_path}/static/testdata"
module_path = f"{project_path}/Modules"
