from random import *


def main():
    standard = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z"
    ]
    encrypted = []  # initializing arrays
    encrypted_text = []
    encryption = []
    encrypted_message = []
    decrypted_text = []

    def encrypt():
        generator = [i for i in range(26)]
        shuffle(generator)
        for nano in generator:
            encrypted.append(standard[nano])

    # generates random numbers to randomize letter combination

    def capitalize_all(original_word):
        charlie = ""
        for el in original_word:
            charlie = charlie + el.capitalize()
        return charlie

    # capitalizes all letters in a string or array

    def algorithm(bitch):
        if bitch == 'A':
            encrypted_text.append(encrypted[0])
        if bitch == 'B':
            encrypted_text.append(encrypted[1])
        if bitch == 'C':
            encrypted_text.append(encrypted[2])
        if bitch == 'D':
            encrypted_text.append(encrypted[3])
        if bitch == 'E':
            encrypted_text.append(encrypted[4])
        if bitch == 'F':
            encrypted_text.append(encrypted[5])
        if bitch == 'G':
            encrypted_text.append(encrypted[6])
        if bitch == 'H':
            encrypted_text.append(encrypted[7])
        if bitch == 'I':
            encrypted_text.append(encrypted[8])
        if bitch == 'J':
            encrypted_text.append(encrypted[9])
        if bitch == 'K':
            encrypted_text.append(encrypted[10])
        if bitch == 'L':
            encrypted_text.append(encrypted[11])
        if bitch == 'M':
            encrypted_text.append(encrypted[12])
        if bitch == 'N':
            encrypted_text.append(encrypted[13])
        if bitch == 'O':
            encrypted_text.append(encrypted[14])
        if bitch == 'P':
            encrypted_text.append(encrypted[15])
        if bitch == 'Q':
            encrypted_text.append(encrypted[16])
        if bitch == 'R':
            encrypted_text.append(encrypted[17])
        if bitch == 'S':
            encrypted_text.append(encrypted[18])
        if bitch == 'T':
            encrypted_text.append(encrypted[19])
        if bitch == 'U':
            encrypted_text.append(encrypted[20])
        if bitch == 'V':
            encrypted_text.append(encrypted[21])
        if bitch == 'W':
            encrypted_text.append(encrypted[22])
        if bitch == 'X':
            encrypted_text.append(encrypted[23])
        if bitch == 'Y':
            encrypted_text.append(encrypted[24])
        if bitch == 'Z':
            encrypted_text.append(encrypted[25])
        if bitch == "a":
            encrypted_text.append(encrypted[0])
        if bitch == 'b':
            encrypted_text.append(encrypted[1])
        if bitch == 'c':
            encrypted_text.append(encrypted[2])
        if bitch == 'd':
            encrypted_text.append(encrypted[3])
        if bitch == 'e':
            encrypted_text.append(encrypted[4])
        if bitch == 'f':
            encrypted_text.append(encrypted[5])
        if bitch == 'g':
            encrypted_text.append(encrypted[6])
        if bitch == 'h':
            encrypted_text.append(encrypted[7])
        if bitch == 'i':
            encrypted_text.append(encrypted[8])
        if bitch == 'j':
            encrypted_text.append(encrypted[9])
        if bitch == 'k':
            encrypted_text.append(encrypted[10])
        if bitch == 'l':
            encrypted_text.append(encrypted[11])
        if bitch == 'm':
            encrypted_text.append(encrypted[12])
        if bitch == 'n':
            encrypted_text.append(encrypted[13])
        if bitch == 'o':
            encrypted_text.append(encrypted[14])
        if bitch == 'p':
            encrypted_text.append(encrypted[15])
        if bitch == 'q':
            encrypted_text.append(encrypted[16])
        if bitch == 'r':
            encrypted_text.append(encrypted[17])
        if bitch == 's':
            encrypted_text.append(encrypted[18])
        if bitch == 't':
            encrypted_text.append(encrypted[19])
        if bitch == 'u':
            encrypted_text.append(encrypted[20])
        if bitch == 'v':
            encrypted_text.append(encrypted[21])
        if bitch == 'w':
            encrypted_text.append(encrypted[22])
        if bitch == 'x':
            encrypted_text.append(encrypted[23])
        if bitch == 'y':
            encrypted_text.append(encrypted[24])
        if bitch == 'z':
            encrypted_text.append(encrypted[25])
        if bitch == " ":
            encrypted_text.append(" ")

    # finds encrypted letter that matches input and adds it to the array encrypted text

    def read_array(array):
        key = ""
        for read in array:
            key = (key + read)
        return key

    # reads out arrays and lists

    def make_array(whatever, array_maker):
        for anti in whatever:
            array_maker.append(anti)
        return array_maker

    # turns whatever into a list or array_maker

    def print_blank(y):
        x = 0
        while x < y:
            print("")
            x = (1 + x)

    # prints y blank lines

    def restart():
        start = input("To restart press enter")
        if start == "":
            return main()
        else:
            return

    # gives restart parameters

    def decimal_to_binary(n):
        return bin(n).replace("0b", "")

    # turns decimal to binary

    def binary_to_decimal(n):
        return int(n, 2)

    # turns binary to decimal

    openfile = input("Type New to open a new file or Existing to use an existing file (hit enter it skip): ")
    open_seg = capitalize_all(openfile)
    if open_seg == "":
        print("*NO FILE*")
    elif open_seg[0] == "N" or open_seg[0] == "E":
        file_title = input("Input title here:  ")
    nova = int()
    password = input("Please enter password here: ")
    # input password for encryption

    for value in password:
        nova = (ord(value) + nova)
    # adds up ASCII values of each letter in password

    print("Would you like to encrypt or decrypt messages?")
    print("please input Encrypt or Decrypt")
    cyphers = input("Choose cypher mode here:  ")
    # choose to encrypt or decrypt

    capitalized = capitalize_all(cyphers)

    if capitalized[0] == "D":  # decrypt

        if open_seg == "":
            code = input("Please enter encryption key now:  ")
            message = input("Please enter encrypted message now:  ")

        elif open_seg[0] == "E":
            file = open(file_title, "r")
            verify = file.read()
            test = verify.index(":")
            test += 1
            gate = verify.index("x")
            binaryCode = (gate - 12)
            messageCode = (gate + 3)
            code = verify[test:binaryCode]
            message = verify[messageCode:]
            file.close()
        reverseit = []
        code = code.strip()
        mes = message.strip()
        me = capitalize_all(mes)
        word = ""
        for kappa in code:
            if kappa == " ":
                reverseit.append(word)
                word = ""
            else:
                word = (word + kappa)
        reverseit.reverse()
        for theta in reverseit:
                king = binary_to_decimal(theta)  # takes each set of binary(word) and turns them into decimal
                solved = int(king / nova)  # divide binary value by password value to get decryption key letter value
                data = chr(solved)  # get letter
                print(data)
                encryption.append(data)

        make_array(me, encrypted_message)
        encrypted_message.reverse()

        for index in encrypted_message:
            zeta = 0
            if index == " ":
                decrypted_text.append(" ")
            for alpha in encryption:
                if index == alpha:
                    decrypted_text.append(standard[zeta])
                zeta = (zeta + 1)
        decrypted_done = read_array(decrypted_text)

        samefile = input("To save decryption in file type Yes:")
        files = capitalize_all(samefile)
        if files == "":
            print("*NOT SAVING*")
        elif files[0] == "Y":
            if open_seg[0] == "E" or open_seg[0] == "N":
                file = open(file_title, "a")
                file.write("Decrypted Text: ")
                file.write(decrypted_done)
                file.close()

        print(decrypted_done)
        print_blank(3)

    if capitalized[0] == "E":
        text = input("Enter plain text here:  ")
        encrypt()
        num_array = []

        for bit in text:
            zed = bit
            algorithm(bitch=zed)
        print(encrypted)
        encrypted_text.reverse()
        encrypted.reverse()

        for num in encrypted:
            delta = (ord(num) * nova)
            num_array.append(delta)
        half = ""

        for gamma in num_array:
            omega = "% s" % decimal_to_binary(gamma)
            half = (half + omega + " ")

        encrypting = read_array(encrypted_text)

        samefile = input("To save encryption in file type Yes (press enter to skip): ")
        files = capitalize_all(samefile)
        if files == "":
            print("*NOT SAVING*")
        elif files[0] == "Y":
            if open_seg[0] == "R" or open_seg[0] == "N":
                file = open(file_title, "a")
                file.write("Encryption Key: ")
                file.write(half)
                file.write("Encrypted Text:     ")
                file.write(encrypting)
                file.close()

        print(half)
        print(encrypting)
        print_blank(3)

    restart()


main()
