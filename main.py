from Secret_Sharing import Secret
from Decoder import DecodeASecret

def main():

    sectet = Secret("H")
    decoder = DecodeASecret(sectet.lst_of_vectors, sectet.lst_of_teachers)
    decoder.decode()


if __name__ == '__main__':
    main()