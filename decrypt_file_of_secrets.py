#!/usr/bin/python3

from Crypto.Cipher import DES3
from codecs import decode
from sys import argv



def decrypt(input):
  ciphertext = input
  # fixed decryption key
  key_signed_byte_array = [61, 22, 11, 57, 110, 89, -20, -1, 0, 99, 111, -120, 55, 4, -9, 10, 11, 45, 71, -89, 21, -99, 54, 51]
  key_byte_array = [ b & 0xff for b in key_signed_byte_array ]
  key = bytes(key_byte_array)
  # decrypt ciphertext
  des3_ciphertext = ciphertext.lstrip('zxx')
  des3_cipherbytes = decode(des3_ciphertext, 'hex')
  # create cipher
  cipher = DES3.new(key, DES3.MODE_ECB)
  # decrypt
  plaintext_padded = cipher.decrypt(des3_cipherbytes)
  # remove padding
  plaintext = plaintext_padded[:-plaintext_padded[-1]]
  # return plaintext
  return(plaintext.decode('utf-8'))


def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            processed_line = decrypt(line.strip())
            with open('output.txt', 'a') as output_file:
                output_file.write(processed_line + '\n')

# decrypts the ciphertext
file_path = "./keys.txt"
process_file(file_path)
