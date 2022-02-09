# -*- coding: utf-8 -*-
import model


def _init():
    global _global_user_array
    global _global_user_link
    global _global_user_tree
    global _global_log_queue
    global _global_user_obj

    _global_user_obj = model.User(name='Bob', email='Bob@example.com', tel='123456789')
    _global_user_array = []
    _global_user_link = model.LinkNode(model.User(name='Bob', email='Bob@example.com', tel='123456789'))
    _global_user_tree = model.TreeNode(model.User(name='Bob', email='Bob@example.com', tel='123456789'))

    _global_log_queue = []


def init():
    _init()


def get_user_info():
    try:
        return _global_user_obj
    except:
        print('global未初始化')


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
