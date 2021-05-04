#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(s):
    
    letters = [letter for letter in s if letter.isalpha()]
    clean_word = ''.join(letters)
    length = len(clean_word)
    vowels = 'AEIOU'
  
    points_vowels = 0
    points_consonants = 0

    for start in range(length):
        if clean_word[start] in vowels:
            points_vowels += (length - start)
        else:
            points_consonants += (length - start)
    

    if points_vowels > points_consonants:
      print('Kevin', points_vowels)
    elif points_vowels < points_consonants:
      print('Stuart', points_consonants)
    else:
      print('Draw')


s = input()
minion_game(s)