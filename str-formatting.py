###Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary###

def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        
        print(i,end=" ")
        print(oct(i)[2:],end=" ")
        print(hex(i)[2:],end=" ")
        print(bin(i)[2:])
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
