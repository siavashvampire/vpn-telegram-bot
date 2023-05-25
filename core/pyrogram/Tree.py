from collections import defaultdict


def Tree():
    return defaultdict(Tree)


user_pocket = Tree()
