import queue


def bfs(tree):
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        key, children = q.get()
        yield key
        for child in children:
            q.put(child)
