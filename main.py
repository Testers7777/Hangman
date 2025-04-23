import random
import os

mode = str(input('Bienvenue ! Jouer en Solo ou Multijoueur ? (S/M)')).upper()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

hangman_stages = [
    
    """
       +----+
            |
            |
            |
          ===
    """,
    """
       +----+
       O    |
            |
            |
          ===
    """,
    """
       +----+
       O    |
       |    |
            |
          ===
    """,
    """
       +----+
       O    |
      /|    |
            |
          ===
    """,
    """
       +----+
       O    |
      /|\\   |
            |
          ===
    """,
    """
       +----+
       O    |
      /|\\   |
      /     |
          ===
    """,
    """
       +----+
       O    |
      /|\\   |
      / \\   |
          ===
    """
]


def play(word):
    secretWord = word
    while True:
        foundLetters = []
        triedLetters = []
        tries = 0

        while True:
            wordPlace = ""
            for letter in secretWord:
                if letter in foundLetters:
                    wordPlace += letter + " "
                else:
                    wordPlace += "_ "

            if "_" not in wordPlace:
                clear()
                print(f'🎉 Bravo ! Le mot était : {secretWord}')
                break

            if tries == 6:
                clear()
                print(hangman_stages[tries])
                print(f'💀 Vous avez perdu ! Le mot était : {secretWord}')
                break

            print(hangman_stages[tries])
            newLetter = input(f'\nMot : {wordPlace.strip()}\nLettres essayées : {" ".join(triedLetters)}\n\nEntre une lettre : ').lower()
            clear()

            if not newLetter.isalpha() or len(newLetter) != 1:
                print("❌ Entrée invalide. Tu dois entrer une seule lettre.")
                continue
            elif newLetter in foundLetters or newLetter in triedLetters:
                print("Lettre déjà essayée.")
                continue
            elif newLetter in secretWord:
                foundLetters.append(newLetter)
                print("✅ Bonne lettre !")
            else:
                triedLetters.append(newLetter)
                print("❌ Mauvaise lettre.")
                tries += 1

        playAgain = input("Rejouer ? (Y/N) ").upper()
        if playAgain != "Y":
            print("Bonne journée !")
            break
        else:
            global mode
            clear()
            mode = str(input('Bienvenue ! Jouer en Solo ou Multijoueur ? (S/M)')).upper()
            if mode == "S":
                with open("./hangman/mots.txt", "r", encoding="utf-8") as fichier:
                    words = [word.strip() for word in fichier if word.strip()]
                    secretWord = random.choice(words)
            elif mode == "M":
                secretWord = str(input('Quel mot voulez-vous que votre adversaire devine ?')).lower()
            else:
                print('Bonne journée !')
                break

if mode == "S":
    with open("./hangman/mots.txt", "r", encoding="utf-8") as fichier:
        words = [word.strip() for word in fichier if word.strip()]
    play(random.choice(words))
elif mode == "M":
    wordWanted = str(input('Quel mot voulez-vous que votre adversaire devine ?')).lower()
    play(wordWanted)
else:
    print('Veuillez rendre sois S (Solo) sois M (Multijoueur)')