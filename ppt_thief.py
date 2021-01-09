import os
import time
from pathlib import Path
import re

from utils import smell_u_disk, find_ppt, stole_ppt, GLOBAL

logo = '''
================================================================
    ++====++ ++====++ ========                 by skyleaworlder
    ||    || ||    ||    ||
    ||====++ ||====++    ||
    ||       ||          ||
    ||       ||                |   |       ----
                       ------- |---|  ---  |--- ----
                          |    |   |   |   |--- |---
                          |           ---       |
================================================================
'''

print(logo)

print("U 盘盘符 (e.g. 若为 E 盘，则输入 \"E\"，默认为 \"E\")")
while True:
    input_res = input("请输入老师 U 盘的盘符: ")
    u_charactor = input_res+":\\" if len(input_res) != 0 else "E:\\"

    print("盘符为:", u_charactor)
    input_res = input("请输入 Y 确认: ")
    if input_res == "Y":
        break
print("\n")


print("(查找间隔时间的单位为秒, 类型为整型，默认为 5)")
while True:
    input_res = input("请输入查找 U 盘的间隔时间: ")
    check_time = float(input_res) if len(input_res) != 0 else 5

    print("间隔时间为:", check_time)
    input_res = input("请输入 Y 确认: ")
    if input_res == "Y":
        break
print("\n")


print("如果你对老师的 U 盘十分了解，或者明确地知道目标 ppt 的位置，请在下方输入")
print("e.g. 如果目标 ppt 在 \"E:\这是ppt\第一节课\" 下，那么请输入 \"这是ppt\第一节课\"")
print("     如果你不清楚，只是想全盘扫描，那请直接摁回车")
while True:
    detail_root = input("请输入目标 ppt 于 U 盘的位置: ")
    print("你的输入为:", detail_root)
    input_res = input("请输入 Y 确认: ")
    if input_res == "Y":
        break
print("\n")

root = Path(u_charactor+detail_root)
print("你想要查找的路径为:", root, "\n")


print("本程序使用层序遍历方法，因此需要给出遍历的层数，层数默认为 5。")
print("ppt 藏匿过深可能会导致程序效果欠佳。")
while True:
    input_res = input("请输入层序遍历层数: ")
    total_layer = int(input_res) if len(input_res) != 0 else 5
    print("输入的层数为:", total_layer)
    input_res = input("请输入 Y 确认: ")
    if input_res == "Y":
        break
print('\n')


print("ppt 的输出路径，默认为 \"./out/output\"")
print("你还可以输出到其他文件夹下，e.g. \"D:\\ppt_output\"")
print("如果指定的文件夹不存在，我会为你创建一个")
print("warning: 不建议将目标路径选为 C 盘，操作不当时可能不具备权限")
while True:
    input_res = input("请输入 ppt 的输出路径: ")
    output_path = input_res if len(input_res) != 0 else "./out/output"
    print("输出路径为:", output_path)
    input_res = input("请输入 Y 确认: ")
    if input_res == "Y":
        GLOBAL.target_path = output_path
        break
print("\n")


while True:
    is_tar = input("请问是否打包？ 是(Y)，否(N):")
    if is_tar == "Y":
        print("请输入打包文件名与所在路径，默认为 \"./out/ppt_thief.tar\"")
        print("你还可以输出到其他文件夹下，e.g. \"D:\\ppt_output\\ppt_thief.tar\"")
        input_res = input("打包文件名路径为: ")
        tar_path = input_res if len(input_res) != 0 else "./out/ppt_thief.tar"
        GLOBAL.tar_path = tar_path
        break
    elif is_tar == "N":
        tar_path = ""
        GLOBAL.tar_path = tar_path
        break




while True:
    enable_target = (len(detail_root) != 0)
    detail = detail_root if enable_target else None
    smell_res = smell_u_disk.smell(u_charactor, enable_target, detail)

    if smell_res["target_exist"]:
        find_ppt.layer_trans(root, total_layer)
        stole_ppt.copy_ppt()
        if is_tar:
            stole_ppt.tar_ppt()
        break
    else:
        time.sleep(int(float(check_time)))
        print("[PPT-THIEF]: you're waiting your rabbits under the TREE.")
