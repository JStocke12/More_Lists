def sum_of_odd_nums(n):
    return sum([i for i in range(n*2) if i%2==1])

def caesar_cipher(message, key):
    return ''.join([chr(ord(i)+key) for i in message])

def fizzbuzz(n):
    return [("fizz"*(i%3==0)+"buzz"*(i%5==0)+"!").capitalize() if (i%3==0) or (i%5==0) else i for i in range(1,n+1)]

def main():
    print('Table of the sum for the first n odd numbers:')
    print('n\tsum')
    print('-'*16)
    for n in range(10):
        print('{}\t{}'.format(n, sum_of_odd_nums(n)))

    print()

    ciphertext = "Frpsxwhu#Vflhqfh#lv#qr#pruh#derxw#frpsxwhuv#wkdq#dvwurqrp|#lv#derxw#whohvfrshv1"
    print(caesar_cipher(ciphertext, -3))

    print()

    for i in fizzbuzz(25):
        print(i)

if __name__ == '__main__':
    main()
