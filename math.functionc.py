def welcome():
    """Welcome function"""
if __name__ == "__main__":
    welcome()
    print("Welcome to the algorithmic functions library!")
def factorial(n):
    """Function for factorial"""
    if n==1 or n ==0:
        return 1
    return n* factorial(n-1)
if __name__ == "__main__":
    factorial(5)


