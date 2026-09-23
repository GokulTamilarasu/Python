from script import alphabets
def encrypt_or_decrypt(message,shift,encrypt_or_decrypt):
    output=""
    if encrypt_or_decrypt=="encrypt":
        for letter in message:
            if letter not in alphabets:
                output+=letter
            else:
                encrypt_index=alphabets.index(letter)+ shift
                output+=alphabets[encrypt_index]
    print(output)


encrypt_or_decrypt("hello",9,"encrypt")