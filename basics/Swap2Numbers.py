
#swap without adding new variable
#n1=input('Enter first number:   ')
#n2=input('Enter second number:  ')
#n1, n2 = n2, n1
#print(n1, n2)3

#Swap with airthmetic operators
n1=int(input('Enter first number:   '))
n2=int(input('Enter second number:  '))
print('Old value of n1 is {0} and n2 is {1}'.format(n1,n2))
n1 = (n1+n2)
n2 = (n1-n2)
n1 = (n1-n2)
print('New value of n1 is {0} and n2 is {1}'.format(n1,n2))




