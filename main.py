from Decoder import DecodeASecret
from Secret_Sharing import Secret


def main():
    sectet = Secret("Hellosssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    decoder = DecodeASecret(sectet.lst_of_vectors, sectet.lst_of_teachers)
    print(decoder.output(decoder.decode()))


if __name__ == '__main__':
    main()
