import math
from collections import OrderedDict
import csv
import re

# all contributors
#zc285
#ass209
#kap401
#arb295

#word_freq = {}
idf_dict = {}
idf_calc = {}
doc_freq = {}
#tfidf_dict = {}

def preproc(file):

    # open file
    preprocFile = open(file)
    preprocFileW = open(f"preproc_{file}", 'w')
    for line in preprocFile:

        str1 = line  
        
    
    # clean up the string

        str1 = re.sub(r'http://\S+ | https://\S+', '', str1)
        str1 = re.sub('[^\w\s]','',str1) 
        str1 = re.sub('\s+', ' ', str1)
        str1 = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', str1)
        str1 = str1.lower()

    # get rid of stopword
        stopList = []
        stopWords = open('stopwords.txt')
        for line in stopWords:
            stopList.append(line.strip())

        for stopWord in stopList:
           str1 = re.sub(r'\b'+ stopWord + r'\b\s+', '', str1)

    # remove suffixes which have ly, ing, ment        

        suffixList = ['ly', 'ing', 'ment']

        for suffix in suffixList:
            str1 = re.sub(suffix + r'\b', '', str1)
        
        
        preprocFileW.write(str1)
    
    
def IDFDictFinder(file):
    
    IDFRead = open(file)

    for line in IDFRead:
        wordList = line.split(" ")
        for i in wordList:
            if i not in idf_dict.keys():
                idf_dict[i] = 0

    IDFRead.close()

    IDFRead2 = open(file)            
    for line in IDFRead2:
        for key in idf_dict.keys():
            if re.search(r'\b' + key + r'\b', line):
                idf_dict[key] += 1




def calcuIDF(numberOfDocs):

    for key in idf_dict.keys():
        if key not in idf_calc:
            idf_calc[key] = (math.log(numberOfDocs/idf_dict[key])) + 1

    #print(idf_calc)

def calcTFIDF(file):
    tf_idf = open(file)
    modified_file = file[8:]
    
    
    tf_idfW = open(f'tfidf_{modified_file}', 'w')

    word_freq = {}

    totalWords = 0
    for line in tf_idf:
        wordList = line.split(' ')
        for i in wordList:
            totalWords += 1
            if i not in word_freq.keys():
                word_freq[i] = 1
            else:
                word_freq[i] += 1

    #print('Word Freq')
    #print(word_freq)
    #print()
   
    #print(word_freq) #Calculating frequencies of every word
    #print(doc_freq)
    tf_dict = {}
    
    for i in word_freq.keys():
        tf_dict[i] = word_freq[i] / totalWords

    tfidf_dict = {}

    for IDFkey in idf_calc.keys():
        if IDFkey not in tfidf_dict.keys():
            tfidf_dict[IDFkey] = 0
  
    for TFkey in tf_dict.keys():
        for IDFkey in idf_calc.keys():
            if TFkey == IDFkey:
                tfidf_dict[TFkey] = round(tf_dict[TFkey] * idf_calc[IDFkey], 2)

    #print(tf_dict)
    #print()
    #print(idf_calc)
    #print()
    #print(idf_calc)

    dict1 = OrderedDict(sorted(tfidf_dict.items()))
   
    top5Words = sorted(dict1.items(), key=lambda rating: rating[1], reverse= True) [:5]    

    tf_idfW.write(str(top5Words))

    #print(top5Words)


def main():


    with open('tfidf_docs.txt') as docs:
        list = docs.readlines()
        for line in list:
            preproc(line.strip())
            IDFDictFinder(f'preproc_{line.strip()}')

    numberOfDocs = len(list)
    calcuIDF(numberOfDocs)

    #print(idf_calc)

    with open('tfidf_docs.txt') as docs:
        list = docs.readlines()
        for line in list:
            calcTFIDF(f'preproc_{line.strip()}')
    
   
    #print(idf_dict)

main()