class Grammar:
    def __init__(self, VN, VT, P, S):
        self.VN = VN
        self.VT = VT
        self.P = P
        self.S = S

    def eliminate_epsilon_productions(self):
        epsilon_productions = {non_term: [''] for non_term in self.VN}
        updated_productions = {}

        for non_term, productions in self.P.items():
            updated_productions[non_term] = []
            for production in productions:
                if production != '':
                    updated_productions[non_term].append(production)
                else:
                    epsilon_productions[non_term].append('')

        # Iterating until no new productions can be added
        while True:
            new_productions_added = False
            for non_term, productions in self.P.items():
                for production in productions:
                    for symbol in production:
                        if symbol in epsilon_productions:
                            # Productions without the epsilon symbol are added
                            new_productions = [production.replace(symbol, '') for production in epsilon_productions[symbol] if production != '']
                            new_productions_added = any(new_production not in updated_productions[non_term] for new_production in new_productions)
                            updated_productions[non_term].extend(new_production for new_production in new_productions if new_production not in updated_productions[non_term])

            # Update epsilon productions
            for non_term in epsilon_productions:
                epsilon_productions[non_term].extend(updated_productions[non_term])

            if not new_productions_added:
                break

        # Remove epsilon symbol from productions
        self.P = {non_term: [production.replace('', '') for production in productions if production != ''] for non_term, productions in updated_productions.items()}

    def eliminate_renaming(self):
        updated_productions = {}
        for non_term, productions in self.P.items():
            updated_productions[non_term] = []
            for production in productions:
                if len(production) > 1 or production[0] not in self.VN:
                    updated_productions[non_term].append(production)

        self.P = updated_productions

    def eliminate_inaccessible_symbols(self):
        reachable = set([self.S])
        updated_productions = {}
        for non_term, productions in self.P.items():
            updated_productions[non_term] = []
            if non_term in reachable:
                for production in productions:
                    for symbol in production:
                        if symbol in self.VN:
                            reachable.add(symbol)
                    updated_productions[non_term].append(production)

        self.P = updated_productions

    def eliminate_non_productive_symbols(self):
        productive = set()
        updated_productions = {}

        # Initialize productive symbols with terminals
        productive.update(self.VT)

        # Keep iterating until no new productive symbols are found
        while True:
            new_productions_added = False
            for non_term, productions in self.P.items():
                if non_term not in productive:
                    for production in productions:
                        if all(symbol in productive or symbol in self.VT for symbol in production):
                            productive.add(non_term)
                            new_productions_added = True
                            break

            if not new_productions_added:
                break

        # Filter productions to include only those with productive symbols
        for non_term, productions in self.P.items():
            updated_productions[non_term] = [production for production in productions if all(symbol in productive or symbol in self.VT for symbol in production)]

        self.P = updated_productions

    def obtain_cnf(self):
        self.eliminate_epsilon_productions()
        self.eliminate_renaming()
        self.eliminate_inaccessible_symbols()
        self.eliminate_non_productive_symbols()

        new_productions = {}
        production_count = 1

        for non_term, productions in self.P.items():
            new_productions[non_term] = []
            for production in productions:
                if len(production) > 2:
                    # Replace long productions with new non-terminals
                    remaining_symbols = production
                    while len(remaining_symbols) > 2:
                        print("Remaining symbols:", remaining_symbols)
                        new_non_term = f'N{production_count}'
                        print("New non-terminal:", new_non_term)
                        production_count += 1
                        new_productions[new_non_term] = [[remaining_symbols[0], remaining_symbols[1]]]
                        remaining_symbols = [new_non_term] + remaining_symbols[2:]

                    new_productions[non_term].append(remaining_symbols)
                else:
                    new_productions[non_term].append(production)

        # Update the productions
        self.P = new_productions

        # Output the CNF productions
        for non_term, productions in self.P.items():
            for production in productions:
                print(f"{non_term} -> {' '.join(production)}")

# Variant 8
VN = {'S', 'A', 'B', 'C'}
VT = {'a', 'd'}
P = {'S': ['dB', 'A'], 'A': ['d', 'dS', 'aAdAB'], 'B': ['a', 'aS', 'B', ''], 'C': ['Aa']}
S = 'S'

grammar = Grammar(VN, VT, P, S)
grammar.obtain_cnf()