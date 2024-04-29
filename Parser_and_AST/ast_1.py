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

def plot_ast(root):
    def set_positions(node, x, y):
        node.x = x
        node.y = y
        if node.children:
            dx = 0.3 / len(node.children)
            for i, child in enumerate(node.children):
                set_positions(child, x + i * dx, y - 0.2)

    set_positions(root, 0.75, 0.8)

    def plot_node(node):
        plt.text(node.x, node.y, str(node), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
        if node.children:
            for child in node.children:
                plt.plot([node.x, child.x], [node.y, child.y], 'k-')
                plot_node(child)

    plt.figure(figsize=(8, 6))
    plot_node(root)
    plt.axis('off')  # Turn off axis display
    plt.show()