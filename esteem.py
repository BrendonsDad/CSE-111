import time
import random

def main():
    print()
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.\nThis program will show you ten statements that you could possibly\napply to yourself. Please rate how much you agree with each of the\nstatements by responding with one of these four letters:")
    print()
    time.sleep(3)
    print("Type 'D' for strongly disagree, 'd' for disagree, 'a' for agree, or 'A' for strongly agree.")
    print()
    time.sleep(1)
    q1 = input('1. I feel that I am a person of worth, at least on an equal plane with others. ')
    print()
    time.sleep(.5)
    s1 = positive_numbers(q1)

    q2 = input('2. I feel that I have a number of good qualities. ')
    print()
    time.sleep(.5)
    s2 = positive_numbers(q2)

    q3 = input('3. All in all, I am inclined to feel that I am a failure. ')
    print()
    time.sleep(.5)
    s3 = negative_numbers(q3)

    q4 = input('4. I am able to do things as well as most other people. ')
    print()
    time.sleep(.5)
    s4 = positive_numbers(q4)

    q5 = input('5. I feel I do not have much to be proud of. ')
    print()
    time.sleep(.5)
    s5 = negative_numbers(q5)

    q6 = input('6. I take a positive attitude toward myself. ')
    print()
    time.sleep(.5)
    s6 = positive_numbers(q6)

    q7 = input('7. On the whole, I am satisfied with myself. ')
    print()
    time.sleep(.5)
    s7 = positive_numbers(q7)

    q8 = input('8. I wish I could have more respect for myself. ')
    print()
    time.sleep(.5)
    s8 = negative_numbers(q8)

    q9 = input('9. I certainly feel useless at times. ')
    print()
    time.sleep(.5)
    s9 = negative_numbers(q9)

    q10 = input('10. At times I think I am no good at all. ')
    print()
    time.sleep(.5)
    s10 = negative_numbers(q10)

    score = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10

    print(f'Your score is {score}. ')
    print('A score below 15 may indicate problematic low self-esteem. ')

    nrs()


def nrs():
    print()
    print()
    questions = ['My ideal vacation spot would be a remote wilderness area', 'I always think about how my actions effect the enviornment', 'I take notice of wildlife where ever I am', 'I feel very connect all living things and the earth', 'My relationship to nature is an important part of who I am', 'My connection to nature and the enviornment is part of my spirituality']
    print()
    print("This program is an implementation of the Nature Relatedness Scale.\nThis program will show you six statements that you could possibly\napply to yourself. Please rate how much you agree with each of the\nstatements by responding with one of these four letters:")
    print()
    time.sleep(3)
    print("Type 'D' for disagree, 'd' for slightly disagree, n for nuetral, 'a' for slightly agree, or 'A' for agree.")
    print()
    time.sleep(1)

    random.shuffle(questions)

    score = 0
    question_number = 1

    for question in questions:

        prompt = input(f'{question_number}. {question}? ')

        point = positive_numbers2(prompt)

        score = score + point

        question_number = question_number + 1
    
    new_score = score / 6



    # q1 = input('1. My ideal vacation spot would be a remote wilderness area. ')
    # print()
    # time.sleep(.5)
    # s1 = positive_numbers2(q1)

    # q2 = input('2. I always think about how my actions effect the enviornment. ')
    # print()
    # time.sleep(.5)
    # s2 = positive_numbers2(q2)

    # q3 = input('3. I take notice of wildlife where ever I am. ')
    # print()
    # time.sleep(.5)
    # s3 = positive_numbers2(q3)

    # q4 = input('4. I feel very connect all living things and the earth. ')
    # print()
    # time.sleep(.5)
    # s4 = positive_numbers2(q4)

    # q5 = input('5. My relationship to nature is an important. ')
    # print()
    # time.sleep(.5)
    # s5 = positive_numbers2(q5)

    # q6 = input('6. My connection to nature and the enviornment is part of my spirituality. ')
    # print()
    # time.sleep(.5)
    # s6 = positive_numbers2(q6)\
    
    # score = (s1 + s2 + s3 + s4 + s5 + s6) / 6

    print(f'Your score is {new_score:.1f}. ')
    print('A score below 2.5 may indicate problematic low nature awareness. ')

def positive_numbers(question):
    if question == 'D':
        score = 0
    elif question == 'd':
        score = 1
    elif question == 'a':
        score = 2
    else:
        score = 3
    
    return score

def positive_numbers2(question):
    if question == 'D':
        score = 1
    elif question == 'd':
        score = 2
    elif question == 'n':
        score = 3
    elif question == 'a':
        score = 4
    elif question == 'A':
        score = 5
    
    return score

def negative_numbers(question):
    if question == 'D':
        score = 3
    elif question == 'd':
        score = 2
    elif question == 'a':
        score = 1
    else:
        score = 0
    
    return score



main()


