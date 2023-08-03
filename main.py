import random
import sys


class Deck:
    suits = ["♠", "♥", "♦", "♣"]
    values = ["2", "3", "4", "5", "6", "7", "8",
              "9", "10", "Jack", "Queen", "King", "Ace",]

    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for i in self.suits:
            for j in self.values:
                self.cards.append(i + " " + j)
        return self.cards

    # method to split the deck in 2
    def deal(self):
        random.shuffle(self.cards)
        self.deck1 = self.cards[:26]
        self.deck2 = self.cards[26:]
        return self.deck1, self.deck2

    @classmethod
    def compare(cls, card1, card2):
        ...


class Player:
    def __init__(self, name, deck):
        self.deck = deck
        self.name = name
        self.card = None
        self.bottom_deck = []

    def draw(self):
        if self.deck != []:
            self.card = self.deck.pop()
        elif self.bottom_deck != []:
            self.card = self.bottom_deck.pop()
        # Decks are empty, player wins
        else:
            return False
        print(f"{self.name} has drawn a card")
        return self.card

    def add_to_bottom_deck(self, cards):
        for i in cards:
            self.bottom_deck.append(i)
        return self.bottom_deck


def main():
    deck = Deck()
    deck1, deck2 = deck.deal()

    name = input("Enter your name: ")

    player1 = Player("Computer", deck1)
    player2 = Player(name, deck2)

    print("Game begins. To draw a card, type 'd', to finish the game, type 'q'")

    round_cards = []

    while True:
        player1_card = player1.draw()
        if player1_card == False:
            print(f"{player2.name} WON!!!")
            break
        print(player1_card)

        move = input("Draw a card by typing 'd': ")

        if move == "d":
            player2_card = player2.draw()
            if player2_card == False:
                print(f"{player1.name} WON!!!")
                break
            print(player2_card)
            round_cards.append(player1_card)
            round_cards.append(player2_card)

            if Deck.compare(player1_card, player2_card) == "player1":
                print(f"{player1.name} takes the cards\n")
                player1.add_to_bottom_deck(round_cards)
                round_cards = []
                continue
            elif Deck.compare(player1_card, player2_card) == "player2":
                print(f"{player2.name} takes the cards\n")
                player2.add_to_bottom_deck(round_cards)
                round_cards = []
                continue
            elif Deck.compare(player1_card, player2_card) == "draw":
                print("WAR")
                continue

        elif move == "q":
            sys.exit("Quit game")
        else:
            sys.exit("Invalid key entered")


if __name__ == "__main__":
    main()
