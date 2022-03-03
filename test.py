import unittest

import global_val_dev as global_val
import model
import solution_dev as solution


class MyTestCase(unittest.TestCase):
    def test_globalval(self):
        global_val._init()
        global_val.set_user_array([0, 1, 2])
        t = global_val.get_user_array()
        self.assertTrue(t == [0, 1, 2], '全局变量数组类型修改获取不通过')

        global_val.set_user_array([0, 1, 2])
        t = global_val.get_user_array()
        self.assertTrue(t == [0, 1, 2], '全局变量数组类型修改获取不通过')

        n1 = model.LinkNode('Alice')
        n2 = model.LinkNode('Bob')
        n3 = model.LinkNode('Tom')
        n1.next = n2
        n2.next = n3
        global_val.set_user_link(n1)
        r = global_val.get_user_link()
        n = n1
        while r:
            self.assertTrue(r.val == n.val, '全局变量链表类型修改获取不通过')
            r = r.next
            n = n.next

        n1 = model.TreeNode('Bob')
        n2 = model.TreeNode('Alice')
        n3 = model.TreeNode('Tom')
        n1.left = n2
        n1.right = n3
        global_val.set_user_tree(n1)
        r = global_val.get_user_tree()
        n = n1
        self.assertTrue(n.val == r.val, '全局变量树类型修改获取不通过')
        self.assertTrue(n.left.val == r.left.val, '全局变量树类型修改获取不通过')
        self.assertTrue(n.right.val == r.right.val, '全局变量树类型修改获取不通过')

    def test_find_array(self):
        a = model.User('Alice')
        b = model.User('Bob')
        c = model.User('Tom')
        l = []
        self.assertFalse(solution.array_find(l, 'Tom'), '列表为空时，查询失败')

        l = [a, b, c]
        self.assertTrue(solution.array_find(l, 'Jim') is None, '查询数组中不存在的用户失败')
        self.assertTrue(solution.array_find(l, 'Bob') == b, '未正确返回查询用户信息')

    def test_find_link(self):
        a = model.User('Alice')
        b = model.User('Bob')
        c = model.User('Tom')
        n1 = model.LinkNode(a)
        n2 = model.LinkNode(b)
        n3 = model.LinkNode(c)

        n1.next = n2
        n2.next = n3

        self.assertTrue(solution.link_find(None, 'Tom') is None, '当链表为空时，查找失败')
        self.assertTrue(solution.link_find(n1, 'Jim') is None, '查询链表中不存在的用户失败')
        self.assertTrue(solution.link_find(n1, 'Alice') == a, '查询链表中头节点用户失败')
        self.assertTrue(solution.link_find(n1, 'Bob') == b, '查询链表中中间节点用户失败')
        self.assertTrue(solution.link_find(n1, 'Tom') == c, '查询链表中尾节点用户失败')

    def test_find_tree(self):
        a = model.User('Alice')
        b = model.User('Bob')
        c = model.User('Tom')
        n1 = model.TreeNode(a)
        n2 = model.TreeNode(b)
        n3 = model.TreeNode(c)
        n1.right = n2
        n2.right = n3
        self.assertTrue(solution.tree_find(None, 'Tom') is None, '树为None时，查询失败')
        self.assertTrue(solution.tree_find(n1, 'Alice') == a, '树当前节点查询失败')
        self.assertTrue(solution.tree_find(n1, 'Bob') == b, '树右节点查询失败')
        self.assertTrue(solution.tree_find(n1, 'Tom') == c, '树右节点查询失败')

        n2.left = n1
        n2.right = n3
        self.assertTrue(solution.tree_find(None, 'Tom') is None, '树为None时，查询失败')
        self.assertTrue(solution.tree_find(n2, 'Alice') == a, '树左节点查询失败')
        self.assertTrue(solution.tree_find(n2, 'Bob') == b, '树当前节点查询失败')
        self.assertTrue(solution.tree_find(n2, 'Tom') == c, '树右节点查询失败')

        n3.left = n2
        n2.left = n1
        self.assertTrue(solution.tree_find(None, 'Tom') is None, '树为None时，查询失败')
        self.assertTrue(solution.tree_find(n3, 'Alice') == a, '树左节点查询失败')
        self.assertTrue(solution.tree_find(n3, 'Bob') == b, '树左节点查询失败')
        self.assertTrue(solution.tree_find(n3, 'Tom') == c, '树当前节点查询失败')

    def test_array_add(self):
        a = model.User('Alice')
        b = model.User('Bob')
        c = model.User('Tom')
        self.assertTrue(solution.array_add([], a) == [a], '数组为空时插入用户失败')
        self.assertTrue(solution.array_add([b], a) == [a, b], '插入数组头部失败')
        self.assertTrue(solution.array_add([a, c], b) == [a, b, c], '插入数组中间位置失败')
        self.assertTrue(solution.array_add([a, b], c) == [a, b, c], '插入数组尾部失败')

    def test_link_add(self):
        a = model.User('Alice')
        b = model.User('Bob')
        c = model.User('Tom')
        n1 = model.LinkNode(a)
        n2 = model.LinkNode(b)
        n3 = model.LinkNode(c)

        self.assertTrue(solution.link_add(None, n1) == n1, '链表为空时，插入节点失败')
        n = solution.link_add(n1, n2)
        self.assertTrue(n == n1, '链表插入后返回新的根节点失败')
        self.assertTrue(n.next == n2, '链表插入尾节点失败')
        n = solution.link_add(n2, n1)
        self.assertTrue(n == n1, '链表插入新的头节点失败')
        self.assertTrue(n.next == n2, '链表插入新的头节点时，丢失后续节点')

        n1.next = n3
        n = solution.link_add(n1, n2)
        self.assertTrue(n == n1, '链表插入后返回新的根节点失败')
        self.assertTrue(n.next == n2, '链表插入中间节点失败')
        self.assertTrue(n.next.next == n3, '链表插入中间节点时，丢失后续节点')

    def test_tree_add(self):
        a = model.User('Alice')
        b = model.User('Crystal')
        c = model.User('Tom')
        d = model.User('Jim')
        e = model.User('Zara')
        n1 = model.TreeNode(a)
        n2 = model.TreeNode(b)
        n3 = model.TreeNode(c)
        n4 = model.TreeNode(d)
        n5 = model.TreeNode(e)

        self.assertTrue(solution.tree_add(None, n1) == n1)

        n4.left = n2
        n2.left = n1
        n2.right = n3
        n4.right = n5
        self.assertTrue(solution.tree_add(None, n1) == n1)


if __name__ == '__main__':
    unittest.main()
