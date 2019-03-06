class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

    def __str__(self):
        return self.text


w1 = Word("ah")
w2 = Word("AH")
print(w1 == w2)
print(w1)