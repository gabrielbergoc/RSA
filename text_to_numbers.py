def text_to_int(text: str) -> list:
    list_ = []

    for letter in text:
        list_.append(ord(letter))

    return list_

def int_to_text(list_: list) -> str:
    text = ""

    for letter in list_:
        text += chr(letter)

    return text

# msg = "frase MUITO secreta"
#
# enc = text_to_int(msg)
# print(enc)
#
# decd = int_to_text(enc)
# print(decd)