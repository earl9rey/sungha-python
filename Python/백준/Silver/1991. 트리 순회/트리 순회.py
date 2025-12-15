#7662 이중 우선순위 큐

import sys, heapq
input = sys.stdin.readline

N = int(input())

# 트리 정보를 저장할 딕셔너리
# tree['A'] = ['B', 'C']  → A의 왼쪽 자식은 B, 오른쪽 자식은 C
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 

# 전위 순회 (Preorder)
# 방문 순서: 부모 → 왼쪽 → 오른쪽
def preorder(root):
    if root != '.':
        print(root, end='')  # 부모 방문
        preorder(tree[root][0])  # 왼쪽 방문
        preorder(tree[root][1])  # 오른쪽 방문
 

# 중위 순회 (Inorder)
# 방문 순서: 왼쪽 → 부모 → 오른쪽
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # 왼쪽 방문
        print(root, end='')  # 부모 방문
        inorder(tree[root][1])  # 오른쪽 방문
 
# 후위 순회 (Postorder)
# 방문 순서: 왼쪽 → 오른쪽 → 부모
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # 왼쪽 방문
        postorder(tree[root][1])  # 오른쪽 방문
        print(root, end='')  # 부모 방문
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')