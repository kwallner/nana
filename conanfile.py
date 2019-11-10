from conans import ConanFile, CMake

class NanaConan(ConanFile):
    name = "nana"
    version = "1.7.2"
    license = "Boost Software License"
    url = "http://nanapro.org"
    description = "Nana C++ Library designed to allow developers to easily create cross-platform GUI applications with modern C++11 style"
    author = "Karl Wallner <kwallner@mail.de>"
    generators = "cmake"
    settings = "os", "compiler", "arch", "build_type"
    scm = { "type": "git", "url": "auto", "revision": "auto" }
    options = { "shared": [True, False], "fPIC": [True, False] }
    default_options = { "shared": False, "fPIC": False }
    no_copy_source = True
    
    def build(self):
        cmake = CMake(self)
        cmake.definitions["NANA_CMAKE_INSTALL"] = True
        # Yet can not handle this
        cmake.definitions["NANA_STATIC_STDLIB"] = False
        # ... do not want to change defaults
        cmake.definitions["MSVC_USE_STATIC_RUNTIME"] = False
        # More options are available, see e.g. select_filesystem.cmake
        #cmake.definitions["NANA_CMAKE_NANA_FILESYSTEM_FORCE"] = True
        cmake.definitions["CMAKE_CONFIGURATION_TYPES"]= self.settings.build_type
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC or self.options.shared
        cmake.configure()
        cmake.build()
        cmake.install()

