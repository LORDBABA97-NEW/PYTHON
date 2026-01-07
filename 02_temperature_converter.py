def f(n):
  return (n-32)*5/9
def c(n):
  return (n*9/5)+32
print('Please select 1 for fahrenheit to celsius and 2 for celsius to fahrenheit')
sel=int(input('select operation:'))
n=int(input('enter the number:'))
if sel==1:
  print(f(n))
elif sel==2:
  print(c(n))
else:
  print('invalid input')