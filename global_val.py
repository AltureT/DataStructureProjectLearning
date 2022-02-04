# -*- coding: utf-8 -*-
import model


def _init():
    global _global_user_array
    global _global_user_link
    global _global_user_tree
    global _global_log_queue

    _global_user_array = []
    _global_user_link = model.LinkNode(None)
    _global_user_tree = model.TreeNode(None)

    _global_log_queue = []


def get_user_array():
    try:
        return _global_user_array
    except:
        print('global未初始化')


def get_user_link():
    try:
        return _global_user_link
    except:
        print('global未初始化')


def get_user_tree():
    try:
        return _global_user_tree
    except:
        print('global未初始化')


def get_log_queue():
    try:
        return _global_log_queue
    except:
        print('global未初始化')
