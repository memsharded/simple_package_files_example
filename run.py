import os, shutil

# Creating the hello pre-built binary, in user space, assuming they match conan default settings
# THIS IS NOT CONAN RELATED, JUST A MEAN TO GET A PRE-BUILT BINARY IN USER SPACE
try:
    shutil.rmtree("hello_lib/build")
    shutil.rmtree("hello_lib/bin")
except:
    pass
os.system('cd hello_lib && mkdir build && cd build && '
          'cmake .. -G "Visual Studio 14 Win64" && '
          'cmake --build . --config Release')


os.system("conan export user/testing")
os.system("conan package_files Hello/0.1@user/testing --package_folder=hello_lib -f")
os.system("conan upload Hello/0.1@user/testing -r=artifactory --all")