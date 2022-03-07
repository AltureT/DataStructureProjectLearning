# -*- coding: utf-8 -*-
import model

_global_user_array = []
_global_user_link = None
_global_user_tree = None
_global_log_queue = []
_global_runtime = ''
_global_graph = None
_global_pos = None
_global_ax = None


def _init():
    global _global_user_array
    global _global_user_link
    global _global_user_tree
    global _global_log_queue
    global _global_user_obj
    global _global_runtime
    global _global_graph
    global _global_pos
    global _global_ax

    _global_user_obj = None
    _global_user_array = []
    _global_user_link = None
    _global_user_tree = None
    _global_log_queue = []
    _global_runtime = ''
    _global_graph = None
    _global_pos = None
    _global_ax = None


def init():
    _init()


def get_graph():
    try:
        return _global_graph
    except NameError as e:
        print(e, 'global未初始化')


def get_pos():
    try:
        return _global_pos
    except NameError as e:
        print(e, 'global未初始化')


def get_ax():
    try:
        return _global_ax
    except NameError as e:
        print(e, 'global未初始化')


def get_runtime():
    try:
        return _global_runtime
    except NameError as e:
        print(e, 'global未初始化')


def get_user_array():
    try:
        return _global_user_array
    except NameError as e:
        print(e, 'global未初始化')


def get_user_link():
    try:
        return _global_user_link
    except NameError as e:
        print(e, 'global未初始化')


def get_user_tree():
    try:
        return _global_user_tree
    except NameError as e:
        print(e, 'global未初始化')


def get_log_queue():
    try:
        return _global_log_queue
    except NameError as e:
        print(e, 'global未初始化')


def set_user_array(array: list):
    global _global_user_array
    try:
        _global_user_array = array
    except NameError as e:
        print(e, 'global未初始化')


def set_user_link(root: model.LinkNode):
    global _global_user_link
    try:
        _global_user_link = root
    except NameError as e:
        print(e, 'global未初始化')


def set_user_tree(root: model.TreeNode):
    global _global_user_tree
    try:
        _global_user_tree = root
    except NameError as e:
        print(e, 'global未初始化')


def set_log_queue(que):
    global _global_log_queue
    try:
        _global_log_queue = que
    except NameError as e:
        print(e, 'global未初始化')


def set_runtime(time: str):
    global _global_runtime
    try:
        _global_runtime = time
    except NameError as e:
        print(e, 'global未初始化')


def set_graph(graph):
    global _global_graph
    try:
        _global_graph = graph
    except NameError as e:
        print(e, 'global未初始化')


def set_pos(pos):
    global _global_pos
    try:
        _global_pos = pos
    except NameError as e:
        print(e, 'global未初始化')


def set_ax(ax):
    global _global_ax
    try:
        _global_ax = ax
    except NameError as e:
        print(e, 'global未初始化')
