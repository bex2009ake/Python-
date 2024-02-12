# import networkx as nx
# import matplotlib.pyplot as plt


# g = nx.Graph()

# g.add_node('isystem')
# g.add_node('myschool')
# g.add_node('resultschool')
# g.add_node('juniorcode')



# g.add_edge('isystem','myschool')
# g.add_edge('isystem','resultschool')
# g.add_edge('isystem','juniorcode')
# g.add_edge('juniorcode','myschool')
# g.add_edge('juniorcode','isystem')
# nx.draw(g,with_labels = True)
# plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt
# from queue import Queue

# # O'quv markazlarini (filiallar) yaratish
# oquv_markazlari = {
#     "Aziz": (0, 0),
#     "Behruz": (2, 0),
#     "Islom": (1, -1),
#     "Ziyov": (3, -1),
#     "Abu": (1, -2),
#     "Said": (2, -2),
#     "Fazl": (3, -2)
# }

# # Tarmoqni yaratish (DiGraph turi)
# G = nx.DiGraph()

# # O'quv markazlarini aloqalash
# G.add_edges_from([
#     ("Aziz", "Behruz"),
#     ("Aziz", "Islom"),
#     ("Behruz", "Islom"),
#     ("Behruz", "Ziyov"),
#     ("Islom", "Abu"),
#     ("Islom", "Said"),
#     ("Ziyov", "Fazl"),
# ])

# # Aloqalar ustiga markazlarni joylash
# pos = oquv_markazlari

# # Grafni ko'rsatish
# nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue")

# # Xabar almashish va jo'natish uchun queue yaratish
# message_queue = Queue()


# def send_message(sender, recipient, message):
#     message_queue.put((sender, recipient, message))
#     print(f"Xabar jo'natildi: {sender} -> {recipient}: {message}")


# def process_messages():
#     while not message_queue.empty():
#         sender, recipient, message = message_queue.get()
#         print(f"Xabar qabul qilindi: {sender} -> {recipient}: {message}")


# # Xabarlarni yuborish
# send_message("Aziz", "Behruz", "Salom, Behruz!")
# send_message("Fazl", "Islom", "Qalaysizmi, Filial Islom?")

# # Xabarlarni qabul qilish
# process_messages()

# # Grafni ko'rsatish
# plt.show()


# a = []

# b = 'Anor'
# c = 'rohat'
# b.lower()
# c.lower()


# for i in range(len(c)):
#    a.append(c[0:i] in b)

# print(a.count(True) > a.count(False))


print(input('First: ')[-1] == input('Second: ')[0])