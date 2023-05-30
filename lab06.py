
def sine(x):

    k = 0

    def fact(n):
        if n < 2:
            return 1
        else:
            return n * fact(n - 1)

    while k < 10:

        k = k + 1

        f = fact(2*k+1)

        x = x + ((-1) ** k) * (x ** (1 + 2 * k)) / f

        print(x)




def collatz():

    print("Please type a number greater than one \nor ’quit’ to quit")

    n = input("Enter ")
    counter = 1

    if n == "q" or n == "Q":
        print("Goodbye!")
        quit()

    n = int(n)
    if n == 1 or n == 0:
        print("you typed 1, which is not greater than one")
    elif n > 1 :
        print("Giving Collatz sequence for", n )
        print("Iteration", counter, "results in", n, "\n")
        while n > 1:
            if n % 2 != 0:
                n = (3 * n + 1)
                counter  = counter + 1
                print("Iteration", counter, "results in", n, "\n")
            elif n % 2 == 0:
                n = (n // 2)
                counter  = counter + 1
                print("Iteration", counter, "results in", n, "\n")






