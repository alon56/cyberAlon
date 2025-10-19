"""
Author: Alon Fried

Program name:the compass

Description: A program that decrypt a msg and save's it in to a file or decrypt a mag from a file and print it to the user

Date:10/11/25
"""
import logging, argparse, os
from pathlib import Path
from functools import cached_property

FILE_NAME: str = "encrypted_msg_txt"

logger = logging.getLogger("Cipher")
logging.basicConfig(level=logging.DEBUG)
file_handler = logging.FileHandler("log.file")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') 
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


class CipherMessage():
    """
    A class that encrypt or decrypt a word by using a dict
    """
    CHAR_DELIMITER: str = ','

    @cached_property
    def cipher_table(self) -> dict:
        """
        Makes a dict

        :return: A dict based on the classroom assignment
        """
        return {
            '.': 100, 
            "'": 101,
            '!': 102,
            '-': 103,
            ' ': 98,
            ',': 99,
            'A': 56,
            'B': 57,
            'C': 58,
            'D': 59,
            'E': 40,
            'F': 41,
            'G': 42,
            'H': 43,
            'I': 44,
            'J': 45,
            'K': 46,
            'L': 47,
            'M': 48,
            'N': 49,
            'O': 60,
            'P': 61,
            'Q': 62,
            'R': 63,
            'S': 64,
            'T': 65,
            'U': 66,
            'V': 67,
            'W': 68,
            'X': 69,
            'Y': 10,
            'Z': 11,
            'a': 12,
            'b': 13,
            'c': 14,
            'd': 15,
            'e': 16,
            'f': 17,
            'g': 18,
            'h': 19,
            'i': 30,
            'j': 31,
            'k': 32,
            'l': 33,
            'm': 34,
            'n': 35,
            'o': 36,
            'p': 37,
            'q': 38,
            'r': 39,
            's': 90,
            't': 91,
            'u': 92,
            'v': 93,
            'w': 94,
            'x': 95,
            'y': 96,
            'z': 97
}


    @cached_property
    def revers_cipher_table(self) -> dict:
        """
        Makes a dict

        :return: A dict based on the classroom assignment just reversed
        """
        return {v: k for k, v in self.cipher_table.items()}


    def encrypt(self, msg: str) -> str:
        """
        Encrypts the given msg

        :param message: A msg that will be encrypted 
        :return: The msg encrypted
        """
        logger.info(f"Encrypting message: {msg}")
        encrypted_msg = self.CHAR_DELIMITER.join(str(self.cipher_table[c]) for c in msg)
        logger.info(f"Encrypted message: {encrypted_msg}")
        return encrypted_msg


    def decrypt(self, msg: str) -> str:
        """
        decrypt the given msg

        :param message: A msg that will be decrypted
        :return: The msg decrypted
        """
        if len(msg) == 0:
            logger.info("Message was empty")
            return ""
        else:
            logger.info(f"Decrypting message: {msg}")
            decrypted_msg = ''.join(self.revers_cipher_table[int(char_id)] for char_id in msg.split(self.CHAR_DELIMITER))
            logger.info(f"Got decrypted message: {decrypted_msg}")
            return decrypted_msg


def parse_args() -> argparse.Namespace:
    """
    Reads from the user the parameter that the program ran with

    :return: The instructions for the user
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "action",
        choices=[
            "encrypt",
            "decrypt"
        ],
        help = "chose what to with the provided msg"
    )
    
    return parser.parse_args()


def main():
    logger.info("Running cipher msg code")

    msg_cipher = CipherMessage()

    args = parse_args()

    if args.action.lower() == "encrypt":
        msg=input("Insert the msg you want to encrypt: ")
        with open(FILE_NAME,"w") as f:
            f.write(msg_cipher.encrypt(msg))
    elif args.action.lower() == "decrypt":
        try:
            with open(FILE_NAME,"r") as f:
                encrypted_msg = f.read()
            print(msg_cipher.decrypt(encrypted_msg))
        except FileNotFoundError:
            logger.info("file wasn't created")
            print("There was nothing to decrypt(file was empty)")
        

if __name__ == "__main__":

    assert_msg=CipherMessage()

    assert assert_msg.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.'!-") == "56,57,58,59,40,41,42,43,44,45,46,47,48,49,60,61,62,63,64,65,66,67,68,69,10,11,12,13,14,15,16,17,18,19,30,31,32,33,34,35,36,37,38,39,90,91,92,93,94,95,96,97,98,99,100,101,102,103"
    assert assert_msg.decrypt("56,57,58,59,40,41,42,43,44,45,46,47,48,49,60,61,62,63,64,65,66,67,68,69,10,11,12,13,14,15,16,17,18,19,30,31,32,33,34,35,36,37,38,39,90,91,92,93,94,95,96,97,98,99,100,101,102,103") == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.'!-"
    
    main()
