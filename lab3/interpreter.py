def lexer(contents):
    # Split the contents of the file into a list of tokens
    # This way, when an error comes up, it's easier to tell where it is
    lines = contents.split("\n")
    for line in lines:
        chars = list(line)
        
        tokens = []
        temp_str = ""
        for char in chars:
            if char == " ":
                tokens.append(temp_str)
                temp_str = ""
            else:
                temp_str += char
        tokens.append(temp_str)
        print(tokens)
    

def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens