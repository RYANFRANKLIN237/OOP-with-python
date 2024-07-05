#this program creates quizzes with questions and answers in random order, along with the answer Key

import random

#the quiz data. keys are regions and values are their capitals.

capitals = { 'southwest' : 'buea','littoral':'douala','northwest':'bamenda','centre':'yaounde','east':'bertoua'
 ,'south':'ebolowa','west':'bafoussam','north':'garoua','farnorth':'maroua','adamawa':'ngaoundere'}

#generate 7 quiz files

for quizNum in range(7):
    #create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum), 'w')
    answerKeyFile = open('capitalsquizanswers%s.txt' % (quizNum), 'w')

    #create header for quiz
    quizFile.write('Name:\n\nDate:\n\nSubject:Citizenship\n\nTime:8:00am')
    quizFile.write((' ' * 20) + 'capitals quiz (form %s)' % (quizNum +1))
    quizFile.write('\n\n')

    #shuffle the order of regions
    regions = list(capitals.keys())
    random.shuffle(regions)

#write the questions and answer options to the quiz file
quizFile.write('%s. what is capital of %s\n' % (quizNum + 1, regions[quizNum]))
for i in range(4):
    quizFile.write(' %s. %s\n' % ('ABCD' [i], answerOptions[i]))
    quizFile.write('\n')

#loop throuh all 10 regions , making a question for each.

for questioNum in range(10):
    #get right and wrong answers
    correctAnswer = capitals[regions[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    #write the answer key to a file
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()