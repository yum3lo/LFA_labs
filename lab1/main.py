from grammar_class import Grammar
from finite_automaton_class import FiniteAutomaton
import networkx as nx
import matplotlib.pyplot as plt

# Testing the functionalities
grammar = Grammar()
print(grammar.classify_grammar())
automaton = grammar.convert_to_fa()

print("Generated strings:")
for _ in range(5):
    gen_string = grammar.generate_string(max_length=15)
    if automaton.accepts(gen_string):
        print(f"{gen_string} (accepted)")
    else:
        print(f"{gen_string} (rejected)")
 
print("\nTested strings:")
tested_strings = ['aca', 'aede', 'caeda']
for string in tested_strings:
    if automaton.accepts(string):
        print(f"{string} (accepted)")
    else:
        print(f"{string} (rejected)")

# Define the finite automaton
Q = {'q0', 'q1', 'q2', 'q3', 'q4'}
Sigma = {'a', 'b'}
F = {'q3'}
delta = {
    'q0': {'a': 'q1'},
    'q1': {'b': 'q1', 'b': 'q2'},
    'q2': {'b': 'q0', 'a': 'q3'},
    'q3': {'a': 'q4'},
    'q4': {'a': 'q0'},
}

# Create an instance of the FiniteAutomaton class
finite_automaton = FiniteAutomaton(Q, Sigma, delta, 'q0', F)

# Check if the finite automaton is deterministic
if finite_automaton.is_deterministic():
    print("The finite automaton is deterministic.")
else:
    print("The finite automaton is nondeterministic.")

# The graph
G = nx.DiGraph()
G.add_nodes_from(Q)
for state, transitions in delta.items():
    for symbol, next_state in transitions.items():
        G.add_edge(state, next_state, label=symbol)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=1500, arrowsize=20, font_size=15, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Highlight final states
final_states = F.intersection(Q)
nx.draw_networkx_nodes(G, pos, nodelist=final_states, node_color='salmon', node_size=2000)

# Add a title
plt.title("Finite Automaton")

# Display the graph
plt.axis('off')
plt.show()