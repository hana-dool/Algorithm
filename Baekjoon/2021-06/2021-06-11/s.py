from collections import defaultdict
import sys

input = sys.stdin.readline

trees = defaultdict(int)
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    n += 1

tree_lst = list(trees.keys())
tree_lst.sort()
for tree in tree_lst:
    print('%s %.4f' % (tree, trees[tree] / n * 100))
