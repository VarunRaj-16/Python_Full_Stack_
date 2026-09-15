print("5. DIRECTORY OPERATIONS")
import os
import shutil
main_folder = "MyFolder"     # Create main folder
if not os.path.exists(main_folder):
    os.mkdir(main_folder)
    print("Main folder created")
sub_folder = os.path.join(main_folder, "SubFolder")      # Create subfolder
if not os.path.exists(sub_folder):
    os.mkdir(sub_folder)
    print("Subfolder created")
file_path = os.path.join(main_folder, "myfile.txt")     # Create a file inside folder
with open(file_path, "w") as f:
    f.write("This is a sample file.")
print("File created inside folder")
print("Contents of MyFolder:", os.listdir(main_folder))          # List contents
if os.path.exists(file_path):               # File information
    print("File size:", os.path.getsize(file_path), "bytes")
    print("Absolute path:", os.path.abspath(file_path))
