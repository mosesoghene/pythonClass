graph_lengths = []

loop_counter = 1
while loop_counter <= 5:
    user_number_input = int(input("only enter positive integers >> "))
    graph_lengths.append(user_number_input)
    loop_counter += 1

for graph_data in graph_lengths:
    print(graph_data, ":", "*" * graph_data)

