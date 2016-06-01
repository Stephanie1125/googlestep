"""

This program is for practicing anagram:
Find anagram for only one word (no space)

Example input/output:
1.
input: sister
output: ['resist', 'restis', 'sister']
2.
input: smile
output: ['limes', 'slime', 'smile']

"""


# create a dictionary
# the key is the word with sorted letters and value is the word in this case
# example: {'aelpp': 'apple', 'ahppy': 'happy'}
def create_dict(path):
    letter = {}
    f = open(path, "r")
    for line in f.readlines():
        line = line.strip()
        key = sorted_word(line)
        if key in letter:
            value = letter.get(key) + "," + line
            letter[key] = value
        else:
            letter[key] = line
    return letter


# function for sorting the string
def sorted_word(word):
    s_word = sorted(word)
    return "".join(s_word)


def anagram(letter, word):
    key = sorted_word(word)
    values = letter.get(key, "NONE")
    return values.split(",")


def main():
    word = input("please input a word:")
    letter = create_dict("/usr/share/dict/words")
    results = anagram(letter, word)
    print(results)

if __name__ == "__main__":
    main()



