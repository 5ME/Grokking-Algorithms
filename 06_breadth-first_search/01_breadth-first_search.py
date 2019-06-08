# -*- coding: utf-8 -*-
# 广度优先搜索
# 2019-06-08

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []       # 用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:      # 仅当这个人没检查过时才检查
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)     # 将这个人标记为检查过
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search("you")
