import sys

def print_maturity(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a kiddo!")

if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)

print("The program was called with this parameters %s" % sys.argv[1:])
print("The first parameter is %s \n" % sys.argv[1])

