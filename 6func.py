def changeTem(x):
    print(x*9/5+32)


if __name__ == "__main__":
    x = int(input())
    changeTem(x)
    print("If you want to exit,please enter 'N'")
    y = input()
    while y != 'N':
        x = int(input())
        changeTem(x)
        print("If you want to exit,please enter 'N'")
        y = input()
