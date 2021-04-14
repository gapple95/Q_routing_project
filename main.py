# import node
import shorteset_path_routing as node

# topology = [
#         [(0, 0), (1, 6)],          # 0번 노드
#         [(0, 0), (0, 2)],          # 1번 노드
#         [(0, 0), (1, 2)],          # 2번 노드
#         [(0, 0), (2, 4)],          # 3번 노드
#         [(0, 0), (3, 5)],          # 4번 노드
#         [(0, 0), (4, 11)],         # 5번 노드
#         [(0, 0), (0, 12)],         # 6번 노드
#         [(0, 0), (8, 13)],         # 7번 노드
#         [(0, 0), (7, 14)],         # 8번 노드
#         [(0, 0), (10, 15)],        # 9번 노드
#         [(0, 0), (9, 16)],         # 10번 노드
#         [(0, 0), (5, 17)],         # 11번 노드
#         [(0, 0), (6, 13, 18)],     # 12번 노드
#         [(0, 0), (7, 12, 14, 19)], # 13번 노드
#         [(0, 0), (8, 13, 15, 20)], # 14번 노드
#         [(0, 0), (9, 14, 16, 21)], # 15번 노드
#         [(0, 0), (10, 15, 17, 22)],# 16번 노드
#         [(0, 0), (11, 16, 23)],    # 17번 노드
#         [(0, 0), (12, 19, 24)],    # 18번 노드
#         [(0, 0), (13, 18, 20, 25)],# 19번 노드
#         [(0, 0), (14, 19, 26)],    # 20번 노드
#         [(0, 0), (15, 22, 27)],    # 21번 노드
#         [(0, 0), (16, 21, 23, 28)],# 22번 노드
#         [(0, 0), (17, 22, 29)],    # 23번 노드
#         [(0, 0), (18, 25, 30)],    # 24번 노드
#         [(0, 0), (19, 24, 26, 31)],# 25번 노드
#         [(0, 0), (20, 25, 32)],    # 26번 노드
#         [(0, 0), (21, 28, 33)],    # 27번 노드
#         [(0, 0), (22, 27, 29, 34)],# 28번 노드
#         [(0, 0), (23, 28, 35)],    # 29번 노드
#         [(0, 0), (24, 31)],        # 30번 노드
#         [(0, 0), (25, 30, 32)],    # 31번 노드
#         [(0, 0), (26, 31)],        # 32번 노드
#         [(0, 0), (27, 34)],        # 33번 노드
#         [(0, 0), (28, 33, 35)],    # 34번 노드
#         [(0, 0), (29, 34)]         # 35번 노드
#     ]
#
# print(topology[0][1][len(topology[0][1]) - 1])

# node0 = node.Node(0, 0, 0)
# node1 = node.Node(0, 0, 1)
# node2 = node.Node(0, 0, 2)
# node3 = node.Node(0, 0, 3)
# node4 = node.Node(0, 0, 4)
# node5 = node.Node(0, 0, 5)
# node6 = node.Node(0, 0, 6)
# node7 = node.Node(0, 0, 7)
# node8 = node.Node(0, 0, 8)
# node9 = node.Node(0, 0, 9)
# node10 = node.Node(0, 0, 10)
# node11 = node.Node(0, 0, 11)
# node12 = node.Node(0, 0, 12)
# node13 = node.Node(0, 0, 13)
# node14 = node.Node(0, 0, 14)
# node15 = node.Node(0, 0, 15)
# node16 = node.Node(0, 0, 16)
# node17 = node.Node(0, 0, 17)
# node18 = node.Node(0, 0, 18)
# node19 = node.Node(0, 0, 19)
# node20 = node.Node(0, 0, 20)
# node21 = node.Node(0, 0, 21)
# node22 = node.Node(0, 0, 22)
# node23 = node.Node(0, 0, 23)
# node24 = node.Node(0, 0, 24)
# node25 = node.Node(0, 0, 25)
# node26 = node.Node(0, 0, 26)
# node27 = node.Node(0, 0, 27)
# node28 = node.Node(0, 0, 28)
# node29 = node.Node(0, 0, 29)
# node30 = node.Node(0, 0, 30)
# node31 = node.Node(0, 0, 31)
# node32 = node.Node(0, 0, 32)
# node33 = node.Node(0, 0, 33)
# node34 = node.Node(0, 0, 34)
# node35 = node.Node(0, 0, 35)

Nodes = list()
for i in range(0, 36):
    Nodes.append(node.Node(0, 0, i))

for i in range(0, 36):
    Nodes[i].init_routing()

for t in range(0, 100):
    for i in range(0, 36):
        # print("t : " + str(t) + ", i : " + str(i))
        Nodes[i].activate(t)

for i in range(0, 36):
    if i % 6 == 0:
        print()
    print(str(len(Nodes[i].success)) + " ", end='')


print()

for i in range(0, 36):
    if i % 6 == 0:
        print()
    print(str(Nodes[i].hop_count) + " ", end='')