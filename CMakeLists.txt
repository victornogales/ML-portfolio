# Set the minimum required version of CMake to be 3.10
cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(libreg VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add MathFunctions to this project
add_subdirectory(myMath)

# add the executable
add_executable(libreg main.cpp)

# Link the library to our executable
target_link_libraries(libreg PUBLIC myMath)

# Add MathFunctions to Tutorial's target_include_directories()
target_include_directories(libreg PUBLIC
                          "${PROJECT_SOURCE_DIR}/myMath"
                          )

