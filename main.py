# import node
import shorteset_path_routing as node

Nodes = list()
for i in range(0, 36):
    Nodes.append(node.Node(0, 0, i))

for i in range(0, 36):
    Nodes[i].init_routing()

# for t in range(0, 36):
#     for i in range(0, 36):
#         # print("t : " + str(t) + ", i : " + str(i))
#         Nodes[i].activate(t)

for i in range(0, 36):
    for j in range(0, 36):
        if i == j:
            continue
        Nodes[i].create_packet(0, j)
        for k in range(0, 36):
            Nodes[k].activate(0)

# for i in range(0, 36):
#     Nodes[i].create_packet(0, i)
#
# for t in range(0, 1000):
#     for i in range(0, 36):
#         Nodes[i].activate(t)
#
for i in range(0, 36):
    if i % 6 == 0:
        print()
    print(str(len(Nodes[i].success)) + " ", end='')


print()

for i in range(0, 36):
    if i % 6 == 0:
        print()
    print(str(Nodes[i].hop_count) + " ", end='')

# print()
# for i in range(0, len(Nodes[34].success)):
#     print(str(Nodes[34].success[i].source) + " ", end='')