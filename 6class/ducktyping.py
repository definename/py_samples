class Quote():
    def __init__(self, person, phrase):
        self.person = person
        self.phrase = phrase
    def who(self):
        return self.person
    def says(self):
        return self.phrase + "."

class QuestionQuote(Quote):
    def says(self):
        return self.phrase + "?"

class ExclamationQuote(Quote):
    def says(self):
        return self.phrase + "!"

def who_says(obj):
    print(obj.who(), "says", obj.says())

hunter = Quote("Hunter", "I'm hunting")
who_says(hunter)

victim1 = ExclamationQuote("Victim2", "It's hunting season")
who_says(victim1)

victim2 = QuestionQuote("Victim1", "What's up, doc")
who_says(victim2)

print()

class Victim():
    def who(self):
        return "Another victim"
    def says(self):
        return "I am innocent!!"

victim3 = Victim()
who_says(victim3)