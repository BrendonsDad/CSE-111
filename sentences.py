import random
import time

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ['adult', 'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'woman']
    else:
        nouns = ['adults', 'birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'women']
    
    noun = random.choice(nouns)
    return noun
        


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == 'past':
        verbs = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']

    elif tense == 'present' and quantity == 1:
        verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']

    elif tense == 'present' and quantity != 1:
        verbs = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']

    elif tense == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f'{preposition} {determiner} {noun}'
    return prepositional_phrase


def main():
    print('Hello there, my name is Hal. What is your name? ')
    name = input('')
    print(f"It's nice to meet you {name.capitalize()}. How are you today? ")
    mood = input(' ')
    if mood.lower() == 'good' or  mood.lower() == 'good!' or  mood.lower() == 'great' or  mood.lower() == 'great!' or  mood.lower() == 'well' or  mood.lower() == "i'm doing good" or  mood.lower() == "i'm good" or  mood.lower() == "i'm great!":
        print('That is good to hear. ')
        moods = ['okay', 'not doing so well', 'pretty good', 'great']
        current_mood = random.choice(moods)
        time.sleep(1)
        print(f"I'm {current_mood} today. ")
    
    elif mood.lower() == "i'm good, how about you?" or  mood.lower() == "i'm good how about you?" or  mood.lower() == "i'm good how about you" or mood.lower() == "i'm great, how about you?" or  mood.lower() == "i'm great how about you?" or  mood.lower() == "i'm great how about you" or mood.lower() == "i'm good, how are you?" or  mood.lower() == "i'm good how are you?" or  mood.lower() == "i'm good how are you" or mood.lower() == "i'm great, how are you?" or  mood.lower() == "i'm great how are you?" or  mood.lower() == "i'm great how are you" or mood.lower() == "i'm good! How about you?" or  mood.lower() == "i'm good! How about you?" or  mood.lower() == "i'm good! how about you" or mood.lower() == "i'm great! How about you?" or  mood.lower() == "i'm great! how about you?" or  mood.lower() == "i'm great! how about you" or mood.lower() == 'good, you?' or mood.lower() == 'good, and you?' or mood.lower() == 'How are you?':
        print()
        moods = ['okay', 'not doing so well', 'pretty good', 'great']
        current_mood = random.choice(moods)
        time.sleep(1)
        print(f"I'm {current_mood} today, thank you for asking! ")
    
    else:
        print('Human emotions are hard for me to understand. ')

    print()
    time.sleep(3)
    print('I have been trained in some aspects of your language. Here are some sentences I can produce on my own: ')
    time.sleep(5)

    

    print()
    for i in range(1,3):
        word = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, 'past')
        print(f'{word.capitalize()} {noun} {verb}. ')

    for i in range(1,3):
        word = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, 'present')
        print(f'{word.capitalize()} {noun} {verb}. ')
    
    for i in range(1,3):
        word = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, 'future')
        print(f'{word.capitalize()} {noun} {verb}. ')
    
    print()

    
    for i in range(1,3):
        word = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, 'past')
        prepositional_phrase = get_prepositional_phrase(i)
        print(f'{word.capitalize()} {noun} {verb} {prepositional_phrase}. ')

    for i in range(1,3):
        word = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, 'present')
        prepositional_phrase = get_prepositional_phrase(i)
        print(f'{word.capitalize()} {noun} {verb} {prepositional_phrase}. ')
    
    for i in range(1,3):
        word = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, 'future')
        prepositional_phrase = get_prepositional_phrase(i)
        print(f'{word.capitalize()} {noun} {verb} {prepositional_phrase}. ')
    
    print()
    time.sleep(5.75)
    print('Human language has always facinated me. ')
    time.sleep(1)
    print()
    subject = ''
    while subject.lower() != 'goodbye':
        print(f"What is something you would like to talk about {name.capitalize()}? Say 'goodbye' when you are bored. ")
        subject = input('')
        if subject.lower() == 'goodbye':
            subject = 'goodbye'
        else:
            quantity = float(input(f'How many {subject} are there? '))
            for i in range(1,3):
                word = get_determiner(quantity)
                noun = subject
                verb = get_verb(quantity, 'present')
                prepositional_phrase = get_prepositional_phrase(quantity)
                print(f'{word.capitalize()} {noun} {verb} {prepositional_phrase}. ')
    print(f'Goodbye {name.capitalize()}. ')

if __name__ == "__main__":
    main()