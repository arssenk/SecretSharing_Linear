from Secret_Sharing import Secret
from Decoder import DecodeASecret

def main():

    sectet = Secret("Hallo bastards, i'm back! And i am after you!")
    decoder = DecodeASecret(sectet.lst_of_vectors, sectet.lst_of_teachers)
    print(decoder.output(decoder.decode()))


if __name__ == '__main__':
    main()