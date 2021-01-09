import psutil
import time
import traceback
import sys

from .GLOBAL import pc_disk_partitions

def smell(target_drive="E:\\", enable_target=False):
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
        check_target = True if target_drive in drive_letters and enable_target else False
        return {
            "success": True,
            "disk_part": pc_disk_partitions,
            "target_exist": check_target
        }