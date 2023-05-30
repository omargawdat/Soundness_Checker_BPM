import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx


def draw_reachability_graph(reachability_graph, initial_marking, goal_place, is_sound):
    G = nx.DiGraph()

    start_state = ",".join(f"P{place}" for place in initial_marking)
    goal_state = f"P{goal_place}"

    for state, transitions in reachability_graph.items():
        state_str = ",".join(f"P{place}" for place in state)
        G.add_node(state_str)

        for tran, next_state in transitions:
            next_state_str = ",".join(f"P{place}" for place in next_state)
            G.add_edge(state_str, next_state_str, label=f"T{tran.id}")

    pos = nx.spring_layout(G)
    colors = ["limegreen" if node == start_state else "red" if node == goal_state else "lightblue" for node in
              G.nodes()]

    nx.draw(G, pos, with_labels=True, node_size=2000, node_color=colors, font_size=10, font_weight='bold')
    edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    sound_text = "Sound" if is_sound else "Not sound"
    plt.gca().annotate(sound_text, fontsize=20, xy=(1, 1), xycoords='axes fraction',
                       horizontalalignment='right', verticalalignment='top',
                       bbox=dict(facecolor='white', alpha=0.5))

    plt.title("Reachability Graph")
    plt.axis("off")
    plt.show()
