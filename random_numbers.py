import random

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(0, quantity):
        word = random.uniform(1, 100)
        clean_word = round(word, 1)
        numbers_list.append(clean_word)

def append_random_words(words_list, quantity=1):
    my_words = ['bird', 'cat', 'dog', 'elephant', 'Antartica', 'Russia', 'rifle', 'Georgia']
    for _ in range(0, quantity):
        word = random.choice(my_words)
        words_list.append(word)

def main():
    randnums = [16.2, 75.1, 52.3]
    randwords = ['hammer', 'axle', 'ape', 'Moon', 'light']
    print(randnums)
    
    append_random_numbers(randnums)
    print(randnums)
    randnums_map = map(str, randnums)
    randnums_str = ', '.join(randnums_map)
    print(randnums_str)

    append_random_numbers(randnums, 3)
    for i in randnums:
        print(i)

    append_random_words(randwords, 3)
    print(randwords)

if __name__ == "__main__":
    main()


# students = ["joey", "emily", "fred"]
# print(students)

# user_student = input("Please enter your favorite student: ")

# howgwarts_students = ['hermione', 'ron', 'harry']
# students.extend(howgwarts_students)
# students.append(user_student)
# students.insert(1, user_student)
# students_copy = students.copy
# print(students.count('joey'))

# #Change Emily
# students[1] = "Hanna"

# print(students)

# print(type(students[0].capitalize()))



# for i, val in enumerate(students):
#     students[i] = val.title()

# print(students)