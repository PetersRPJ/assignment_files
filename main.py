__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import zipfile
import shutil

def clean_cache():
    directory = 'cache'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)    
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors = False)
    os.makedirs(path)                       
    print("Directory '%s' created" %directory)                                       
    return

clean_cache()

def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
        return zip_ref

cache_zip("./data.zip", './cache')

def cached_files():
    path = os.path.abspath('./cache')
    files = []
    for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                if not file_path in files:
                    files.append(file_path)
    return files

def find_password(files_list):
    for a in files_list:  
        with open(a, 'r') as f:
            for line in f:
                if 'password' in line:
                    return line.strip()[10:]
                    
print (find_password(cached_files()))

