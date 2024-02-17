import random

class Grammar:
    def __init__(self):
        self.variables = {'S', 'D', 'E', 'J'}
        self.terminals = {'a', 'b', 'c', 'd', 'e'}
        self.productions = {
            'S': ['aD'],
            'D': ['dE', 'bJ', 'aE'],
            'J': ['cS'],
            'E': ['e', 'aE']
        }

    def generate_string(self, variable, depth=0):
        if depth > 10:  # To avoid infinite recursion
            return ""

        if variable not in self.variables:
            return variable

        production = random.choice(self.productions[variable])
        string = ""
        for symbol in production:
            string += self.generate_string(symbol, depth+1)
        return string

    def generate_valid_strings(self, num_strings):
        valid_strings = []
        for _ in range(num_strings):
            valid_strings.append(self.generate_string('S'))
        return valid_strings

if __name__ == "__main__":
    grammar = Grammar()
    generated_strings = grammar.generate_valid_strings(5)
    print("Generated Strings:")
    for string in generated_strings:
        print(string)
