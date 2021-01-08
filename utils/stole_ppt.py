from pathlib import Path
import os
import shutil
import tarfile, zipfile

from ..GLOBAL import ppt_path, target_path

def copy_ppt():
    global target_path
    # create folder
    if not Path(target_path).is_dir():
        os.mkdir(target_path)

    for ppt in ppt_path:
        shutil.copy(ppt, target_path)

def tar_ppt(tar_path="C:\\ppt_tar"):
    tar = tarfile.open(tar_path, "w")
    ppt_new_path = os.listdir(target_path)
    for ppt in ppt_new_path:
        tar.add(ppt)
    tar.close()

def zip_ppt(src):
    # TODO: unfinished
    z = zipfile.ZipFile()