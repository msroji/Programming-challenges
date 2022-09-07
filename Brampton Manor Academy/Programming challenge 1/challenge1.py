def add(numlist):
    sum = 0
    for i in range(len(numlist)):
        sum+= int(numlist[i])
    return sum

def main():
    numlist = input("Enter list of integers using spaces")
    numlist = numlist.split()
    print(add(numlist))
    
if __name__ == '__main__':
    main()
