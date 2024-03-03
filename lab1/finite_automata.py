import random

class Grammar:
    def __init__(self):
        self.VN = {'S', 'D', 'E', 'J'}
        self.VT = {'a', 'b', 'c', 'd', 'e'}
        self.P = {
            'S': ['aD'],
            'D': ['dE', 'bJ', 'aE'],
            'J': ['cS'],
            'E': ['e', 'aE']
        }

    def generate_string(self, symbol=None, length=0, max_length=15):
        # If no symbol is provided, start from the initial state
        if symbol is None:
            symbol = 'S'

        if length > max_length:
            return ''

        # If the current symbol is a terminal, it returns it
        if symbol in self.VT:
            return symbol

        # Otherwise, it generates a string for each production of the current symbol
        production = random.choice(self.P.get(symbol, []))
        generated_string = ''
        for s in production:
            generated_string += self.generate_string(s, length + 1, max_length)
        return generated_string
    
    def classify_grammar(self):
        # Determine if the grammar is regular, context-free, context-sensitive, or unrestricted

        # Check if all production rules are of the form A -> a or A -> aB where 'a' is a terminal and 'B' is a non-terminal
        is_regular = all(len(self.P[non_terminal]) == 1 and (len(self.P[non_terminal][0]) == 1 or (len(self.P[non_terminal][0]) == 2 and self.P[non_terminal][0][1] in self.VN)) for non_terminal in self.P)

        # Check if it's not regular but each production rule has only one non-terminal on the left-hand side
        is_context_free = not is_regular and all(len(production) == 1 or (len(production) == 2 and production[1] in self.VN) for production in self.P)

        # Check if it's not context-free but each production rule can rewrite any string of terminals and non-terminals
        is_context_sensitive = not is_context_free and all(len(production) <= len(replacement) for production, replacement in self.P.items())

        # If none of the above conditions are met, it's an unrestricted grammar
        return "This grammar is " + \
       ("Unrestricted " if not is_regular and not is_context_free and not is_context_sensitive else "") + \
       ("Context-Sensitive " if is_context_sensitive else "") + \
       ("Context-Free " if is_context_free else "") + \
       ("Regular" if is_regular else "")

        
    def convert_to_fa(self):
        # Initializes the transitions dictionary and the final state
        transitions = {}
        final_state = 'DEAD'

        # Initializes transitions for each non-terminal
        for non_terminal in self.VN:
            transitions[non_terminal] = {}

        # Adds transitions for each production
        for non_terminal, productions in self.P.items():
            for production in productions:
                # If the length of the current production is 1 and it's a terminal, add a transition to the final state
                if len(production) == 1 and production[0] in self.VT:
                    transitions[non_terminal][production] = final_state
                else:
                    # Otherwise, add a transition to the new state defined by the production
                    transition, new_state = production[0], production[1]
                    transitions[non_terminal][transition] = new_state

        return FiniteAutomaton(
            states=self.VN.union({final_state}),
            alphabet=self.VT,
            transitions=transitions,
            initial_state='S',
            accept_states={final_state}
        )

class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = accept_states

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