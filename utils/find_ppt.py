import os
from pathlib import Path
import re
import traceback
import sys
from queue import Queue

o_path = os.getcwd()
sys.path.append(o_path)
from .GLOBAL import ppt_path, match_pattern, skip_pattern

def sepa_dir_file(files):
    '''
    传进来一堆路径，划分出它们是目录还是文件
    files: 文件路径的列表
    '''
    dir_lst = []
    file_lst = []
    for file in files:
        if Path(file).is_dir():
            dir_lst.append(file)
        elif Path(file).is_file():
            file_lst.append(file)
    return dir_lst, file_lst

def listdir_s(local_root):
    '''
    根据当前路径，列出下属所有文件/目录
    local_root: 当前路径
    '''
    all_sub_files = []
    try:
        all_sub_files = os.listdir(local_root)
        print("listdir_s:", all_sub_files)
    except Exception as e:
        all_sub_files = []
        traceback.print_exc(e)
        sys.exit(-1)

    return [str(local_root)+'\\'+file_path for file_path in all_sub_files]

def add_ppt_from_lst(file_paths):
    '''
    给定一个 file_paths，选择 ppt 加入到全局变量中
    file_paths: 文件路径候选列表
    '''
    for file in file_paths:
        if re.match(match_pattern, file):
            ppt_path.append(file)
        print(file)

def layer_trans(local_root, total_layer):
    '''
    层序遍历目录树
    '''
    local_layer = 0
    dir_paths_buf0 = [local_root]

    # 层序遍历，使用了两个 buffer 作刷新
    while local_layer != total_layer:
        file_paths = []
        dir_paths_buf1 = []

        '''
        遍历当前路径下的所有子目录
        获得并存入所有子目录中的文件/目录
        也就是说，一个 for 循环中获得下一“层”的所有目录和文件

        buffer0 存储当前目录下的所有子目录
        buffer1 存储当前目录下所有子目录的子目录
        '''
        for director in dir_paths_buf0:
            all_sub_file_paths = listdir_s(director)
            tmp_dir_paths, tmp_file_paths = sepa_dir_file(all_sub_file_paths)
            dir_paths_buf1 += tmp_dir_paths
            file_paths += tmp_file_paths
            print(file_paths, dir_paths_buf1, dir_paths_buf0)

        # 先将下一层的检测并添加
        add_ppt_from_lst(file_paths)
        dir_paths_buf0 = dir_paths_buf1
        local_layer = local_layer + 1
    return ppt_path

def find_ppt(begin_root, total_layer):
    layer_trans(begin_root, total_layer)
