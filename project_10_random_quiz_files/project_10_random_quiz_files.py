# Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

# Here is what the program does:
# Creates 35 different quizzes
# Creates 50 multiple-choice questions for each quiz, in random order
# Provides the correct answer and three random wrong answers for each question, in random order
# Writes the quizzes to 35 text files
# Writes the answer keys to 35 text files

#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
import os, pathlib

# Store the states and their capitals in a dictionary
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
number_of_quizzes=35

# set cwd to path where the *.py lies
file_path = pathlib.Path(os.path.realpath(__file__))
os.chdir(file_path.parent)
print(os.getcwd())

# Generate 35 quiz files.
for quizNum in range(number_of_quizzes):
# Call open(), write(), and close() for the quiz and answer key text files
# Use random.shuffle() to randomize the order of the questions and multiple-choice options

    # Create the quiz and answer key files.
    quizFile=open(f'capitalsquiz{quizNum + 1}.txt','w')
    answerKeyFile=open(f'capitalsquiz_answers{quizNum + 1}.txt','w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys()) # convert dictionary into list
    random.shuffle(states) # shuffle method randomly shuffles argument (list in this case) 

    # Loop through all 50 states, making a question for each of them
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]] # use questionNum enumerator to get state from shuffled list. Then find this state in dict and get it's corresponding value
        wrongAnswers = list(capitals.values()) # create list of all capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # from this list delete correct answer
        wrongAnswers = random.sample(wrongAnswers, 3) # from remaining list randomly choose 3 other wrong answers
        answerOptions = wrongAnswers + [correctAnswer] # join list of wrong answers and list with one correct answer
        random.shuffle(answerOptions) # randomly shuffle 4 answers

        # Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n") # {'ABCD'[i]} treats the string 'ABCD' as an array and will evaluate to 'A','B', 'C', and then 'D' on each respective iteration through the loop.
            quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}") # find correct answer's position in list answerOptions and write corresponding letter

    # close both files after looping through 50 questions
    quizFile.close()
    answerKeyFile.close()