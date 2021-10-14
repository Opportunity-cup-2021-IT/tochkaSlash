from pyvis.network import Network

# создаём сеть
net = Network('700px', '700px', notebook=False)

# создаём ноды
net.add_node(1, label="Work #1", title="Start: 01.01.2020\nEnd:06.01.2020")

net.add_node(2, label="Work #2", title="Start: 16.01.2020\nEnd:18.01.2020")
net.add_node(3, label="Work #3", title="Start: 12.01.2020\nEnd:15.01.2020")
net.add_node(4, label="Work #4", title="Start: 07.01.2020\nEnd:16.01.2020")

net.add_node(5, label="Work #5", title="Start: 18.01.2020\nEnd:18.01.2020")

net.add_node(6, label="Work #6", title="Start: 18.01.2020\nEnd:22.01.2020")
net.add_node(7, label="Work #7", title="Start: 18.01.2020\nEnd:24.01.2020")

net.add_node(8, label="Work #8", title="Start: 20.01.2020\nEnd:20.01.2020")

net.add_node(9, label="Work #9", title="Start: 25.01.2020\nEnd:29.01.2020")

width_works = 1.5
width_milestones = 0.25

# связываем ноды между собой
net.add_edge(1, 2, label="10 days", width=width_works)
net.add_edge(1, 3, label="6 days", width=width_works)
net.add_edge(1, 4, label="1 day", width=width_works)

net.add_edge(2, 5, label="0 days", width=width_milestones)
net.add_edge(3, 5, label="0 days", width=width_milestones)

net.add_edge(4, 8, label="4 days", title="4", width=width_milestones)

net.add_edge(5, 6, label="0 days", width=width_works)
net.add_edge(5, 7, label="0 days", width=width_works)
net.add_edge(8, 9, label="5 days", width=width_works)

net.add_edge(6, 9, label="3 days", width=width_works)
net.add_edge(7, 9, label="1 day", width=width_works)


net.toggle_physics(False)

net.show("without shift.html")
