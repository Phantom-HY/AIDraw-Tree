class Tree:
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
