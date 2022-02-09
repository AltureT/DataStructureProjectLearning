# -*- coding: utf-8 -*-
import global_val
import solution

class Search:
    def __init__(self, name):
        self.name = name

    def from_array(self):
        solution.array_find(self.name)
        return

    def from_link(self):
        pos = 3
        return pos

    def from_tree(self):
        pos = 3
        return pos


class Add:
    def __init__(self, name, email, tel):
        self.name = name
        self.email = email
        self.tel = tel

    def add_to_array(self):
        pos = 3
        return pos

    def add_to_link(self):
        pos = 3
        return pos

    def add_to_tree(self):
        pos = 3
        return pos
