def encypt_func(Plain_txt, s):
    result = ""
    # transverse the plain txt
    for i in range(len(Plain_txt)):
        char = Plain_txt[i]
        # encypt_func uppercase characters in plain txt
        if (char.isupper()):
            result += chr((ord(char) + s - 64) % 26 + 65)
            # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) + s - 96) % 26 + 97)
    return result

Plain_txt = input("Enter Plain Text:")
s= int(input("Enter Encypt_key:"))
print("Plain txt : " + Plain_txt)
print("Shift pattern : " + str(s))
print("Cipher: " + encypt_func(Plain_txt, s))