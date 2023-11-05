def dfs(tree):
    key, children = tree
    yield key
    for child in children:
        for key in dfs(child):
            yield key
