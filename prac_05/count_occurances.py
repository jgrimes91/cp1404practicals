words = {}
text = input("Please enter some words: ")
word_list = text.split(" ")
for word in word_list:

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

length = max(len(word) for word in words)
print(length)


for word in sorted(words.keys()):

    print("{:{}}: {}".format(word, length, words[word]))