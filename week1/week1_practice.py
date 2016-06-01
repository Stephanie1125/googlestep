"""

First week's practice for Google STEP:
与えられてあ16文字からなるべく長い単語を出力するプログラムをつくろう！
Given 16 letters and try to find all words which len(word) > 8 that output from the combination of this 16 words.
Set the length limit in order to decrease the number of output

Example:
Input: aehmnooqqrrstzzz
Output:
astronomer
hoarstone
anorthose
resonator

"""


def create_lst(path):
    letter = []
    f = open(path, "r")
    for line in f.readlines():
        letter.append(line.strip())
    return letter


def counts(string):
    d = {}
    for c in string:
        d[c] = d.get(c, 0) + 1
    return d


def valid(input_str, word):
    input_lst = counts(input_str)
    word_lst = counts(word)
    for key in word_lst:
        if key not in input_lst:
            return False
        if word_lst[key] > input_lst[key]:
            return False
    return True


def main():
    input_str = input("please input a word:")
    letters = create_lst("/usr/share/dict/words")
    for word in letters:
        if valid(input_str, word):
            if len(word) > 8:
                print(word)


if __name__ == "__main__":
    main()

