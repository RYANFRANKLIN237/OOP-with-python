import TextBlob
def Convert(string ):
    li = list (string.split())
    return li
str1 = input("enter the word :")
words= Convert(str1)
corrected_words = []
for i in words :
    corrected_words.append(TextBlob(i))
print("wrong spelling :" , words)
print("right spelling :")
for i in corrected_words:
    print(i.correct(), end="")
