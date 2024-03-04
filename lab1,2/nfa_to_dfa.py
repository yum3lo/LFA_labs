class DFAConverter:
    def __init__(self, nfa):
        self.nfa = nfa
        self.dfa_states = {}  # Dictionary to store DFA states and their transitions
        self.alphabet = nfa.alphabet

    def convert_to_dfa(self):
        initial_state = frozenset([self.nfa.initial_state])  # Initial state of the DFA
        self.dfa_states[initial_state] = {}  # Initialize with the initial state of the DFA
        self.explore_state(initial_state)

    def explore_state(self, state):
        for symbol in self.alphabet:
            next_states = self.nfa.next_state_for_symbol(state, symbol)
            if next_states:
                next_state = frozenset(next_states)
                if next_state not in self.dfa_states:
                    self.dfa_states[next_state] = {}
                    self.explore_state(next_state)
                self.dfa_states[state][symbol] = next_state

    def print_dfa_transitions(self):
        print("DFA transitions:")
        for state, transitions in self.dfa_states.items():
            for symbol, next_state in transitions.items():
                print(f"{state} -> {symbol}{next_state}")