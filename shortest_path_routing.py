import packet
import random
import heapq


class Node:
    # topology = list()       # grid, 6x6 등등
    # grid_topology 구현
    topology = [
        [(0, 0), (1, 6)],  # 0번 노드
        [(0, 0), (0, 2)],  # 1번 노드
        [(0, 0), (1, 3)],  # 2번 노드
        [(0, 0), (2, 4)],  # 3번 노드
        [(0, 0), (3, 5)],  # 4번 노드
        [(0, 0), (4, 11)],  # 5번 노드
        [(0, 0), (0, 12)],  # 6번 노드
        [(0, 0), (8, 13)],  # 7번 노드
        [(0, 0), (7, 14)],  # 8번 노드
        [(0, 0), (10, 15)],  # 9번 노드
        [(0, 0), (9, 16)],  # 10번 노드
        [(0, 0), (5, 17)],  # 11번 노드
        [(0, 0), (6, 13, 18)],  # 12번 노드
        [(0, 0), (7, 12, 14, 19)],  # 13번 노드
        [(0, 0), (8, 13, 15, 20)],  # 14번 노드
        [(0, 0), (9, 14, 16, 21)],  # 15번 노드
        [(0, 0), (10, 15, 17, 22)],  # 16번 노드
        [(0, 0), (11, 16, 23)],  # 17번 노드
        [(0, 0), (12, 19, 24)],  # 18번 노드
        [(0, 0), (13, 18, 20, 25)],  # 19번 노드
        [(0, 0), (14, 19, 26)],  # 20번 노드
        [(0, 0), (15, 22, 27)],  # 21번 노드
        [(0, 0), (16, 21, 23, 28)],  # 22번 노드
        [(0, 0), (17, 22, 29)],  # 23번 노드
        [(0, 0), (18, 25, 30)],  # 24번 노드
        [(0, 0), (19, 24, 26, 31)],  # 25번 노드
        [(0, 0), (20, 25, 32)],  # 26번 노드
        [(0, 0), (21, 28, 33)],  # 27번 노드
        [(0, 0), (22, 27, 29, 34)],  # 28번 노드
        [(0, 0), (23, 28, 35)],  # 29번 노드
        [(0, 0), (24, 31)],  # 30번 노드
        [(0, 0), (25, 30, 32)],  # 31번 노드
        [(0, 0), (26, 31)],  # 32번 노드
        [(0, 0), (27, 34)],  # 33번 노드
        [(0, 0), (28, 33, 35)],  # 34번 노드
        [(0, 0), (29, 34)]  # 35번 노드
    ]
    # 전송속도
    s = 1
    # 패킷 생성 주기
    load_period = 1
    # 패킷 생성 수
    load = 1

    # 패킷을 임시로 담아두는 배열
    packet_queue = list()

    def __init__(self, x, y, _id):
        self.x = x
        self.y = y
        self.id = _id
        self.queue = list()
        self.routing_table = list()
        self.hop_count = 0
        self.success = list()

    def receive(self):
        # 자신에게 보내진 패킷을 찾아서 처리
        for i in Node.packet_queue:
            # 패킷 i 확인
            if i.next == self.id:
                self.hop_count += 1
                # 해당 패킷이 목표 노드라면
                if i.destination == self.id:
                    self.success.append(i)
                # 아니라면 큐에 저장
                else:
                    # 패킷 i의 next 결정
                    i.next = self.select_next(i.destination)
                    # 패킷을 노드의 큐에 저장
                    self.queue.append(i)
                # 해당 패킷이 노드를 찾았으면 배열에서 제거
                Node.packet_queue.remove(i)

    def select_next(self, packet_destination):
        return self.routing_table[packet_destination]

    def send(self):
        # 이웃 노드 설정
        # 패킷의 목표 주소를 기준으로 선정
        if not len(self.queue) == 0:
            p = self.queue.pop()
            p.next = self.select_next(p.destination)

            # 노드의 큐에서 패킷을 꺼내 전송
            Node.packet_queue.append(p)

    def create_packet_random(self, t):
        # 목표 노드 설정
        # 자신을 제외한 나머지 노드들 중에 랜덤하게 선택
        while 1:
            destination = random.randrange(0, len(Node.topology))
            if not destination == self.id:
                break

        # 패킷 생성
        # 이웃 노드는 아직 설정하지 않기 때문에 0
        p = packet.Packet(t, self.id, destination, 0)
        self.queue.append(p)

    def create_packet(self, t, destination):
        # 패킷 생성
        # 이웃 노드는 아직 설정하지 않기 때문에 0
        p = packet.Packet(t, self.id, destination, 0)
        self.queue.append(p)

    def activate(self, t):
        # 패킷을 주기마다 생성
        # if t % Node.load_period == 0:
        #     for i in range(0, Node.load):
        #         self.create_packet_random(t)

        # 다른 노드에서 보낸 패킷을 큐에 저장
        self.receive()

        # 패킷 전송
        self.send()

    def init_routing(self):
        # 토폴로지 크기
        size = len(Node.topology)
        # 토폴로지 크기 만큼 라우팅 테이블 초기화
        self.routing_table = [0 for i in range(size)]
        # hop 초기화
        self.hop_count = 0

        distances = {vertex : [float('inf'), self.id] for vertex in range(0,size )}

        distances[self.id] = [0, self.id]

        queue = list()

        queue.append([distances[self.id][0], self.id])

        while queue:
            # print(queue)
            current_distance, current_vertex = queue.pop(0)
            # print("# " + str(current_vertex) + ", " + str(current_distance))

            if distances[current_vertex][0] < current_distance:
                continue

            dis_path = list()
            for v in Node.topology[current_vertex][1]:
                dis_path.append(v)

            distance = current_distance + 1
            # print(dis_path)
            for v in random.sample(dis_path, len(dis_path)):
                # print(v)

                if distance < distances[v][0]:
                    # print("[" + str(v) + "]")
                    distances[v] = [distance, current_vertex]
                    queue.append([distance, v])
        # start = self.id
        # end = 35
        # path = end
        # path_output = str(end) + '->'
        # while distances[path][1] != start:
        #     path_output += str(distances[path][1]) + '->'
        #     path = distances[path][1]
        # path_output += str(start)
        # print(path_output)
        for i in range(0, size):
            start = self.id
            end = i
            if start == end:
                continue

            path = end
            ###
            path_output = str(end) + '->'
            ###
            while distances[path][1] != start:
                path = distances[path][1]
                ###
                path_output += str(path) + '->'
                ###

            ###
            path_output += str(start)
            # print(path_output)
            ###

            self.routing_table[i] = path