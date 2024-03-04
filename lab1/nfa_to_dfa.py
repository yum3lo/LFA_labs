from finite_automaton_class import FiniteAutomaton

class NFAtoDFAConverter:
    def __init__(self, nfa):
        self.nfa = nfa
        self.dfa = self.convert_to_dfa()

    def convert_to_dfa(self):
        dfa_states = set()  # States of the DFA
        dfa_delta = {}  # Transition function of the DFA
        dfa_initial_state = frozenset([self.nfa.initial_state])  # Initial state of the DFA
        dfa_accept_states = set()  # Accept states of the DFA

        unmarked_states = [dfa_initial_state]  # Unmarked states of the DFA

        # While there are unmarked states in the DFA
        while unmarked_states:
            current_dfa_state = unmarked_states.pop(0)
            dfa_states.add(current_dfa_state)

            # Check if the current DFA state is an accept state
            if any(state in self.nfa.accept_states for state in current_dfa_state):
                dfa_accept_states.add(current_dfa_state)

            # Initialize the transition dictionary for the current DFA state
            dfa_delta[current_dfa_state] = {}

            # Iterate over each symbol in the alphabet
            for symbol in self.nfa.alphabet:
                next_nfa_states = set()  # Next states in the NFA

                # Find the next states in the NFA for the current symbol
                for state in current_dfa_state:
                    next_nfa_states.update(self.nfa.transitions.get(state, {}).get(symbol, set()))

                # Create the next DFA state from the next NFA states
                next_dfa_state = frozenset(next_nfa_states)

                # Add the transition to the DFA transition function
                dfa_delta[current_dfa_state][symbol] = next_dfa_state

                # Add the next DFA state to unmarked states if it's not already marked
                if next_dfa_state not in dfa_states:
                    unmarked_states.append(next_dfa_state)

        return FiniteAutomaton(dfa_states, self.nfa.alphabet, dfa_delta, dfa_initial_state, dfa_accept_states)