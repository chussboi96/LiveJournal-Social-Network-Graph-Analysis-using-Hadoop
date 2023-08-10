import heapq
from csv import writer
import time


def append_list_as_row(file_name, list_of_elem):         # function appends list of elements to a CSV file as a new row
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)


def dijkstra(graph, start):
    dist = {start: 0}
    prev = {}
    pq = [(0, start)]
    while pq:
        (d, current_node) = heapq.heappop(pq)
        if d > dist[current_node]:
            continue
        for neighbor in graph.get(current_node, []):
            cost = 1
            if current_node in dist:
                new_cost = dist[current_node] + cost
                if neighbor not in dist or new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    prev[neighbor] = current_node
                    heapq.heappush(pq, (new_cost, neighbor))
    return prev, dist


roll_number = 2696  # last 4 digits of 21i-wxyz: wxyz
file = f"i21{roll_number}.csv"
print(file)

st = time.time()
count = 0
nodes = {}
with open(r"C:\Users\HAMMAD\Downloads\soc-LiveJournal1.txt") as f:
    for lines in f.readlines():
        count += 1
        if count > 4:
            x = lines.strip().split()
            if int(x[0]) in nodes:
                nodes[int(x[0])].append(int(x[1]))
            else:
                nodes[int(x[0])] = [int(x[1])]
et = time.time()
t = (et - st)/60
print(f"Total Time taken to read the file was: {round(t,2)} mins.")

# find shortest paths and store in CSV
st = time.time()
for i in range(4847571):
    print(i)
    prev, dist = dijkstra(nodes, roll_number)
    path = []
    node = i
    while node in prev:
        path.append(node)
        node = prev[node]
    if node == roll_number:
        path.append(node)
        append_list_as_row(file, path[::-1])
    else:
        append_list_as_row(file, [-1])
input("Press enter to stop the program")
et = time.time()
t = (et - st)/60
print(f"ELapsed time was: {round(t,2)} mins.")
