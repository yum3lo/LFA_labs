import matplotlib.pyplot as plt
import networkx as nx
class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = accept_states
        self.is_deterministic = self.is_deterministic

    def is_deterministic(self):
        # Iterate over each state in the finite automaton
        for state in self.states:
            transitions_from_state = self.transitions.get(state, {})
            seen_symbols = set()

            # Check transitions for each symbol in the alphabet
            for symbol in self.alphabet:
                if symbol in transitions_from_state:
                    # If the symbol was seen before, the finite automaton is nondeterministic
                    if symbol in seen_symbols:
                        return False
                    seen_symbols.add(symbol)
        return True

    def accepts(self, input_string):
        current_state = self.initial_state

        for symbol in input_string:
            # Check if the current state has a transition defined for the current symbol
            if current_state in self.transitions and symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                # If there's no transition defined, the string cannot be obtained by state transitions
                return False
            if symbol not in self.alphabet:
                # If the symbol is not part of the alphabet, the string cannot be obtained by state transitions
                return False

        # Check if the final state after processing all symbols is one of the accept states
        return current_state in self.accept_states
    
# Create a directed graph
G = nx.DiGraph()
nodes = ['q0', 'q1', 'q2', 'q3', 'q4']
G.add_nodes_from(nodes)
edges = [('q0', 'q1', 'a'), ('q1', 'q2', 'b'), ('q2', 'q0', 'b'),
         ('q3', 'q4', 'a'), ('q4', 'q0', 'a'), ('q2', 'q3', 'a'), ('q1', 'q1', 'b')]
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)  # Position nodes using the spring layout algorithm
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=12, arrowsize=20)
edge_labels = {edge[:2]: edge[2] for edge in edges}  # Create a dictionary of edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Draw edge labels

# Show the graph
plt.title('Finite Automaton')
plt.show()