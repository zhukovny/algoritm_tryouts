from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def get_height(root: Node) -> int:
    if not root:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return max(left_height, right_height) + 1


def print_tree(root: Node):
    if not root:
        return

    height = get_height(root)

    for i in range(height):
        print_level(root, i)


def print_level(node: Node, level: int):
    if not node:
        return

    if level == 0:
        print(node.value)
    else:
        print_level(node.left, level - 1)
        print_level(node.right, level - 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_tree(root)
    