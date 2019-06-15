#program to predict the correct word for wrongly typed word

import re
import spellchecker

#creating a spellchecker object---spell
spell = spellchecker.SpellChecker(language=None) # turning off loading a built-in language dictionary


try:
    #working with big.txt corpus
    with open('big.txt', 'r') as file:
        f = file.read()
        words = []
        for word in f.split():
            words.append(word)   #creating a list of words present in corpus
    
    #filtering out all words except special chars & numbers using Regular Expression
    array = re.sub('[^a-zA-Z]', ' ', f)
   
   #writing the filtered words into myfile.txt
    with open('myfile.txt', 'w') as myfile:
        myfile.write(array)

    with open('myfile.txt','r') as  mfile:
        ff = mfile.read()

    #appending final words into a list
    final_words=[]
    for word in ff.split():
        final_words.append(word)


except FileNotFoundError:
    print('File not found')

except:
    print('Cannot open file')



#loading our own corpus--- it loads as words as in list 
#in spell object
spell.word_frequency.load_text_file('./myfile.txt')

txt = input('Enter a word: ')

#correccting the spelling entered by used using the same spell object
x = spell.correction(txt)
print('Correct spelling is: ',x)

#finding probability of corrected word
print('Probability of correct word: ',spell.word_probability(x,  total_words=len(final_words)))

#other possible words 
print('Other possible words: ',spell.candidates(txt))
