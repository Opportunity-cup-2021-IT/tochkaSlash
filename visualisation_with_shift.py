from pyvis.network import Network
import model_algoritm
from model_algoritm import shifted_ids, id_shifted_work, shift_time

# создаём сеть
net = Network('700px', '700px', notebook=False)
net.add_node(1, label="Work #1", title="Start: 01.01.2020\nEnd:06.01.2020")

net.add_node(2, label="Work #2", title="Start: 16.01.2020\nEnd:18.01.2020")
net.add_node(3, label="Work #3", title="Start: 12.01.2020\nEnd:15.01.2020")
net.add_node(4, label="Work #4", title="Start: 07.01.2020\nEnd:16.01.2020")

net.add_node(5, label="Work #5", title="Start: 18.01.2020\nEnd:18.01.2020")

net.add_node(6, label="Work #6", title="Start: 18.01.2020\nEnd:22.01.2020")
net.add_node(7, label="Work #7", title="Start: 18.01.2020\nEnd:24.01.2020")

net.add_node(8, label="Work #8", title="Start: 20.01.2020\nEnd:20.01.2020")

net.add_node(9, label="Work #9", title="Start: 25.01.2020\nEnd:29.01.2020")

width_works = 1.6
width_milestones = 0.20

net.add_edge(1, 2, title="10 days", width=width_works)
net.add_edge(1, 3, title="6 days", width=width_works)
net.add_edge(1, 4, title="1 day", width=width_works)

net.add_edge(2, 5, title="0 days", width=width_milestones)
net.add_edge(3, 5, title="0 days", width=width_milestones)

net.add_edge(4, 8, title="4 days", width=width_milestones)

net.add_edge(5, 6, title="0 days", width=width_works)
net.add_edge(5, 7, title="0 days", width=width_works)
net.add_edge(8, 9, title="5 days", width=width_works)

net.add_edge(6, 9, title="3 days", width=width_works)
net.add_edge(7, 9, title="1 day", width=width_works)


all_shifted_works = shifted_ids[1:]

net.get_node(int(id_shifted_work))['color'] = '#FFD700'

for shifted_work in all_shifted_works:
    net.get_node(shifted_work)['color'] = '#dd4b39'
net.add_node("CounterShifted", label=f"{len(all_shifted_works) + 1} перенесено", color='#00B200')

net.toggle_physics(False)


net.show(f"work{id_shifted_work}_shifted_{int(shift_time / 86400)}days.html")
