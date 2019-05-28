import os
cwd = os.getcwd()

project_path = ""
flag = False

for dir in cwd.split("/")[1:]:
    project_path = f"{project_path}/{dir}"
    if dir == "source":
        flag = True
        break

if not flag:
    project_path = f"{project_path}/source/"

input_path = f"{project_path}/static/input.txt"
figure_path = f"{project_path}/static/figure.png"
requirements_path = f"{project_path}/static/requirements.txt"
testdata_path = f"{project_path}/static/testdata"
module_path = f"{project_path}/Modules"
