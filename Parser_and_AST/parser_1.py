from lexer import Lexer
from ast_1 import *

class Parser:
    def __init__(self):
        self.instructions = []

    def parse(self, lexemes_list):
        for line_lexemes in lexemes_list:
            if len(line_lexemes) < 2:
                # Invalid syntax, skip this line
                continue

            # Extracting the instruction type (Symbol) and its arguments (Variable and String)
            instruction = line_lexemes[0][1]
            arguments = []
            for token in line_lexemes[1:]:
                if token[0] == "Variable":
                    arguments.append(("Variable", token[1]))
                elif token[0] == "String":
                    arguments.append(("String", token[1]))

            # Storing the instruction and its arguments as a tuple
            self.instructions.append((instruction, arguments))

    def get_instructions(self):
        return self.instructions


if __name__ == "__main__":
    lexer = Lexer()
    parser = Parser()

    # Get input from the console
    print("Enter your commands (press Enter after each command):")
    inputs = []
    while True:
        line = input().strip()
        if not line:
            break
        inputs.append(line)

    # Tokenize the input
    lexemes_list = lexer.tokenize("\n".join(inputs))

    # Parse the input
    parser.parse(lexemes_list)

    # Get the parsed instructions
    instructions = parser.get_instructions()
    for instruction in instructions:
        print("Parsed command:", instruction)

        # Convert the parsed instruction tuple into a simple AST
        symbol_node = SymbolNode(instruction[0])
        variable_node = None
        for arg_type, arg_value in instruction[1]:
            if arg_type == "Variable":
                variable_node = VariableNode(arg_value)
                symbol_node.add_child(variable_node)
            elif arg_type == "String" and variable_node:
                string_node = StringNode(arg_value)
                variable_node.add_child(string_node)

        # Print the AST
        print("AST:")
        print(symbol_node)
        for child in symbol_node.children:
            print(f"└── {child}")
            for sub_child in child.children:
                print(f"    └── {sub_child}")