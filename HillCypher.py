def getasciicode(char):
    t = ord(char) - 65
    return t

def encryption(string, key):
    n = len(string)
    key_array = [[0 for i in range(n)] for j in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            key_array[i][j] = getasciicode(key[k])
            k += 1
    string_array = [getasciicode(string[i]) for i in range(n)]
    output_array = [0 for i in range(n)]
    for i in range(n):
        sum_output = 0
        for j in range(n):
            sum_output += key_array[i][j] * string_array[j]
        output_array[i] = sum_output % 26 + 65

    for i in range(n):
        print(chr(output_array[i]), end="")

    return ""

def decryption(string, key):
    