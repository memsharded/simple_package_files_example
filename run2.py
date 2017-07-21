import os, shutil

# This run2 assumes the library has already been created with the other run.py script
# so hello_lib/bin and hello_lib/inc are already existing and populated with hello.lib
try:
    shutil.rmtree("pkg")
except:
    pass
os.makedirs("pkg") # prepare an empty folder, for clean pacakge
shutil.copytree("hello_lib/bin", "pkg/bin")
shutil.copytree("hello_lib/inc", "pkg/inc")


# Conan commands
os.system("conan export user/testing")
os.system("conan package_files Hello/0.1@user/testing --package_folder=pkg -f")
os.system("conan upload Hello/0.1@user/testing -r=artifactory --all")