n = input('Enter any number: ')
def main():
    prime(n)

def prime(n):
    if(n>1):
        for i in range(2, int(n/2)+1):
            if(n % i)==0:
                print(n,'it is not prime number')
                break;
            else:
                print(n, 'it is a prime number')
    else:
        print(n,'it is not a prime number')


if __name__ == "__main__":
    main()
