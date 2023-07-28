'War' game requirements

1. User should type 'start' to start the game
2. Program should draw the card first and print it so user can see
3. User should be prompted to input 'd' to draw a card and program should print it out
4. Program should compare the two cards and add both of them to round winner's 'bottom deck'
5. Each player should have a main deck and also a bottom deck. If main deck is emptied, cards should be drawn from the bottom deck.
6. If player runs out of cards in both main and bottom decks, the other player should win.
7. In case of a tie in war round, an additional card should be drawn from both players (face down card) and then another one (face up) to compare if any of the cards have a bigger value and so on.

Program structure

class Deck
1. Build a deck
2. Deal two decks for each player
3. Compare card values (as a @classmethod)

class Player
1. Store a deck that was passed as an argument
2. Store a bottom deck
3. Method to draw a card from the deck and print it
4. If main deck is empty then draw from bottom deck
5. Method to add an array of cards to bottom deck

main function
1. Construct Deck and 2 player objects
2. Each player object should take a dealt deck as an argument
3. Create a variable to track cards drawn in a round
4. Create a while loop for the game
   - Computer draws a card
   - Program asks for user input ('d' for draw)
   - User draws a card
   - Drawn cards get stored
   - Compare which card wins
     - Append winning player's botttom deck with drawn cards
     - Empty drawn cards array for the next round
     - Continue the while loop
     - If a tie, draw face down cards, add to drawn cards array and continue the loop
