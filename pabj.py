from deck import Deck
from player import Player

print("WELCOME TO PERSONAL ATTACK BLACKJACK, WHERE EVEN WHEN YOU WIN YOU'RE STILL A FUCKIN LOSER!")

class pabj:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.show()

        if p_status == 1:
            print("Congrats fuckface, u got a blackjack. Probably your only real accomplishment in life. I wish you the worst.")
            if d_status == 1:
                print("Oh my! BOTH of you got a blackjack :/ It's like even when u win, YOU'RE STILL A LOSER")
            return 1

        cmd = ""
        while cmd != "stand":
            bust = 0
            cmd = input("hit or stand? ...Don't fuck this up.")

            if cmd == "hit":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:
                print("wow, what a surprise, u fucked this up. u literally had one job.")
                return 1
        print ("\n")
        self.dealer.show()
        if d_status == 1:
            print("LOL Dealer got a blackjack b4 u even had a chance. Ur an idiot 4 playing this game.")
            return 1

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer busted. Ugh I hate it when my Dealer gets busted.")
                return 1
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print ("What a waste of time, it's a push. As in I hope someone pushes you off a cliff.")
        elif self.dealer.check_score() > self.player.check_score():
            print ("Dealer wins, Loser Loses. Same shit, different day.")
        elif self.dealer.check_score() < self.player.check_score():
            print ("ya, we get it, you won, you're not special.")
cmd = ""
while cmd != "no":
    b = pabj()
    b.play()
    cmd = input("Keep playing? yes or no. ")
