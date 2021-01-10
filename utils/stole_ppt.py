from pathlib import Path
import os
import shutil
import tarfile, zipfile, gzip

from .GLOBAL import ppt_path, target_path, tar_path, zip_path

def copy_ppt(ppt_path=ppt_path, target_path=target_path):
    # create folder
    if not Path(target_path).is_dir():
        print("[PPT-THIEF]: Create New Folder!")
        os.mkdir(target_path)

    for ppt in ppt_path:
        shutil.copy(ppt, target_path)
    return target_path

def tar_ppt(ppt_path=target_path, tar_file_path=tar_path):
    tar = tarfile.open(tar_file_path, "w")
    ppt_new_path = os.listdir(ppt_path)
    print("[PPT-THIEF]: Begin to tar.")
    for ppt in ppt_new_path:
        tar.add(ppt_path+'\\'+ppt)
    tar.close()
    return tar_file_path

def zip_ppt(ziped_files, zip_file_path=zip_path, choice="gz"):
    assert (type(ziped_files) is list and len(ziped_files) == 1) or (type(ziped_files) is str)
    if choice == "gz":
        with open(ziped_files, "rb") as f_in:
            with gzip.open(zip_file_path, "wb") as f_out:
                print("[PPT-THIEF]: Begin to zip.")
                shutil.copyfileobj(f_in, f_out)
    elif choice == "zip":
        z = zipfile.ZipFile(zip_file_path, "w")
        for file in ziped_files:
            z.write(file)
        z.close()
    return zip_file_path