class Lexer:
    def __init__(self):
        self.symbols = {
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
        self.vars = {}

    def tokenize(self, contents):
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
                elif token in self.symbols:
                    line_lexemes.append(("Symbol", token))
                elif "=" in token:
                    parts = token.split("=")
                    variable = parts[0]
                    value = parts[1]
                    line_lexemes.append(("Variable", variable))
                    line_lexemes.append(("String", value))

            lexemes_list.append(line_lexemes)

        return lexemes_list

    def parse(self, filename):
        with open(filename, "r") as f:
            contents = f.read()
        lines = self.tokenize(contents)
        
        # Iterate over each line
        for line in lines:
            instr_line = ""
            for token in line:
                if token[0] == "Symbol":
                    if token[1] in self.symbols:
                        instr_line += token[1] + " "
                elif token[0] == "Variable":
                    if len(line) > 1 and line[line.index(token) + 1][0] == "String":
                        self.vars[token[1]] = line[line.index(token) + 1][1]
                else:
                    # Error
                    break
            # If there are no errors, print the instruction line
            else:
                print(instr_line)
        
        for line in lines:
            print(line)