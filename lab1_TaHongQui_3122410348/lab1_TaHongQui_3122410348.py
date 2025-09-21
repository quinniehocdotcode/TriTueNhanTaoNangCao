ADJ = {'A': ['C', 'E', 'F', 'D'], 'B': [], 'C': ['H'], 'D': ['E', 'H'], 'E': ['K', 'I'], 'F': ['I', 'G'], 'G': [], 'H': ['K'], 'I': ['K', 'B'], 'K': ['B']}
import pprint
pprint.pprint(ADJ)
print('2. Thao tác duyệt đồ thị')
print('(a) Liệt kê các đỉnh trong đồ thị')
print('Các đỉnh của đồ thị: ', end=' ')
print(sorted(list(ADJ.keys())))
print('(b) Liệt kê tất cả các cạnh đồ thị hiển thị dạng danh sách kề')
print('Danh sách kề của đồ thị: ')

def HienThiDoThi(G):
    for u in sorted(G.keys()):
        ke = ' '.join(G[u])
        print(f'{u}: {ke}')
HienThiDoThi(ADJ)
print('(c) Cho hai đỉnh A, B. Hỏi hai đỉnh A, B có kề nhau không?')

def LaKe(G, a, b):
    if a not in G or b not in G:
        return -1
    return 1 if b in G[a] else 0
a = 'L'
b = 'R'
print(f'{a} ke {b}: {LaKe(ADJ, a, b)}')
a = 'A'
b = 'R'
print(f'{a} ke {b}: {LaKe(ADJ, a, b)}')
a = 'E'
b = 'D'
print(f'{a} ke {b}: {LaKe(ADJ, a, b)}')
a = 'D'
b = 'E'
print(f'{a} ke {b}: {LaKe(ADJ, a, b)}')
print('(d) Cho một đỉnh A. Hỏi danh sách các đỉnh kề với A')

def LayKe(G, a):
    if a not in G:
        return None
    return list(G[a])
a = 'P'
print(f'Danh sach ke voi dinh {a}: {LayKe(ADJ, a)}')
a = 'A'
print(f'Danh sach ke voi dinh {a}: {LayKe(ADJ, a)}')
a = 'B'
print(f'Danh sach ke voi dinh {a}: {LayKe(ADJ, a)}')
a = 'D'
print(f'Danh sach ke voi dinh {a}: {LayKe(ADJ, a)}')
print('1. Lưu đồ thị xuống tập tin')

def LuuDoThi(G, file_path, verbose=True):
    import os
    file_dir = os.path.dirname(file_path)
    if file_dir != '' and (not os.path.exists(file_dir)):
        os.makedirs(file_dir)
        if verbose:
            print(f'+ Tao thu muc: {file_dir}')
    with open(file_path, 'wt', encoding='utf-8') as file:
        file.write(str(len(G)) + '\n')
        for u in sorted(G.keys()):
            line = ' '.join([u] + G[u])
            file.write(line + '\n')
        if verbose:
            print(f'Luu do thi thanh cong xuong tap tin: {file_path}')
LuuDoThi(ADJ, 'dske1.txt', verbose=True)
with open('dske1.txt', 'rt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
print('\n2. Đọc đồ thị từ tập tin')
import pprint

def DocDoThi(file_path, verbose=True):
    import os
    if not os.path.exists(file_path):
        return None
    G = {}
    with open(file_path, 'rt', encoding='utf-8') as file:
        n = int(file.readline().strip())
        for _ in range(n):
            raw = file.readline()
            if raw is None or raw == '':
                break
            tokens = raw.strip().split()
            if len(tokens) == 0:
                continue
            u = tokens[0]
            neighbors = tokens[1:] if len(tokens) > 1 else []
            G[u] = neighbors
    return G
G1 = DocDoThi('dske1.txt', verbose=True)
pprint.pprint(G1)

def BFS(G, start, goal):
    if start not in G or goal not in G:
        return None
    from collections import deque
    q = deque([start])
    parent = {start: None}
    visited = set([start])
    while q:
        u = q.popleft()
        if u == goal:
            break
        for v in G[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)
    return parent
path_bfs = BFS(ADJ, 'A', 'B')
print('BFS parent mapping:')
pprint.pprint(path_bfs)

def find_path(parent, start, goal):
    if parent is None:
        return []
    if start == goal:
        return [start]
    if goal not in parent:
        return []
    cur = goal
    route = []
    while cur is not None:
        route.append(cur)
        cur = parent.get(cur, None)
    route.reverse()
    return route if len(route) > 0 and route[0] == start else []
print('Đường đi BFS A -> B:', find_path(path_bfs, 'A', 'B'))

def DFS(G, start, goal):
    if start not in G or goal not in G:
        return None
    stack = [start]
    parent = {start: None}
    visited = set()
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        if u == goal:
            break
        for v in reversed(G[u]):
            if v not in visited and v not in parent:
                parent[v] = u
                stack.append(v)
    return parent
path_dfs = DFS(ADJ, 'A', 'B')
print('DFS parent mapping:')
pprint.pprint(path_dfs)
print('Đường đi DFS A -> B:', find_path(path_dfs, 'A', 'B'))