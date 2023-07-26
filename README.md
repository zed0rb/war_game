'War' game requirements

1. User should type 'start' to start the game
2. Program should draw the card first and print it so user can see
3. User should be prompted to input 'd' to draw a card and program should print it out
4. Program should compare the two cards and add both of them to round winner's 'bottom deck'
5. Each player should have a main deck and also a bottom deck. If main deck is emptied, cards should be drawn from the bottom deck.
6. If player runs out of cards in both main and bottom decks, the other player should win.
7. In case of a tie in war round, an additional card should be drawn from both players (face down card) and then another one (face up) to compare if any of the cards have a bigger value and so on.

Program structure

1. class Deck
   Build a deck
   Deal two decks for each player
   Compare card values (as a @classmethod)

2. class Player
   Store a deck that was passed as an argument
   Store a bottom deck
   Method to draw a card from the deck and print it
   If main deck is empty then draw from bottom deck
   Method to add an array of cards to bottom deck

3. main function
   Construct Deck and 2 player objects
   Each player object should take a dealt deck as an argument
   Create a variable to track cards drawn in a round
   Create a while loop for the game
   - Computer draws a card
   - Program asks for user input ('d' for draw)
   - User draws a card
   - Drawn cards get stored
   - Compare which card wins
     - Append winning player's botttom deck with drawn cards
     - Empty drawn cards array for the next round
     - Continue the while loop
     - If a tie, draw face down cards, add to drawn cards array and continue the loop
