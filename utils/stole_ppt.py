from pathlib import Path
import os
import shutil
import tarfile, zipfile

from .GLOBAL import ppt_path, target_path, tar_path, zip_path

def copy_ppt(ppt_path=ppt_path, target_path=target_path):
    # create folder
    if not Path(target_path).is_dir():
        print("create new folder")
        os.mkdir(target_path)

    for ppt in ppt_path:
        shutil.copy(ppt, target_path)

def tar_ppt(ppt_path=target_path, tar_file_path=tar_path):
    tar = tarfile.open(tar_file_path, "w")
    ppt_new_path = os.listdir(ppt_path)
    for ppt in ppt_new_path:
        tar.add(ppt_path+'\\'+ppt)
    tar.close()

def zip_ppt(ziped_files, zip_file_path=zip_path):
    z = zipfile.ZipFile(zip_file_path, "w")
    for file in ziped_files:
        z.write(file)
    z.close()