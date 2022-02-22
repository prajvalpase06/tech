string = str(input("Enter the text: "))        #input by user
word_count = string.count(' ') + 1                  # the number of words in a sentence is always 1 + no. of spaces

x = string.count("?")
y = string.count(".")
z = string.count("!")

sentence_count = x+y+z                         #counting the num of sentences
count_letters = 0

for i in string:
    if i.isalpha():                            #isalpha is used to check whether the character is a alphabet or not
        count_letters += 1

L = (count_letters/word_count)*100
S = (sentence_count/word_count)*100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)                            # rounding the index to the nearest integer

if grade>16:
    print("16+")
if grade<1:
    print("below grade 1")
if ((grade>=1) and (grade<=16)):
    print("Grade "+str(grade))





