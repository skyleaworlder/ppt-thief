# run on .
import sys, os
import unittest
from ddt import ddt, data, unpack

o_path = os.getcwd()
sys.path.append(o_path)

from utils import find_ppt, stole_ppt, smell_u_disk

@ddt
class Test(unittest.TestCase):

    layer_trans_data = (
        { "local_root": r"./test/assets/test_slides/", "total_layer": 4 },
        { "local_root": r"./test/assets/test_slides/", "total_layer": 3 },
    )

    copy_ppt_data = (
        { "target_path": "./test/assets/test_slides_output", "ppt_path": ['./test/assets/test_slides/\\1_1-搜索问题导入及形式化.pptx', './test/assets/test_slides/\\1_4-对抗搜索.pptx', './test/assets/test_slides/\\2019 B树.ppt', './test/assets/test_slides/\\2_chapt_07-逻辑智能体--微课.ppt', './test/assets/test_slides/\\数组和广义表20190923.ppt', './test/assets/test_slides/\\树和二叉树20190925.ppt', './test/assets/test_slides/\\线性表201909.ppt', './test/assets/test_slides/\\1.1\\1 Introduction - mdq - 20190820.pptx', './test/assets/test_slides/\\1.2\\3.3-有信息搜索.pptx', './test/assets/test_slides/\\1.3\\2.2 智能化智能体-理性的概念.pptx', './test/assets/test_slides/\\1.4\\栈和队列201909.ppt', './test/assets/test_slides/\\1.1\\2.2\\2.1 智能化智能体-智能体与环境.pptx', './test/assets/test_slides/\\1.1\\2.2\\2.3 智能化智能体-环境的本质.pptx', './test/assets/test_slides/\\1.3\\2.1\\第六章 不确定性的量化_微课PPT - 副本.pptx', './test/assets/test_slides/\\1.3\\2.1\\第六章 不确定性的量化_微课PPT.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-决策树学习.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-多层前馈网络.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-学习概述.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-感知器.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-神经网络－神经元和神经网络结构.pptx', './test/assets/test_slides/\\1.4\\2.2\\图20191031.ppt', './test/assets/test_slides/\\1.4\\2.2\\3.1\\第七章 概率推理_微课PPT.pptx', './test/assets/test_slides/\\1.4\\2.2\\3.1\\绪论201909.ppt'] },
    )

    tar_ppt_data = (
        { "ppt_path": "./test/assets/test_slides_output", "tar_file_path": "./test/assets/test_tar/ppt.tar" },
    )

    zip_ppt_data = (
        { "zip_file_path": "./out/ppt_thief.tar.gz", "ziped_files": "./out/ppt_thief.tar" },
        #{ "zip_file_path": "./test/assets/test_zip/ppt.zip", "ziped_files": ['./test/assets/test_slides/\\1_1-搜索问题导入及形式化.pptx', './test/assets/test_slides/\\1_4-对抗搜索.pptx', './test/assets/test_slides/\\2019 B树.ppt', './test/assets/test_slides/\\2_chapt_07-逻辑智能体--微课.ppt', './test/assets/test_slides/\\数组和广义表20190923.ppt', './test/assets/test_slides/\\树和二叉树20190925.ppt', './test/assets/test_slides/\\线性表201909.ppt', './test/assets/test_slides/\\1.1\\1 Introduction - mdq - 20190820.pptx', './test/assets/test_slides/\\1.2\\3.3-有信息搜索.pptx', './test/assets/test_slides/\\1.3\\2.2 智能化智能体-理性的概念.pptx', './test/assets/test_slides/\\1.4\\栈和队列201909.ppt', './test/assets/test_slides/\\1.1\\2.2\\2.1 智能化智能体-智能体与环境.pptx', './test/assets/test_slides/\\1.1\\2.2\\2.3 智能化智能体-环境的本质.pptx', './test/assets/test_slides/\\1.3\\2.1\\第六章 不确定性的量化_微课PPT - 副本.pptx', './test/assets/test_slides/\\1.3\\2.1\\第六章 不确定性的量化_微课PPT.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-决策树学习.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-多层前馈网络.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-学习概述.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-感知器.pptx', './test/assets/test_slides/\\1.3\\2.2\\第8章 学习-神经网络－神经元和神经网络结构.pptx', './test/assets/test_slides/\\1.4\\2.2\\图20191031.ppt', './test/assets/test_slides/\\1.4\\2.2\\3.1\\第七章 概率推理_微课PPT.pptx', './test/assets/test_slides/\\1.4\\2.2\\3.1\\绪论201909.ppt'] },
        #{ "zip_file_path": "./test/assets/test_zip/ppt1.zip", "ziped_files": ['./test/assets/test_tar/ppt.tar'] },
    )

    @unittest.skip
    @data(layer_trans_data)
    @unpack
    def test_layer_trans(self, *args, **kwargs):
        for data in args:
            local_root, total_layer = data["local_root"], data["total_layer"]
            print(local_root, total_layer)
            print(find_ppt.layer_trans(local_root, total_layer))

    @unittest.skip
    @data(copy_ppt_data)
    @unpack
    def test_copy_ppt(self, *args, **kwargs):
        for data in args:
            target_path, ppt_path = data["target_path"], data["ppt_path"]
            stole_ppt.copy_ppt(ppt_path, target_path)

    @unittest.skip
    @data(tar_ppt_data)
    @unpack
    def test_tar_ppt(self, *args, **kwargs):
        for data in args:
            ppt_path, tar_file_path = data["ppt_path"], data["tar_file_path"]
            stole_ppt.tar_ppt(ppt_path, tar_file_path)

    #@unittest.skip
    @data(zip_ppt_data)
    @unpack
    def test_zip_ppt(self, *args, **kwargs):
        for data in args:
            zip_file_path, ziped_files = data["zip_file_path"], data["ziped_files"]
            stole_ppt.zip_ppt(ziped_files, zip_file_path)


if __name__ == "__main__":
    '''runner = unittest.TextTestRunner()
    runner.run()'''

    unittest.main()