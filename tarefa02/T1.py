def main():
    num1 = int(input("informe o seu numero 1!: "))
    num2 = int(input("informe o seu numero 2!: "))
    if num1 < num2:
        start, end=num2, num1
    else:
        start, end=num1, num2
    for num in range(start, end -1, -1):
        print(num)
if __name__=="__main__":
    main()