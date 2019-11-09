from conans import ConanFile

class Conan(ConanFile):
    name = "StackBlox"
    version = ""
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires.add("android_sdl2/0.1.0#db746d43b1b7e728db3b2d280aae273da3922e68")
        self.build_requires.add("cmake_utils/0.1.0#9efedba7676c460adbfbf3a98e4c51cea7d320db")

    def requirements(self):
        self.requires.add("gtest/1.10.0#ca07d9d05d12f3bbb091f095e30f7c54cd2920ee")
        self.requires.add("ssrobins_engine/0.2.0#012ac83390f32170f0438c909972c837931eb297")
