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


def tokenize(line):
    token = {}
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
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    # Deal with the multiplication and division part first
    while index != len(tokens):
        index = 1
        while index < len(tokens):
            if tokens[index]["type"] in {"MUL", "DIV"}:
                temp = 0
                if tokens[index]["type"] == "MUL":
                    temp = tokens[index-1]["number"] * tokens[index + 1]["number"]
                else:
                    temp = tokens[index-1]["number"] / tokens[index + 1]["number"]
                tokens[index-1:index+2] = [{"type":"NUMBER","number":temp}]
                break
            index += 1
    # Deal with the addition and subtraction part
    for i in xrange(1, len(tokens)):
        if tokens[i]["type"] == "NUMBER":
            if tokens[i-1]["type"] == "PLUS":
                answer += tokens[i]["number"]
            else:
                answer -= tokens[i]["number"]
    return answer


while True:
    print '> ',
    line = raw_input()
    if line == 'q':
        break
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %f\n" % answer
