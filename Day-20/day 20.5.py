print("10. os MODULE - Directory & File Operations")
import os
print("Current Directory:", os.getcwd())
folder_name = "DemoFolder"  # Create a folder if it doesn't exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created")
else:
    print(f"Folder '{folder_name}' already exists")
sub_folder = os.path.join(folder_name, "SubFolder")    # Create a subfolder
if not os.path.exists(sub_folder):
    os.mkdir(sub_folder)
    print("SubFolder created")
file_path = os.path.join(folder_name, "sample.txt")    # Create a file inside the folder
with open(file_path, "w") as f:
    f.write("Hello! This is a sample file.")
print("File created:", file_path)
print("Contents of DemoFolder:", os.listdir(folder_name))   # List contents of the folder
empty_file = os.path.join(folder_name, "empty.txt")    # Create an empty file
open(empty_file, "w").close()
print("Empty file created")
print("11. DELETING FILES AND FOLDERS")
if os.path.exists(empty_file):
    os.remove(empty_file)
    print("empty.txt deleted")
if os.path.exists(sub_folder):  # Delete empty subfolder
    os.rmdir(sub_folder)
    print("SubFolder deleted")
# To delete a folder with contents, use shutil
import shutil # shutil.rmtree("DemoFolder")   # Uncomment to delete entire folder with contents
print("Use shutil.rmtree() to delete non-empty folders")



