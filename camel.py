def main():
    var_came = input("camelCase: ")
    var_snake = fromCameToSnake(var_came)
    print("snake_case:", var_snake)

def fromCameToSnake(var_name):
    for lether in var_name:
            camel = ""
            if lether.isupper():
                camel = camel + "_" + lether.lower()
            else:
                camel = camel + lether
    return camel

main()