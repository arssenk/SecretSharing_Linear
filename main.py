from Secret_Sharing import Secret
from Decoder import DecodeASecret

def main():

    sectet = Secret("Hello World")
    decoder = DecodeASecret(sectet.lst_of_vectors, sectet.lst_of_teachers)
    print(decoder.output(decoder.decode()))


if __name__ == '__main__':
    main()