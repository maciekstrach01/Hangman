
## Video


https://github.com/maciekstrach01/Threads/assets/146733279/d7b2ae32-e964-4f20-850d-d6963eb23260
# Hangman

The programme is a Python implementation of the hanging game. It includes functions for guessing words, managing the state of the game, displaying results and handling menus. The player tries to guess a randomly selected word with a certain number of attempts depending on the selected difficulty level. Game results and game status are saved to text files. The programme allows the player to play the game again, display the results, review the guessed words or terminate the activity.



The validation logic I used during the game itself plays an important role in the programme:

-if the user enters a value which is not a single letter, he/she will get a corresponding message and the number of attempts will remain unchanged

-if the user enters a single letter which has already been entered, they will be informed and given another chance




The programme uses two external APIs. The first API, available at "https://random-word-api.herokuapp.com/word?number=1", is used to retrieve a random word, which becomes the object of the hanging game. The second API, available at "https://api.dictionaryapi.dev/api/v2/entries/en/{word}", is used to retrieve the definition of the selected word, which adds an educational element to the game by presenting the player with the meaning of the word they are trying to guess. If there is no definition for the word, the software will display a 'No definition' message.

## Screenshots




![Zrzut ekranu 2023-11-25 002447](https://github.com/maciekstrach01/Threads/assets/146733279/bf06ed1d-a537-4cd3-a07e-77d2b5949807)

![Zrzut ekranu 2023-11-25 002503](https://github.com/maciekstrach01/Threads/assets/146733279/2e240166-1298-4ee7-80c8-d83927919c99)

![Zrzut ekranu 2023-11-25 002529](https://github.com/maciekstrach01/Threads/assets/146733279/a1e6e9dc-591d-4a0a-bc41-727070e592d2)













## 🛠 Skills
Python


## Running Tests

To run the tests, you must have Visual Studio Code or another preferred IDE for Python installed. Configure the IDE for Python, translate the code into machine language i.e. compile it, and then run the program.