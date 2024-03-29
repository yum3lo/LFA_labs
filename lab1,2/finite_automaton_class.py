class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = accept_states

    def is_deterministic(self):
        for state in self.states:
            transitions_from_state = self.transitions.get(state, {})
            seen_symbols = set()

            # Check transitions for each symbol in the alphabet
            for symbol in self.alphabet:
                if symbol in transitions_from_state:
                    # If the symbol was seen before, the finite automaton is nondeterministic
                    if symbol in seen_symbols or len(transitions_from_state[symbol]) > 1:
                        return False
                    seen_symbols.add(symbol)
        return True

    def get_next_states(self, current_state, symbol):
        # Get the next states based on the current state and input symbol
        # Check if the current state and symbol combination has transitions defined
        if current_state in self.transitions and symbol in self.transitions[current_state]:
            return self.transitions[current_state][symbol]
        else:
            return set()

    def accepts(self, input_string):
        current_state = self.initial_state

        for symbol in input_string:
            # Check if the current state has a transition defined for the current symbol
            if current_state in self.transitions and symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                # If no transition defined, the string cannot be obtained by state transitions
                return False
            if symbol not in self.alphabet:
                # If the symbol is not in the alphabet, the string cannot be obtained by state transitions
                return False

        # Check if the final state after processing all symbols is one of the accept states
        return current_state in self.accept_states