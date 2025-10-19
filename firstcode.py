#“””

#Author:alon fried

#Program name:the compass

#Description: A program that decrypt a mesage and save's it in to a file or decrypt a measage from a file and print it to the user

#Date:10/11/25

#“””
import sys

#מילון רגיל: האות זה המפתחת המספר הערך
cipher_table={
    '.': 100,"'": 101,'!': 102,
    '-': 103,' ': 98,',': 99,
    'A': 56, 'B': 57, 'C': 58, 'D': 59, 'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44,
    'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 60, 'P': 61, 'Q': 62, 'R': 63, 'S': 64, 'T': 65, 'U': 66, 'V': 67, 'W': 68, 'X': 69, 'Y': 10, 'Z': 11,
    'a': 12, 'b': 13, 'c': 14, 'd': 15, 'e': 16, 'f': 17, 'g': 18, 'h': 19, 'i': 30, 'j': 31, 'k': 32, 'l': 33, 'm': 34, 'n': 35, 'o': 36, 'p': 37, 'q': 38,
    'r': 39, 's': 90, 't': 91, 'u': 92, 'v': 93, 'w': 94, 'x': 95, 'y': 96, 'z': 97
}


# מילון שני: המספר הוא המפתח, האות/סימן הוא הערך
revers_cipher_table= {v: k for k, v in cipher_table.items()}


# functions
def encrypt():
    measage = input("enter measage to encrypt: ")
    encrpted_measage=','.join(str(cipher_table[c]) for c in measage) #נצפין את ההודעה שהתקבלה
    with open("msg_encrypted.txt", "w") as f:
        f.write(encrpted_measage) 
#--------------------------------------------------------------------
#פונקציה ששומרת בקובץ את ההצפנה של ההודעה שהמשתמש הכניס בה
#--------------------------------------------------------------------

def decrypt():
    with open("msg_encrypted.txt", "r") as f: 
        encrpted_measage=f.read() 
    if len(encrpted_measage) == 0:
        print(encrpted_measage)
    else:
        decrypted_measage = ''.join( revers_cipher_table[int(num)] for num in encrpted_measage.split(',')) #נמיר את המספרים להודעה
        print(decrypted_measage) 
#--------------------------------------------------------------------
#פוקנציה שמדפיסה למשתמש את הפיענוח של הקובץ המוצפן
#--------------------------------------------------------------------


def main():
#--------------------------------------------------------------------
#טיפול במצב שלא הכניסו פרמטר בתחילת הקוד
#--------------------------------------------------------------------
    if len(sys.argv) < 2:
        print("need to insert:encrypt or decrypt ")
        sys.exit()

#--------------------------------------------------------------------
#הצפנת הודעה והעברה לקובץ 
#--------------------------------------------------------------------
    elif sys.argv[1].lower() == "encrypt":
         encrypt()

#--------------------------------------------------------------------
#פיענוח הודעה והדפסה למסך
#--------------------------------------------------------------------
    elif sys.argv[1] == "decrypt":
        decrypt()

#--------------------------------------------------------------------
#מצב לא חוקי(המשתמש לא הזין להצפין או מוצפן)
#--------------------------------------------------------------------
    else:
        print("Ilegal parmeater need to insert:encrypt or decrypt ")
        

if __name__ == "__main__":   
    main()