# Chord Progression Generator - Marshall Ferguson - 7/2020

print("Welcome to the Chord Progression Generator!")
print("This program will ask if you want a major or minor progression,")
print("and then how many chords you want in the progression.")
print("Then, the program will give you a randomized chord progression based on your answers!")

# TODO - Ask user if they want a major or minor chord progression

major_or_minor = input("Would you like the chord progression to be in a major or minor key?")

# TODO - Ask user how many chords they want in the progression

number_of_chords = input("How many chords would you like in the progression?")
number_of_chords = int(number_of_chords)

# TODO - Create a data structure that represents the chord board graph

major_chord_board = {'I': ['ii', 'iii', 'IV', 'V', 'vi', 'vii'],
                     'ii': ['I', 'iii', 'IV', 'V', 'vi', 'vii'],
                     'iii': ['I', 'ii', 'IV', 'V', 'vi', 'vii'],
                     'IV': ['I', 'ii', 'iii', 'V', 'vi', 'vii'],
                     'V': ['I', 'ii', 'iii', 'IV', 'vi', 'vii'],
                     'vi': ['I', 'ii', 'iii', 'IV', 'V', 'vii'],
                     'vii': ['I', 'ii', 'IV', 'V', 'vi']
}

minor_chord_board = {'i': ['ii', 'III', 'iv', 'V', 'VI', 'VII'],
                     'ii': ['i', 'III', 'iv', 'V', 'VI', 'VII'],
                     'III': ['i', 'ii', 'iv', 'V', 'VI', 'VII'],
                     'iv': ['i', 'ii', 'III', 'V', 'VI', 'VII'],
                     'V': ['i', 'ii', 'III', 'iv', 'VI', 'VII'],
                     'VI': ['i', 'ii', 'III', 'iv', 'V', 'VII'],
                     'VII': ['i', 'ii', 'III', 'iv', 'V', 'VI'],
}

# TODO - Create a function that generates a chord progression based on user input
    # EG - if user asks for a 4 chord progression in a major key, the program outputs something like "I IV V I" or "I ii vii I"