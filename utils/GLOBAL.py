# 磁盘分区，方便检测
pc_disk_partitions = []

# ppt 所在位置
ppt_path = []

# 筛选条件
match_pattern = '.+\.(ppt|pptx)$'

# 跳过条件
skip_pattern = '($RECYCLE)'

# 默认盘符
u_charactor = "E:\\"

# 查找间隔秒数
check_time_interval = 5

# 层序遍历层数
layer_num = 5

# 存储路径
target_path = "./out/output"

# 打包路径
tar_path = "./out/ppt_thief.tar"

# 压缩路径
zip_path = "./out/ppt_thief.tar.gz"