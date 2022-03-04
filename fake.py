from faker import Faker

import global_val_dev
import model
import solution_dev


def fake_data():
    n = 10000
    fake = Faker(locale='zh_CN')
    for i in range(n):
        name = fake.name()
        email = fake.email()
        tel = fake.phone_number()

        u = model.User(name, email, tel)
        nlink = model.LinkNode(u)
        ntree = model.TreeNode(u)

        r = solution_dev.array_add(global_val_dev.get_user_array(), u)
        global_val_dev.set_user_array(r)
        r = solution_dev.link_add(global_val_dev.get_user_link(), nlink)
        global_val_dev.set_user_link(r)
        r = solution_dev.tree_add(global_val_dev.get_user_tree(), ntree)
        global_val_dev.set_user_tree(r)

        print(name, email, tel)
