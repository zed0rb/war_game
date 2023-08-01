import random


class Deck:
    suits = ["♠", "♥", "♦", "♣"]
    values = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def init(self):
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


def main():
    deck = Deck()
    deck1, deck2 = deck.deal()

    start = input(
        "Game begins. To draw a card, type 'd', to finish the game, type 'q'. Start game by drawing a card: "
    )


if __name__ == "__main__":
    main()
