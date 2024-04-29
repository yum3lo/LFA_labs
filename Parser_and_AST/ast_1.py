import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class SymbolNode(Node):
    def __str__(self):
        return f"<SymbolNode {self.value}>"

class VariableNode(Node):
    def __str__(self):
        return f"<VariableNode {self.value}>"

class StringNode(Node):
    def __str__(self):
        return f"<StringNode {self.value}>"

def construct_ast(parsed_commands):
    # Initialize the root node
    root = None

    # Construct the AST
    for command in parsed_commands:
        symbol, details = command

        # Create nodes for the symbol and its details
        symbol_node = SymbolNode(symbol)
        variable_node = VariableNode(details[0][1])
        string_node = StringNode(details[1][1])

        # Link the nodes together
        symbol_node.add_child(variable_node)
        variable_node.add_child(string_node)

        # Set the root node if not set
        if root is None:
            root = symbol_node

    return root