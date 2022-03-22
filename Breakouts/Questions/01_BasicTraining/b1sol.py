## solutions to the breakout #1 (Day 1)
sent = ""
while True:
    newword = input("Please enter a word in the sentence (enter . ! or ? to end.): ")
    if newword in [".", "?", "!"]:
        if len(sent) > 0:
            # get rid of the nasty space we added in
            sent = sent[:-1]
        sent += newword
        break

    sent += f'{newword} '
    print(f"...currently: {sent}")
print(f"--->{sent}")
###  created by Josh Bloom at UC Berkeley, 2010,2012,2013,2015 (ucbpythonclass+bootcamp@gmail.com)
