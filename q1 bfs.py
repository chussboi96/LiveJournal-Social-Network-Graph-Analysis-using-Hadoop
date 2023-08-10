import time
from collections import deque
from csv import writer


def append_list_as_row(file_name, list_of_elem):        # function appends list of elements to a CSV file as a new row.
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)


def bfs(graph, start, end):         # BFS algorithm
    visited = set()
    queue = deque([[start, []]])
    while queue:
        current_node, prev_path = queue.popleft()
        visited.add(current_node)
        if current_node == end:
            return prev_path + [current_node]

        if current_node in graph.keys():
            for links in graph[current_node]:
                if links == end:
                    return prev_path + [current_node, links]
                if links not in visited:
                    queue.append([links, prev_path + [current_node]])
    return [-1]


roll_no = 1381  # last 4 digits of 21i-wxyz, roll_no = wxyz
file = f"i21{roll_no}.csv"
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
print(f"Total time taken to read the file was: {round(t,2)} mins.")

st = time.time()
# loop to find paths (storing in csv)
for i in range(4847571):
    print(i)
    x1 = bfs(nodes, roll_no, i)
    append_list_as_row(file, x1)

et = time.time()
t = (et - st)/60
print(f"Total Execution time was: {round(t,2)} mins.")
