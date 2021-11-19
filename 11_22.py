list_of_words = input()
word_split = list_of_words.split()

for word in word_split:
        print(word,word_split.count(word))

