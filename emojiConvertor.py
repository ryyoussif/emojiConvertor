
emoji_convertor = {
    "<3": "❤",
    ":)": "😊",
    ":-D":"😂",
    ":(":"🙁",
    ";-)":"😘"
}
text = input(">")
text = text.split()
for word in text:
    print(emoji_convertor.get(word,word),end = ' ')
