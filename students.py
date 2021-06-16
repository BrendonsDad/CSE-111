import csv


def main():
    INUMBERINDEX = 0

    students = read_dict("students.csv", INUMBERINDEX)

    print(students)

    id = input('Please enter your Inumber9 (xx-xxx-xxxx): ')

    id = id.replace('-', '')
    if len(id) > 9:
        print(f'Invalid, too many characters. You typed {len(id)}, must have 9.')
    elif len(id) < 9:
        print(f'Invalid, too few characters. You typed {len(id)}, must have 9.')
    else:
        if not id.isdigit():
            print('Invalid number, only numbers accepted.')
        else:

            if id in students:

                # Find the student ID in the dictionary and
                # retrieve the corresponding value, which is a list.
                value = students[id]

                # Retrieve the student's given name (first name) and
                # surname (last name or family name) from the list.
                given_name = value


                # Print the student's name.
                print(f"Welcome, {given_name}")
            else:
                print("No such student")


def read_dict(filename, key_column_index):


    dictionary = {}


    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        students = []
        inumber = []

        for student in reader:
            students.append(student[0])
            inumber.append(student[1])
        
            dictionary = dict(zip(students, inumber))

    return dictionary


if __name__ == "__main__":
    main()