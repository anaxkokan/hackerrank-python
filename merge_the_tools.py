#https://www.hackerrank.com/challenges/merge-the-tools/problem
string = input()
k = int(input())

letters = [letter.upper() for letter in string if letter.isalpha()]
clean_word = ''.join(letters)

length = len(clean_word)
num_substrings = length // k

for i in range(num_substrings): 
    start = i*k
    end = start + k
    substring = clean_word[start:end]
    new_list = []

    for j in range(len(substring)):
        if substring[j] not in new_list:
            new_list.append(substring[j])
                
    print(''.join(new_list))