import sys

def collatz(number):
    if number %2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
print('Enter the number:')
try:
    num = int(input())
except(ValueError):
    print("Should be integer")
    sys.exit()

while True:    
    if num == 1:
        break
    else:
        num = collatz(num)
    print(num)

print('-------')        
    
