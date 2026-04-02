def main():
    x = int(input("x : "))
    y = int(input("y : "))

    print("%d + %d = %d" %(x, y, add(x,y)))

def add(x,y):
    return x + y

if __name__ == "__main__":
    main()