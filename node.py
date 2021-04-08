import packet
import random


class Node:
    # topology = list()       # grid, 6x6 등등
    # grid_topology 구현
    topology = [
        [(0, 0), (1, 6)],  # 0번 노드
        [(0, 0), (0, 2)],  # 1번 노드
        [(0, 0), (1, 2)],  # 2번 노드
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
    load_period = 1
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

    def receive(self):
        # 자신에게 보내진 패킷을 찾아서 처리
        for i in Node.packet_queue:
            # 패킷 i 확인
            if i.next == self.id:
                # 해당 패킷이 목표 노드라면
                if i.destination == self.id:
                    pass
                # 아니라면 큐에 저장
                else:
                    # 패킷 i의 next 결정

                    # 패킷을 노드의 큐에 저장
                    self.queue.append(i)
                    self.hop_count += 1
            # 해당 패킷이 노드를 찾았으면 배열에서 제거
            Node.packet_queue.remove(i)

    def send(self):
        # 노드의 큐에서 패킷을 꺼내 전송
        Node.packet_queue.append(self.queue.pop())

    def create_packet(self):
        # 목표 노드 설정
        # 자신을 제외한 나머지 노드들 중에 랜덤하게 선택
        while 1:
            destination = random.randrange(0, len(Node.topology))
            if not destination == self.id:
                break

        # 이웃 노드 설정
        next = 0
        # 패킷 생성
        p = packet.Packet(0, self.id, destination, next)
        self.queue.append(p)

    def activate(self, t):
        # 패킷을 주기마다 생성
        if t % Node.load_period == 0:
            for i in range(0, Node.load):
                self.create_packet()
            self.load_period = 0

        # 다른 노드에서 보낸 패킷을 큐에 저장
        self.receive()

        # 패킷 전송
        self.send()
