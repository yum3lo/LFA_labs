import re

class ASTNode:
    def __init__(self, operation):
        self.operation = operation
        self.attributes = {}

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def __str__(self):
        attributes_str = ', '.join([f"{key}={value}" for key, value in self.attributes.items()])
        return f"{self.operation}({attributes_str})"

def parse_input_file(filename):
    file_path = "D:\\LFA_labs\\LexerScanner\\" + filename
    with open(file_path, "r") as file:
        contents = file.read()
    ast_nodes = parse_input(contents)
    return ast_nodes

def parse_input(input_text):
    ast_nodes = []
    lines = input_text.split('\n')
    for line in lines:
        operation, attributes_str = re.match(r'(\w+)\s+(.*)', line).groups()
        attributes = dict(re.findall(r'(\w+)="([^"]+)"', attributes_str))
        node = ASTNode(operation)
        for key, value in attributes.items():
            node.add_attribute(key, value)
        ast_nodes.append(node)
    return ast_nodes

def print_ast(ast_nodes):
    for node in ast_nodes:
        print(node)

ast_nodes = parse_input_file('test.txt')
print_ast(ast_nodes)