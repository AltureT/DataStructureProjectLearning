# 数据结构项目化学习

## 学习目标

1. 通过查询、插入功能编写数组、链表、树的查找、新增操作代码
2. 通过日志系统学习队列结构
3. 通过邮箱规范验证学习正则表达式
4. 通过手机号码规范学习字符串处理
5. 代码不涉及数据库等外部模块，尽可能用python内置库实现功能

## 使用方法

1. 程序分成两种运行环境：开发者环境与生产环境。开发者环境已经写完代码，仅供运行参考。生产环境用于学习，代码完善。所以建议切换成生产环境

> 环境切换为**生产环境**方法:将main.py中的`config`修改成如下

```python
config = {'env': 'pro'}
```

> 环境切换为**开发者环境**方法:将[main.py](/main.py)中的`config`修改成如下

```python
config = {'env': 'dev'}
```

2. 在[solution.py](/solution.py)中，根据注释完成内容，按要求返回数据