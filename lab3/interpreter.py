def lexer(contents):
    # Split the contents of the file into a list of tokens
    # This way, when an error comes up, it's easier to tell where it is
    lines = contents.split("\n")
    lexemes_list = []

    for line in lines:
        lexemes = []
        token = ""
        in_quotes = False

        for char in line:
            if char in ['"', "'"]:
                in_quotes = not in_quotes
                token += char
            elif char == " " and not in_quotes:
                if token:
                    lexemes.append(token)
                    token = ""
            else:
                token += char

        if token:
            lexemes.append(token)

        line_lexemes = []
        for token in lexemes:
            if token.startswith('"') or token.startswith("'"):
                line_lexemes.append(("String", token))
            elif token in Symbols:
                line_lexemes.append(("Symbol", token))
            elif "=" in token:
                parts = token.split("=")
                variable = parts[0]
                value = parts[1]
                line_lexemes.append(("Variable", variable))
                line_lexemes.append(("String", value))

        lexemes_list.append(line_lexemes)

    return lexemes_list
    
Symbols = {
    "detect", 
    "recognize",
    "read_text",
    "read_text_lang",
    "train",
    "load",
    "generate_text",
    "retrieve_params",
    "recognize",
    "process",
    "transcribe",
    "convert"
}

Vars = {}

def parse(filename):
    with open(filename, "r") as f:
        contents = f.read()
    lines = lexer(contents)
    
    # Iterate over each line
    for line in lines:
        instr_line = ""
        for token in line:
            if token[0] == "Symbol":
                if token[1] in Symbols:
                    instr_line += token[1] + " "
            elif token[0] == "Variable":
                if len(line) > 1 and line[line.index(token) + 1][0] == "String":
                    Vars[token[1]] = line[line.index(token) + 1][1]
            else:
                # Error
                break
        # If there are no errors, print the instruction line
        else:
            print(instr_line)
    
    for line in lines:
        print(line)