def letters(sentence):
    count = 0
    for char in sentence:
        if char.isalpha():
            count += 1
    return count
def words(sentence):
    sentence += " "
    w_count = 1
    switch = 0
    count = 0
    for char in sentence:
        if char.isalpha() or char == ' ':
            if char == ' ' and switch == 0:
                switch = 1
                count = 0
            elif char != ' ' and switch == 1:
                count = 1
            elif char == ' ' and switch + count == 2:
                w_count += 1
                count = 0
        else:
            pass
    return w_count

def sentences(string):
    string = str(string)
    return string.count('.')

string = input("Enter string: ")

L = ((letters(string))*100/words(string))
S = sentences(string)*100/words(string)
coleman =   0.0588*L - 0.296*S - 15.8
coleman = int(coleman)

if coleman <= 5:
    print("Text is very easy to read [5th grade level and below].")
elif coleman == 6:
    print("Text is easy to read [6th grade].")
elif coleman == 7:
    print("Text is quite easy to read [7th grade].")
elif coleman > 7 and coleman <= 10:
    print("Text is conversational level [8th-10th grade].")
elif coleman == 11 or coleman == 12:
    print("Text is hard to read [11th-12th grade].")
elif coleman > 12 or coleman < 17:
    print("Text is difficult to read [college level].")
elif coleman >= 17:
    print("Text is very difficult to read [professional].")


