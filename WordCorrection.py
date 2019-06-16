import re
from collections import Counter

f = open('big.txt').read()
array = re.findall(r'\w+', f.lower())   
 
final_words = Counter(array)
#print(len(final_words))
n = sum(final_words.values())


#making combinations of entered text by 1-distance
#correcting the word by one letter
def combinationsOne(txt):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_words = []
    for i in range(len(txt)+1):
        for l in letters:
            insert_words.append(txt[:i]+ l + txt[i:])
    
    deleted_words = []
    t = txt
    for i in range(len(txt)):
        t = txt
        deleted_words.append(txt[:i] +  txt[i+1:])

    replace_words = []
    for i in range(len(txt)):
        for l in letters:
            replace_words.append(txt[:i] + l +txt[i+1:])
    
    transpose_words = []
    for i in range(0,len(txt)-1):
        t=list(txt)
        t[i], t[i+1] = t[i+1], t[i]
        transpose_words.append(''.join(t))

    comb1_words = set(insert_words + deleted_words + replace_words + transpose_words)
    return comb1_words


#making combinations of entered text by 2-distance
#correcting the word by two letters
def combinationsTwo(txt):
    comb2_words = []
    for w1 in combinationsOne(txt):
        for w2 in combinationsOne(w1):
            comb2_words.append(w2)
    return comb2_words



#finding out possible(known) words from the original list
def possibleWords(txt):
    possible_list = []
    for w in txt:
        if w in final_words:
            possible_list.append(w)
    return set(possible_list)


#finding out candidate words
def candidateWords(txt):
    candidate1 = txt
    candidate2 = possibleWords([txt])
    candidate3 = possibleWords(combinationsOne(txt))
    candidate4 = possibleWords(combinationsTwo(txt))
    return (candidate2 or candidate3 or candidate4 or candidate1)


#calculating number of times entered word present in original list
def frequencyWords(txt):   
    frequency = final_words[txt] / n
    return frequency


#correcting the spelling of words
#it finds the candidate word that appeared max no. of times
def correctWord(txt):
    #frequencyWords = final_words[txt] / n
    correct = max(candidateWords(txt), key = frequencyWords)
    return correct


txt = input('Enter input: ')
print('Correct word: ', correctWord(txt))
print('Other possible words: ', candidateWords(txt))
print('Frequency of correct word: ' ,frequencyWords(correctWord(txt)))
