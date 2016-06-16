def read_num(line, index):
    number = 0.0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_mul(index):
    token = {'type': 'MUL'}
    return token, index + 1


def read_div(index):
    token = {'type': 'DIV'}
    return token, index + 1


def read_lpar(index):
    token = {'type': 'LPAR'}
    return token, index + 1


def read_rpar(index):
    token = {'type': 'RPAR'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_num(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(index)
        elif line[index] == '-':
            (token, index) = read_minus(index)
        elif line[index] == 'x':
            (token, index) = read_mul(index)
        elif line[index] == '/':
            (token, index) = read_div(index)
        elif line[index] == '(':
            (token, index) = read_lpar(index)
        elif line[index] == ')':
            (token, index) = read_rpar(index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


# for doing the calculation
def calculate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
    index = 1
    while index != len(tokens):
        index = 1
        while index < len(tokens):
            if tokens[index]["type"] in {"MUL", "DIV"}:
                temp = 0
                if tokens[index]["type"] == "MUL":
                    temp = tokens[index - 1]["number"] * tokens[index + 1]["number"]
                else:
                    temp = tokens[index - 1]["number"] / tokens[index + 1]["number"]
                tokens[index - 1:index + 2] = [{"type": "NUMBER", "number": temp}]
                break
            index += 1
    for i in xrange(1, len(tokens)):
        if tokens[i]["type"] == "NUMBER":
            if tokens[i - 1]["type"] == "PLUS":
                answer += tokens[i]["number"]
            else:
                answer -= tokens[i]["number"]
    return answer


def evaluate(tokens):
    stack = []
    rpar_index = None
    tokens.insert(0, {'type': 'PLUS'})
    while tokens:
        new_item = tokens.pop()
        stack.append(new_item)
        if new_item["type"] == 'RPAR':
            rpar_index = len(stack) - 1
        elif new_item["type"] == "LPAR":
            lpar_index = len(stack) - 1
            calculate_part = stack[rpar_index + 1:lpar_index]
            calculate_part.reverse()
            temp_result = calculate(calculate_part)
            tokens.append({'type': 'NUMBER', 'number': temp_result})
            for i in xrange(rpar_index - 1, -1, -1):
                tokens.append(stack[i])
            stack = []
    if stack:
        while stack:
            tokens.append(stack.pop())
    return calculate(tokens)


while True:
    print '> ',
    line = raw_input()
    if line == 'q':
        break
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %f\n" % answer
