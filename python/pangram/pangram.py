import string
def is_pangram(sentence):
#    sentence = sentence.replace(' ', '')
    sentence = sentence.lower()                 
    sentence = list(sentence)                   
    sentence = list(set(sentence))              # set returns a set which means each element occurs once.
#    sentence.sort()
#    print(sentence)
    alphabet = list(string.ascii_lowercase)     # generating a list of alphabets
    flag = 0
    for i in alphabet:
        if i in sentence:
            flag += 1

    if flag == 26:
        return True
    return False
    