class RegularGrammar:
    def __init__(self):
        self.VN = set()
        self.VT = set()
        self.P = {}

    def convert_from_finite_automaton(self, finite_automaton):
        # Add non-terminals for each state in the finite automaton
        self.VN.update(finite_automaton.states)

        # Add terminals from the finite automaton's alphabet
        self.VT.update(finite_automaton.alphabet)

        # Add production rules for each transition in the finite automaton
        for state, transitions in finite_automaton.transitions.items():
            for symbol, next_state in transitions.items():
                # Create production rule for the transition
                production_rule = f"{state} -> {symbol}{next_state}"
                # Add the production rule to the regular grammar
                self.P.setdefault(state, []).append(production_rule)