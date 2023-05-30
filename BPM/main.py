from collections import defaultdict

from Solver import Solver
from Transaction import Transaction
from drawer import draw_reachability_graph


def input_data(choice):
    if choice != 1 and choice != 2 and choice != 3:
        return None, None, None

    if choice == 1:
        initial_marking = {0}
        goal_place = 6
        edges = [('P0', 'T1'), ('T1', 'P1'), ('P1', 'T2'),
                 ('T2', 'P2'), ('P2', 'T3'), ('T3', 'P3'), ('P3', 'T5'), ('T5', 'P6'),
                 ('T2', 'P4'), ('P4', 'T4'), ('T4', 'P5'), ('P5', 'T6'), ('T6', 'P6')]
    elif choice == 2:
        initial_marking = {1}
        goal_place = 6
        edges = [('P1', 'T1'), ('T1', 'P2'), ('T1', 'P3'), ('P2', 'T2'), ('P2', 'T5'), ('P3', 'T3'), ('T2', 'P4'),
                 ('T3', 'P5'),
                 ('P4', 'T4'), ('P5', 'T4'), ('P5', 'T5'), ('T4', 'P6'), ('T5', 'P6')]
    elif choice == 3:
        initial_marking = {int(input("- Initial place number: "))}
        goal_place = int(input("- Goal place number: "))
        edge_count = int(input("- Number of edges: "))
        edges = []
        print("Enter the edges (in this format P1 T2):")
        for _ in range(edge_count):
            edge = tuple(input().split())
            edges.append(edge)

    return initial_marking, goal_place, edges


if __name__ == '__main__':
    # for using lecture tests use choice = 1, or choice =2, for dynamic put choice = 3
    initial_marking, goal_place, edges = input_data(choice=3)

    transactions = defaultdict(Transaction)
    # initialize the transactions
    for edge in edges:
        if edge[0][0] == 'T':
            transactions[edge[0][1]] = Transaction(edge[0][1])
        else:
            transactions[edge[1][1]] = Transaction(edge[1][1])

    # add the required and next places to each transaction
    for edge in edges:
        if edge[0][0] == 'T':
            transactions[edge[0][1]].add_next_place(int(edge[1][1]))
        else:
            transactions[edge[1][1]].add_required_place(int(edge[0][1]))
    #  convert the dict into a list
    transactions = [value for key, value in transactions.items()]

    solver = Solver(transactions, initial_marking, goal_place)
    is_sound = solver.is_sound()
    # print(is_sound)
    draw_reachability_graph(solver.reachability_graph, initial_marking, goal_place, is_sound)
