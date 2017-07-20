from conans import ConanFile


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"

    def package_info(self):
        self.cpp_info.includedirs = ["inc"]
        self.cpp_info.libdirs = ["bin"]
        self.cpp_info.libs = ["hello"]
