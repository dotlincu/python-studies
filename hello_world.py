__author__ = "Lincoln"

def main():
    # 
    print("Número:")
    n = int(input())
    for i in range(n):
        print("%d\n" % i)

    # concatenacao
    str_test = "hello" + "world"
    print(str_test)

    # uso de lista
    list_test = [1, 'ola']
    list_test.append('que estranho')
    print(list_test)

if __name__ == "__main__":
    main()