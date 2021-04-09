# test_path 실행 파일
import test_path as node

Nodes = list()
for i in range(0, 36):
    Nodes.append(node.Node(0, 0, i))

# 0번 노드에 하나의 패킷 생성
Nodes[0].create_packet(0)

for t in range(0, 36):
    for i in range(0, 36):
        print("t : " + str(t) + ", i : " + str(i))
        Nodes[i].activate(t)

print(len(Nodes[35].success))