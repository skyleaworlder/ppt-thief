import psutil
import time
import traceback
import sys
from pathlib import Path

from .GLOBAL import pc_disk_partitions

def smell(target_drive="E:\\", enable_target=False, detail_root=None):
    '''
    用来嗅探盘符情况的函数
    target_drive: 目标盘符
    enable_target: 表示是否有指定文件夹。False 表示没有
    detail_root: 在 enable_target 为 True 时才可指定，表示具体文件夹路径
    '''
    global pc_disk_partitions
    try:
        disk_partition_get = psutil.disk_partitions()
    except Exception as e:
        traceback.print_exc(e)
        sys.exit(-1)
    else:
        if len(disk_partition_get) != len(pc_disk_partitions):
            pc_disk_partitions = disk_partition_get
        drive_letters = [drive.device for drive in pc_disk_partitions]
        check_target = True if target_drive in drive_letters else False
        if enable_target:
            check_detail = Path(detail_root).is_dir()
        else:
            check_detail = None

        return {
            "success": True,
            "disk_part": pc_disk_partitions,
            "target_exist": check_target,
            "detail_exist": check_detail,
        }