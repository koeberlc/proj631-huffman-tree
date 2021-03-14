class Node:
    """
    A node have a label, up to 2 children, a frequency and a value
    A leaf is related to one character
    """
    def __init__(self, label, frequence, left_child=None, right_child=None):
        self.label = label
        self.frequence = frequence
        self.left_child = left_child
        self.right_child = right_child
        self.value = None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_label(self):
        return self.label

    def get_frequence(self):
        return self.frequence

    def get_value(self):
        return self.value

    def get_list_prefixe(self, node="Error"):
        """
        Read the tree (related to a root) in a prefix order

        Attrs:
            node (Node): current node

        Returns:
            str: list of nodes in a tree in a prefix order
        """
        if(node == "Error"):
            node = self
        res = ""

        if (node not is None):
            res = node.get_label() +
            node.get_list_prefixe(node.get_left_child()) +
            node.get_list_prefixe(node.get_right_child())

        return res

    def is_leaf(self):
        """
        Detect if the node is a leaf

        Returns:
            boolean: if the node is a leaf
        """
        return (self.get_right_child() is None) and
        (self.get_right_child() is None)

    def get_all_node(self):
        """
        Return the list of all nodes under the current node

        Returns:
            list: list of node
        """
        list_node = [self]
        if(not self.is_leaf()):
            if(not self.get_right_child() is None):
                list_node += self.get_right_child().get_all_node()
            list_node += self.get_left_child().get_all_node()
        return list_node

    def get_all_leaf(self):
        """
        Return the list of all leaf under the current node

        Returns:
            list: list of node (only leaf)
        """
        list_leaf = []
        list_node = self.get_all_node()
        for n in list_node:
            if(n.is_leaf()):
                list_leaf.append(n)
        return list_leaf

    def get_path(self, node):
        """
        Get the path from the current node to the node passed as a parameter

        Attrs:
            node (Node): Searched node

        Returns:
            list: list related to the path from current node to searched node
        """
        path = []
        list_node = self.get_all_node()

        while self != node:
            for n in list_node:
                if(n.get_left_child() == node or n.get_right_child() == node):
                    path.append(node)
                    node = n

        path.append(self)
        path.reverse()

        return path
