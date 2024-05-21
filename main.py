import random
print("Hi! Welcome to the game 'Hangman'")

words_categories = {
    "Animals" : ["kangaroo", 'mongoose', 'chameleon', 'chimpanzee', 'basilisk', "alligator", "anteater", "duckbill platypus", "mandrill"],
    "EU countries" : ["austria", "bulgaria", "czech republic", "denmark", "luxembourg", "serbia", "montenegro", "kosovo", "andorra", "latvia"],
    "Fruits" : ["watermelon", "grapefruit", "pomogranate", "blueberry", "papaya", "dragonfruit", "cantaloupe", "apricot", "passion fruit", "guava"]
    }
categories = input("Choose  a category (Animals), (EU countries), (Fruits): ")
chosen_list = words_categories[categories]

hangman = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
      +---+
      |   |
      o   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  | 
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========
    """
]

max_index = len(chosen_list) - 1 # length of a list
random_index = random.randint(0, max_index)
random_word = chosen_list[random_index] # 0 1 2 3


fails = 0
guessed_letters = [' ']

while fails < 6:

    word = "" 
    for char in random_word: 
        if char in guessed_letters: 
            word += char 
        else:
            word += "-" 

    
    print(hangman[fails])
    print("Guessed letters:", guessed_letters)
    print(word.capitalize())

    if word == random_word:
        print ("You won!")
        break

    letter = input("Enter your letter: ").lower()
    guessed_letters.append(letter)

    if letter in random_word:
        print("Letter is in the word!")
    else:
        print("Letter is not in the word!")
        fails += 1

if fails == 6:
    print(hangman[6])
    print("You lost!")