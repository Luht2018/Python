# 升级
# 光是根据关键词来判断还不够，所以得有知识体系，才能解决用户的问题
# 通过各种数据库，建立一套体系，通过搜索的方式，来查找
# 根据地图，可以清楚的找寻从一个地方到另一个地方的路径，然后作为回答，
# 反馈给用户

# 建立一个基于目标行业的database
# 比如这里我们用python自带的graph
graph = {
    "上海": ["苏州", "常州"],
    "苏州": ["常州", "镇江"],
    "常州": ["镇江"],
    "镇江": ["常州"],
    "盐城": ["南通"],
    "南通": ["常州"]
}


# 明确如何找到从A到B的路径
def find_path(start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(node, end, path)
            if new_path:
                return new_path
    return None


# 这就是类似构建知识图谱的方法，科目属

print(find_path("苏州", "镇江"))






