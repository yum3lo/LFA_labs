from fa_to_grammar import RegularGrammar
from finite_automaton_class import FiniteAutomaton
from nfa_to_dfa import DFAConverter

# Define the finite automaton
Q = {'q0', 'q1', 'q2', 'q3', 'q4'}
Sigma = {'a', 'b'}
F = {'q3'}
delta = {
    'q0': {'a': {'q1'}},
    'q1': {'b': {'q1', 'q2'}},
    'q2': {'b': {'q0'}, 'a': {'q3'}},
    'q3': {'a': {'q4'}},
    'q4': {'a': {'q0'}},
}

finite_automaton = FiniteAutomaton(Q, Sigma, delta, 'q0', F)

# Instance of RegularGrammar and convert from finite automaton
regular_grammar = RegularGrammar()
regular_grammar.convert_from_fa(finite_automaton)

print("Regular Grammar:")
print("Non-terminals:", regular_grammar.VN)
print("Terminals:", regular_grammar.VT)
print("Production Rules:")
for state, production_rules in regular_grammar.P.items():
    for rule in production_rules:
        print(" ", rule)

#NFA or DFA
dfa_converter = DFAConverter(finite_automaton)
dfa_converter.convert_to_dfa()
dfa_converter.print_dfa_transitions()