from Decoder import DecodeASecret
from Secret_Sharing import Secret


def main(secret):
    back_up_secret.append(secret)
    sectet = Secret(secret)
    decoder = DecodeASecret(sectet.lst_of_vectors, sectet.lst_of_teachers)
    return decoder.output(decoder.decode())
back_up_secret = []
#
# if __name__ == '__main__':
#     print(main("Hello"))
