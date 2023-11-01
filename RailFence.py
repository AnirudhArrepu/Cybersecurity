def encryption(key, string):
    encrypted = ""
    i = 0
    odd = True
    even = False
    arr = [["" for x in range(len(string))] for y in range(key)]
    for j in range(len(string)):
        if odd:
            arr[i][j] = string[j]
            i += 1
            if i == key - 1:
                odd = False
                even = True
                i = key - 1
        elif even:
            arr[i][j] = string[j]
            i -= 1
            if i == 0:
                odd = True
                even = False
                i = 0

    for i in range(key):
        for j in range(len(string)):
            encrypted += arr[i][j]
    return encrypted


def decryption(key, encrypted_string):
    arr = [["" in range(3)] in range(len(encrypted_string))]
    k = 0
    for i in range(3):
        for j in range(i, len(encrypted_string), 2 * key - 2):
            arr[i][j] = encrypted_string[k]
            k += 1
    i = 0
    odd = True
    even = False
    decrypted = ""
    for j in range(len(encrypted_string)):
        if odd:
            decrypted += arr[i][j]
            i += 1
            if i == key - 1:
                odd = False
                even = True
                i = key - 1
        elif even:
            decrypted += arr[i][j]
            i -= 1
            if i == 0:
                odd = True
                even = False
                i = 0
    return decrypted


input_text = input("ENCRYPTION: \n Enter text to be encrypted: ")
input_key = int(input("Enter key:"))
print("The encrypted message is: " + encryption(input_key, input_text))
input_text = input("DECRYPTION: \n Enter text to be decrypted: ")
input_key = int(input("Enter key"))
print("The decrypted message is: " + decryption(input_key, input_text))
