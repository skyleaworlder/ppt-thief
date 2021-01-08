
import sys, os

o_path = os.getcwd()
sys.path.append(o_path)

from utils import find_ppt

if __name__ == "__main__":
    print(find_ppt.layer_trans(r"D:\Projects\Gitexercise\TJCS-Course\100580_人工智能原理与技术", 4))
