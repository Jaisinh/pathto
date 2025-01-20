
#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def find_files_by_name(name, start_dir="/"):
   matching_items = []
   skip_dirs = {'/proc', '/sys', '/dev', '/tmp', '/var/log', '/var/cache', '/private/var'}
   
   try:
       for root, dirs, files in os.walk(start_dir, topdown=True):
           dirs[:] = [d for d in dirs if not d.startswith('.') and 
                     not any(skip in os.path.join(root, d) for skip in skip_dirs)]
           
           for dir_name in dirs:
               if name.lower() in dir_name.lower():
                   full_path = os.path.join(root, dir_name)
                   matching_items.append(full_path)
           
           for file_name in files:
               if name.lower() in file_name.lower():
                   full_path = os.path.join(root, file_name)
                   matching_items.append(full_path)
                   
   except PermissionError:
       pass
   except Exception as e:
       print(f"Error accessing some paths: {e}")
   
   return matching_items

def main():
   if len(sys.argv) < 2:
       print("Usage: pathto <name>")
       sys.exit(1)
   
   name = " ".join(sys.argv[1:])
   print(f"Searching for files or folders named '{name}'...")
   print("(This may take a while as it searches all directories...)")
   
   matching_items = find_files_by_name(name, "/")
   
   if matching_items:
       print("\nFound the following matches:")
       for item in matching_items:
           try:
               item_type = "Directory" if os.path.isdir(item) else "File"
               print(f"{item_type}: {item}")
           except Exception:
               continue
   else:
       print("No items found with the specified name.")

if __name__ == "__main__":
   main()




