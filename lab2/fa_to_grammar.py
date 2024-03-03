class RegularGrammar:
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def convert_to_regular_grammar(self):
        non_terminals = [f'Q_{state}' for state in self.Q] + ['Q_F']
        terminals = list(self.sigma)

        # Production rules
        rules = {}

        # Add epsilon production from initial state to start symbol
        rules['S'] = ['']  # S is the start symbol
        for state in self.Q:
            if state == self.q0:
                rules['S'].append(f'Q_{state}')

            if state in self.delta:
                for symbol in self.delta[state]:
                    for next_state in self.delta[state][symbol]:
                        if next_state in self.F:
                            # If the next state is final, add the terminal symbol only
                            production = symbol
                        else:
                            # Otherwise, add the next state as well
                            production = f'{symbol}Q_{next_state}'

                        # Add the production rule
                        if f'Q_{state}' not in rules:
                            rules[f'Q_{state}'] = [production]
                        else:
                            rules[f'Q_{state}'].append(production)

        return Grammar(non_terminals, terminals, rules, start='S')