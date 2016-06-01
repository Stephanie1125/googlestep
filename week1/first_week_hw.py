"""

First week's homework for Google STEP:
与えられてあ16文字からなるべく長い単語を出力するプログラムをつくろう！
Given 16 letters and try to output the longest word using 16 letters.

Example:
Input: aehmnooqqrrstzzz
Output: astronomer

"""


# build a dict using the path in the computer which key and value are same word
# example: {'apple':'apple','happy':'happy'}
def create_dict(path):
    letter = {}
    f = open(path, "r")
    for line in f.readlines():
        line = line.strip()
        key = line
        letter[key] = line
    return letter


# create a dictionary that can count the numbers of letters in the word
# example: apple -> {a:1, p:2, l:1, e:1} is built
def count(input_str):
    d = {}
    for c in input_str:
        try:
            d[c] += 1
        except:
            d[c] = 1
    return d


# valid function for checking if the input string is satisfied as a valid output
# check if the word/letters in word_dictionary also contain in the input_dictionary
# example: if input is aehmnooqqrrstzzz, astronomer will be a valid output (return True)
def valid(input_str, word):
    input_dict = count(input_str)
    word_dict = count(word)
    for key in word_dict:
        if key not in input_dict:
            return False
        if word_dict[key] > input_dict[key]:
            return False
    return True


# find the longest word in all the valid words
def anagram(input_str, dictionary):
    answer = ""
    for word in dictionary:
        if valid(input_str, word):
            answer = word if len(word) > len(answer) else answer
    return answer


def main():
    word = input("please input:")
    letters = create_dict("/usr/share/dict/words")
    answer = anagram(word, letters)
    print("longest word:", answer)

if __name__ == "__main__":
    main()

