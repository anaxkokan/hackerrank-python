#https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    x = len(s)
    my_list = []
    
    for i in range(x):
      if i == 0:
          letter = s[i].upper()
      elif s[(i-1)].isspace():
          letter = s[i].upper()
      else:
        letter = s[i]
    
      my_list.append(letter)
        
    return ''.join(my_list)
    
       
