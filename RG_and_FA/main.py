from grammar_class import Grammar

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