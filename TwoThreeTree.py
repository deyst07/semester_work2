from print_utils import print_tree


class Node:

    def __init__(self):
        self.keys = []
        self.children = []
        self.parent: Node | None = None
        self.iterations = 0

    def is_leaf(self):

        return len(self.children) == 0


class TwoThreeTree:

    def __init__(self):
        self.root = None

    def search(self, value):

        self.iterations = 0

        return self._search(self.root, value)

    def _search(self, node, value):

        self.iterations += 1

        if node is None:
            
            return False
        if value in node.keys:
            
            return True
        if node.is_leaf():
            
            return False

        if len(node.keys) == 1:
            if value < node.keys[0]:
                
                return self._search(node.children[0], value)
            else:
                
                return self._search(node.children[1], value)
        
        else:
            if value < node.keys[0]:
                
                return self._search(node.children[0], value)
            elif value < node.keys[1]:
                
                return self._search(node.children[1], value)
            else:
                
                return self._search(node.children[2], value)
        
    def _find_leaf(self, node, value):

        self.iterations += 1

        if node.is_leaf():
            
            return node

        if len(node.keys) == 1:
            if value < node.keys[0]:
                
                return self._find_leaf(node.children[0], value)
            else:
                
                return self._find_leaf(node.children[1], value)

        else:
            if value < node.keys[0]:
                
                return self._find_leaf(node.children[0], value)
            elif value < node.keys[1]:
                
                return self._find_leaf(node.children[1], value)
            else:
                
                return self._find_leaf(node.children[2], value)
            
    def insert(self, value):

        self.iterations = 0

        if self.root is None:
            self.root = Node()
            self.root.keys.append(value)
            self.iterations += 1
            
            return

        leaf = self._find_leaf(self.root, value)
        leaf.keys.append(value)
        self.iterations += 1
        leaf.keys.sort()
        self.iterations += 1

        if len(leaf.keys) > 2:
            self._split(leaf)

    def _split(self, node):

        self.iterations += 1

        middle_key = node.keys[1]
        left_node = Node()
        left_node.keys = [node.keys[0]]
        right_node = Node()
        right_node.keys = [node.keys[2]]

        if node.children:
            left_node.children = node.children[:2]
            right_node.children = node.children[2:]

            for child in left_node.children:
                child.parent = left_node

            for child in right_node.children:
                child.parent = right_node

        if node == self.root:
            new_root = Node()

            new_root.keys = [middle_key]
            new_root.children = [left_node, right_node]

            left_node.parent = new_root
            right_node.parent = new_root

            self.root = new_root

            return

        parent = node.parent
        parent.keys.append(middle_key)
        parent.keys.sort()
        parent.children.remove(node)
        insert_index = 0

        while (insert_index < len(parent.keys)
            and middle_key > parent.keys[insert_index]):
            insert_index += 1

        parent.children.insert(insert_index, left_node)
        parent.children.insert(insert_index + 1, right_node)

        left_node.parent = parent
        right_node.parent = parent

        if len(parent.keys) > 2:
            self._split(parent)

    def _find_node(self, node, value):

        self.iterations += 1

        if node is None:
            
            return None
        if value in node.keys:
            
            return node
        if node.is_leaf():
            
            return None
        
        if len(node.keys) == 1:
            if value < node.keys[0]:
                
                return self._find_node(node.children[0], value)
            else:
                
                return self._find_node(node.children[1], value)
        else:
            if value < node.keys[0]:
                
                return self._find_node(node.children[0], value)
            elif value < node.keys[1]:
                
                return self._find_node(node.children[1], value)
            else:
                
                return self._find_node(node.children[2], value)
            
    def delete(self, value):

        self.iterations = 0

        node = self._find_node(self.root, value)

        if node is None:
            
            return

        if not node.is_leaf():
            successor_node = self._get_successor(node, value)
            successor_value = successor_node.keys[0]
            index = node.keys.index(value)
            node.keys[index] = successor_value
            node = successor_node
            value = successor_value

        node.keys.remove(value)
        self.iterations += 1

        if len(node.keys) == 0:

            self._fix(node)

    def _get_successor(self, node, value):

        self.iterations += 1

        if value == node.keys[0]:
            current = node.children[1]
        else:
            current = node.children[2]

        while not current.is_leaf():
            current = current.children[0]

        return current

    def _fix(self, node):

        self.iterations += 1

        if node == self.root:
            if node.children:
                self.root = node.children[0]
                self.root.parent = None
            else:
                self.root = None

            return
        
        parent = node.parent
        index = parent.children.index(node)

        if index > 0:
            left_sibling = parent.children[index - 1]
            
            if len(left_sibling.keys) == 2:
                borrowed_key = left_sibling.keys.pop()
                node.keys.append(parent.keys[index - 1])
                parent.keys[index - 1] = borrowed_key
                if left_sibling.children:
                    borrowed_child = left_sibling.children.pop()
                    node.children.insert(0, borrowed_child)
                    borrowed_child.parent = node
                node.keys.sort()
                self.iterations += 1

                return

        if index < len(parent.children) - 1:
            right_sibling = parent.children[index + 1]
            
            if len(right_sibling.keys) == 2:
                borrowed_key = right_sibling.keys.pop(0)
                node.keys.append(parent.keys[index])
                parent.keys[index] = borrowed_key
                if right_sibling.children:
                    borrowed_child = right_sibling.children.pop(0)
                    node.children.append(borrowed_child)
                    borrowed_child.parent = node
                node.keys.sort()
                self.iterations += 1

                return
            
        if index > 0:
            left_sibling = parent.children[index - 1]
            merge_key = parent.keys.pop(index - 1)
            left_sibling.keys.append(merge_key)
            left_sibling.keys.extend(node.keys)
            left_sibling.children.extend(node.children)
            for child in left_sibling.children:
                child.parent = left_sibling
            left_sibling.keys.sort()
            parent.children.remove(node)
            self.iterations += 1

        else:
            right_sibling = parent.children[index + 1]
            merge_key = parent.keys.pop(index)
            node.keys.append(merge_key)
            node.keys.extend(right_sibling.keys)
            node.children.extend(right_sibling.children)
            for child in right_sibling.children:
                child.parent = node
            node.keys.sort()
            parent.children.remove(right_sibling)
            self.iterations += 1

        if len(parent.keys) == 0:
            self._fix(parent)
