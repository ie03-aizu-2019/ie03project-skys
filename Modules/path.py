import os
cwd = os.getcwd()

project_path = ""

for dir in cwd.split("/")[1:]:
    project_path = f"{project_path}/{dir}"
    if dir == "Modules":
        break

input_path = f"{project_path}/static/input.txt"
figure_path = f"{project_path}/static/figure.png"
testdata_path = f"{project_path}/static/testdata"
module_path = f"{project_path}/Modules"
