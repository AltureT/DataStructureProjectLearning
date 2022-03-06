# 数据结构项目化学习

## 学习目标

1. 通过查询、插入功能编写数组、链表、树的查找、新增操作代码
2. 通过日志系统学习队列结构
3. 通过邮箱规范验证学习正则表达式
4. 通过手机号码规范学习字符串处理
5. 代码不涉及数据库等外部模块，尽可能用python内置库实现功能

## 程序功能

#### 查询模块

1. 在数组、链表、树的三种数据中进行查询，观察消耗时间，分析三种算法结构查询时间效率问题
2. 结合代码观察树结构模型的插入位置

#### 新增模块

在数组、链表、树的三种数据中进行数据插入，观察消耗时间，分析三种算法结构插入时间效率问题

#### 虚拟数据生成模块

通过生成大量数据，分别进行查询、新增功能，对比大量数据下，三种数据结构在算法时间不同

#### 测试模块

在按要求完成代码后，通过运行[test.py](/test.py)文件检验自己的代码情况

## 使用方法

1. 环境包安装：在本项目文件路径下打开Terminal，运行如下代码：

```
pip install --no-index --find-links=DIR -r requirements.txt
```

2. 程序分成两种运行环境：开发者环境与生产环境。
    - **开发者环境**:已经写完代码，仅供运行参考以及数据生成后三种数据结构时间效率上的分析。
    - **生产环境**:用于学习，需要学习者自己完成[solution.py](/solution.py)文件代码，在写完后，运行[test.py](/test.py)文件，测试代码通过情况

> 环境切换为**生产环境**方法:将[main.py](/main.py)中的`config`修改成如下

```python
config = {'env': 'pro'}
```

> 环境切换为**开发者环境**方法:将[main.py](/main.py)中的`config`修改成如下

```python
config = {'env': 'dev'}
```

2. 在[solution.py](/solution.py)中，根据注释完成内容，按要求返回数据