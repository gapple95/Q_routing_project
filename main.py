# import node
# import shortest_path_routing as node
import q_routing as node

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Nodes = list()
# avr = list()
# for i in range(0, 36):
#     Nodes.append(node.Node(0, 0, i))
#     avr.append(0)
#
# for i in range(0, 36):
#     # print(i)
#     Nodes[i].init_routing()
#     # print()
#
# # # Nodes[35].init_routing()
# #
# # # for t in range(0, 36):
# # #     for i in range(0, 36):
# # #         # print("t : " + str(t) + ", i : " + str(i))
# # #         Nodes[i].activate(t)
# # avr_count = 100
# # for a in range(0, avr_count):
# #     for i in range(0, 36):
# #         for j in range(0, 36):
# #             if i == j:
# #                 continue
# #             # print(str(i) + ", " + str(j))
# #             Nodes[i].create_packet(0, j)
# #             for l in range(0, 12):
# #                 for k in range(0, 36):
# #                     Nodes[k].activate(0)
# #
# #     for i in range(0, 36):
# #         avr[i] = avr[i] + Nodes[i].hop_count
# #
# #     for i in range(0, 36):
# #         Nodes[i].init_routing()
# #
# # for i in range(0, 36):
# #     if i % 6 == 0:
# #         print()
# #     print(str(avr[i] / avr_count) + " ", end='')
# # print()
# #
# # # Nodes[35].create_packet(0, 28)
# #
# # # for i in range(0, 36):
# # #     Nodes[i].create_packet(0, i)
# # #
# # # for t in range(0, 1000):
# # #     for i in range(0, 36):
# # #         Nodes[i].activate(t)
# # #
# #
# # for i in range(0, 36):
# #     if i % 6 == 0:
# #         print()
# #     print(str(Nodes[i].hop_count) + " ", end='')
# # print()
# #
# # # for i in range(0, len(Nodes[34].success)):
# # #     print(str(Nodes[34].success[i].source) + " ", end='')
# plot_value = list()
# plot_level = list()
# for level in np.arange(1, 3, 0.1):
#     print(level)
#     Nodes = list()
#     avr = list()
#     for i in range(0, 36):
#         Nodes.append(node.Node(0, 0, i))
#         avr.append(0)
#
#     node.Node.load = level
#
#     for i in range(0, 36):
#         Nodes[i].init_routing()
#
#     average_delivery_time_list = list()
#     for episode in range(0, 10):
#         average_delivery = list()
#         for i in range(0, 36):
#             Nodes[i].init_routing()
#
#         for t in range(0, 150000):
#             for i in range(0, 36):
#                 # print("t : " + str(t) + ", i : " + str(i))
#                 Nodes[i].activate(t)
#
#             for i in range(0, 36):
#                 p = Nodes[i].is_success()
#                 if not p == -1:
#                     average_delivery.append(t - p.time_stamp)
#         # t = 150001
#         # c = True
#         # while c:
#         #     for i in range(0, 36):
#         #         Nodes[i].activate_empty_queue(t)
#         #
#         #     for i in range(0, 36):
#         #         p = Nodes[i].is_success()
#         #         if not p == -1:
#         #             average_delivery.append(t - p.time_stamp)
#         #
#         #     check = 0
#         #     for i in range(0, 36):
#         #         check += Nodes[i].is_empty()
#         #     print(check)
#         #     if check == 36:
#         #         c = False
#         #     t += 1
#
#         average_delivery_time_list.append(sum(average_delivery, 0.0) / len(average_delivery))
#
#     print(average_delivery_time_list)
#     print(sum(average_delivery_time_list, 0.0) / len(average_delivery_time_list))
#     plot_value.append(sum(average_delivery_time_list, 0.0) / len(average_delivery_time_list))
#     plot_level.append(level)
#
# plt.plot(plot_level, plot_value)
# plt.show()

# Nodes = list()
# avr = list()
# for i in range(0, 36):
#     Nodes.append(node.Node(0, 0, i))
#     avr.append(0)
#
# for i in range(0, 36):
#     # print(i)
#     Nodes[i].init_routing()
#     # print()
#
# print(node.Node.q_table)
#
# plot_value = list()
# plot_level = list()
# for level in np.arange(1, 3, 0.1):
#     print(level)
#     Nodes = list()
#     avr = list()
#     for i in range(0, 36):
#         Nodes.append(node.Node(0, 0, i))
#         avr.append(0)
#
#     node.Node.load = level
#
#     for i in range(0, 36):
#         Nodes[i].init_routing()
#
#     average_delivery_time_list = list()
#     for episode in range(0, 10):
#         average_delivery = list()
#         for i in range(0, 36):
#             Nodes[i].init_routing()
#
#         for t in range(0, 150000):
#             for i in range(0, 36):
#                 # print("t : " + str(t) + ", i : " + str(i))
#                 Nodes[i].activate(t)
#
#             for i in range(0, 36):
#                 p = Nodes[i].is_success()
#                 if not p == -1:
#                     average_delivery.append(t - p.time_stamp)
#         # t = 150001
#         # c = True
#         # while c:
#         #     for i in range(0, 36):
#         #         Nodes[i].activate_empty_queue(t)
#         #
#         #     for i in range(0, 36):
#         #         p = Nodes[i].is_success()
#         #         if not p == -1:
#         #             average_delivery.append(t - p.time_stamp)
#         #
#         #     check = 0
#         #     for i in range(0, 36):
#         #         check += Nodes[i].is_empty()
#         #     print(check)
#         #     if check == 36:
#         #         c = False
#         #     t += 1
#
#         average_delivery_time_list.append(sum(average_delivery, 0.0) / len(average_delivery))
#
#     print(average_delivery_time_list)
#     print(sum(average_delivery_time_list, 0.0) / len(average_delivery_time_list))
#     plot_value.append(sum(average_delivery_time_list, 0.0) / len(average_delivery_time_list))
#     plot_level.append(level)
#
# plt.plot(plot_level, plot_value)
# plt.show()
#
# print(node.Node.q_table)


Nodes = list()
avr = list()
for i in range(0, 36):
    Nodes.append(node.Node(0, 0, i))
    avr.append(0)

for i in range(0, 36):
    # print(i)
    Nodes[i].init_routing()
    # print()

# Nodes[35].create_packet(0, 1)

# for i in range(0, 36):
#     Nodes[i].create_packet(0, i)

# for t in range(0, 10000):
#     for i in range(0, 36):
#         Nodes[i].activate(t)
#
# for i in range(0, 36):
#     if i % 6 == 0:
#         print()
#     print(len(Nodes[i].success), end=' ')
# print()

avr_count = 100
for a in range(0, avr_count):
    for i in range(0, 10000):
        for j in range(0, 36):
            Nodes[j].activate(i)

    for i in range(0, 36):
        avr[i] = avr[i] + Nodes[i].hop_count

    for i in range(0, 36):
        Nodes[i].init_routing()

for i in range(0, 36):
    if i % 6 == 0:
        print()
    print(str(avr[i] / avr_count) + " ", end='')
print()

print(node.Node.q_table)