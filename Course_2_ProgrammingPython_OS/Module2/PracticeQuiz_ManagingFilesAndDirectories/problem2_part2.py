import os
print(os.getcwd())
def new_directory(directory, filename):
    if os.path.isdir(directory) == False:
        os.makesdir(directory)
    else:
        os.chdir(directory)
        print(os.getcwd())
        with open(filename, "w") as file:
            pass
    
    return os.listdir()

print(new_directory("PythonPrograms", "script.py"))
