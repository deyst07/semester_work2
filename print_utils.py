from collections import deque


def print_tree(root):

    if root is None:

        print("Tree is empty")
        return

    queue = deque()
    queue.append((root, 0))
    current_level = 0

    print(f"Level {current_level}:", end=" ")

    while queue:
        node, level = queue.popleft()

        if level != current_level:
            current_level = level

            print()
            print(f"Level {current_level}:", end=" ")

        print(node.keys, end=" ")

        for child in node.children:

            queue.append((child, level + 1))

    print()
