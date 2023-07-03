import random
from time import sleep

from game.interfaces.ideck import IDeck
from game.interfaces.iplay import IPlay


class Game(IDeck, IPlay):
    DEFAULT_RESULT = 21
    PRICE_PER_GAME = 10

    def __init__(self, type_of_player):
        self.__suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.__cards = ['jack', 'queen', 'king', 'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.__deck = []
        self.__money = 0
        self.__type_of_player = type_of_player
        self.__result = 0
        self.__safe_result = 18
        self.__player_result = 0
        self.__croupier_result = 0

    def __str__(self):
        return (
            f'{self.__class__.__name__}:\n{{\n\t"money": {self.__money}\n\t"player_result": {self.__player_result}\n}}'
        )

    def _open_deck(self):
        for suit in self.__suits:
            for card in self.__cards:
                self.__deck.append((card, suit))

    def _shuffle_deck(self):
        random.shuffle(self.__deck)
        # print(self.__deck)

    def _reset_deck(self):
        self._open_deck()
        # print(self.__deck)

    def __before_game(self):
        print('I need to get money from my card, so i go to the ATM')
        money_for_game = 100
        self.__money = money_for_game
        sleep(0.5)
        print(f'I got money! Now my balance: {self.__money}')

    def __take_card(self):
        random_card = random.choice(self.__deck)
        sleep(0.5)
        self.__deck.remove(random_card)
        print(f'Card on the table: {random_card}')
        return random_card[0]

    def __count_result(self):
        card = self.__take_card()
        if card == 'jack' or card == 'queen' or card == 'king':
            self.__result += 10
        elif card == 'ace':
            self.__result += 11
        else:
            self.__result += int(card)
        print(self.__result)

    def _start_game(self):
        self.__before_game()
        print('I sit down at the table and say Hello to croupier')
        self._open_deck()
        self._shuffle_deck()

    def __tactics_of_game_for_player(self):
        if self.__type_of_player.lower() == 'aggressive':
            while self.__result <= self.__safe_result:
                self.__count_result()
        elif self.__type_of_player.lower() == 'safe':
            while self.__result < self.__safe_result:
                self.__count_result()
        self.__player_result = self.__result

    def __croupier_play(self):
        self.__result = 0
        while self.__result < self.__safe_result:
            self.__count_result()
        self.__croupier_result = self.__result

    def __check_result(self):
        if self.__player_result > self.DEFAULT_RESULT:
            self.__money = self.__money - self.PRICE_PER_GAME
            print(f'I lose {self.PRICE_PER_GAME}, so my balance now {self.__money}')
        elif self.__player_result <= self.DEFAULT_RESULT:
            print('Enough, now is croupier turn. ')
            self.__croupier_play()
            if self.__player_result < self.__croupier_result <= self.DEFAULT_RESULT:
                self.__money = self.__money - self.PRICE_PER_GAME
                print(f'I lose {self.PRICE_PER_GAME}, so my balance now {self.__money}')
            elif self.__croupier_result < self.__player_result or self.__croupier_result > self.DEFAULT_RESULT:
                self.__money = self.__money + self.PRICE_PER_GAME
                print(f'I won {self.PRICE_PER_GAME}, so my balance now {self.__money}')
            else:
                print(f'We got a draw, so my balance now {self.__money}')

    def play(self):
        self._start_game()
        self.__tactics_of_game_for_player()
        self.__check_result()
        self._finish_game()

    def _finish_game(self):
        print('Thank you for the game, see you later!')
        self._reset_deck()


if __name__ == '__main__':
    # select type of player 'safe' or 'aggressive'
    game = Game('safe')
    game.play()
    # print(game)
