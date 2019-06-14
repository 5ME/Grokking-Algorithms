# 第7章 狄克斯特拉算法

## 狄克斯特拉算法（Dijkstra's algorithm）

+ 广度优先搜索找出的是**段数最少**的路径
+ 要找出最快的路径，可以使用狄克斯特拉算法（Dijkstra's algorithm）

+ 狄克斯特拉算法找出的是总权重最小的路径
+ 狄克斯特拉算法四个步骤：
  1. 找出最便宜的节点，即可在最短时间内前往的节点；
  2. 对于该节点的邻居，检查是否有前往它们的更短路径，如果有，就更新其开销；
  3. 重复这个过程，直到对图中的每个节点都这样做了；
  4. 计算最终路径。

+ 狄克斯特拉算法用于每条边都有关联数字的图，这些数字称为**权重**（weight）
+ 带权重的图称为**加权图**（weighted graph），不带权重的图称为**非加权图**（unweighted graph）
+ **狄克斯特拉算法只适用于有向无环图**（directed acyclic graph，DAG）

+ 最短路径并不一定是物理距离，也可能是让某种度量指标最小。

+ **不能将狄克斯特拉算法用于包含负权边的图**

+ 在包含负权边的图中，要找出最短路径，可以使用**贝尔曼-福德算法**（Bellman-Ford algorithm）
  
## 实现

``` Python
# 狄克斯特拉算法
# 2019-06-14

# 表示图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# print(graph["start"].keys())
# print(graph["start"]["a"])
# print(graph["start"]["b"])
# graph["start"]是一个散列表，它又包含了散列表

# 表示权重
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}       # 终点没有邻居

# 创建开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 父节点散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 处理过的节点
processed = []

# 找出开销最低的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:      # 遍历所有节点
        cost = costs[node]
        # 如果当前节点的开销更低且未处理过，就将其视为开销最低的节点
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
# 这个while循环在所有节点都被处理后结束
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历当前节点所有邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:     # 如果经当前节点前往该邻居更近
            costs[n] = new_cost     # 就更新该邻居的开销
            parents[n] = node       # 同时将该邻居的父节点设置为当前节点
    processed.append(node)          # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)     # 找出接下来要处理的节点，并循环

print("Cost from the start to each node:")
print(costs)

'''
输出：
Cost from the start to each node:
{'a': 5, 'b': 2, 'fin': 6}
'''
```

## 小结

1. 广度优先搜索用于在**非加权图**中查找最短路径
2. 狄克斯特拉算法用于在**加权图**中查找最短路径
3. 仅当权重为正时狄克斯特拉算法才管用
4. 如果图中包含负权边，请使用贝尔曼-福德算法
