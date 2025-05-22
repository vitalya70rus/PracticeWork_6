symbol = 'c'
str = "aaa bbb c ccc ddd cc"

list_of_str = str.split()

count_words = 0
for word in list_of_str:
    if len(word) > 1:
        if word[0] == symbol and word[-1] == symbol:
            count_words += 1

print(count_words)