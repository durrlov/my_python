#Sum of squares(without x)


def ss(x):
  sum = 0
  
  x = int(x)
  
  for i in range(x):
    sqr = i*i
    sum += sqr
  return(sum)

print('Enter a number')
x = input()
print(ss(x))

