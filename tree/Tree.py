class NodeTree:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class Tree:
    def __init__(self, root, name):
        self.root = root
        self.node = [NodeTree(root, name)]

    def add_node(self, id, name):
        self.node.append(NodeTree(id, name))

    def get_node(self, id):  # 获取指定节点信息
        for node in self.node:
            if node.get_id() == id:
                return node
        return None

    def get_root(self):
        return self.root

    def get_node_list(self):
        return self.node
