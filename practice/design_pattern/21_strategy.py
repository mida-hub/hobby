# Strategy

from abc import ABC, abstractmethod
from enum import Enum
from random import randint

class HandType(Enum):
    GUU = 0
    CHOKI = 1
    PAA = 2

    @classmethod
    def show_all(cls) -> [int]:
        return list(map(lambda c: c.value, cls))

class Hand:
    def __init__(self, hand_index):
        if not hand_index in HandType.show_all():
            raise Exception('値が誤っています')
        self.hand_index = hand_index

    def is_win(self, other):
        if (self.hand_index + 1) % 3 == other.hand_index:
            return True
        return False
    
    def is_lose(self, other):
        if self.hand_index == (other.hand_index + 1) % 3:
            return True
        return False

class Strategy:
    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self, is_win):
        pass

# 勝利時は次も同じ手を出す
class SimpleStrategy(Strategy):
    def __init__(self):
        self.hand = None
        self.is_win = False

    def next_hand(self):
        if not self.is_win:
            self.hand = Hand(randint(0, 2))
        return self.hand

    def study(self, is_win):
        self.is_win = is_win

# 前回出した手から、次に出す手のうち最も勝っているものを考えて出す
class ComplexStrategy(Strategy):
    def __init__(self):
        self.current_hand = None
        self.prev_hand = None
        self.histories = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # [今回の手][次の手]

    def next_hand(self):
        if self.current_hand:
            self.prev_hand = self.current_hand
        self.current_hand = self.__get_most_winning_hand()
        return self.current_hand

    def  __get_most_winning_hand(self):
        if not self.prev_hand:
            return Hand(randint(0, 2))
        tmp_hand = 0
        if self.histories[self.prev_hand.hand_index][1] > self.histories[self.prev_hand.hand_index][tmp_hand]:
            tmp_hand = 1
        if self.histories[self.prev_hand.hand_index][2] > self.histories[self.prev_hand.hand_index][tmp_hand]:
            tmp_hand = 2
        return Hand(tmp_hand)

    def study(self, is_win):
        if not self.prev_hand:
            return
        if is_win:
            self.histories[self.prev_hand.hand_index][self.current_hand.hand_index] += 1
        else:
            self.histories[self.prev_hand.hand_index][(self.current_hand.hand_index + 1) % 3] += 1
            self.histories[self.prev_hand.hand_index][(self.current_hand.hand_index + 2) % 3] += 1

class Player:
    def __init__(self, name, strategy: Strategy):
        self.name = name
        self.strategy = strategy
        self.win_count = 0
        self.lose_count = 0
        self.game_count = 0
    
    def next_hand(self):
        return self.strategy.next_hand()
    
    def win(self):
        self.strategy.study(True)
        self.win_count += 1
        self.game_count += 1
    
    def lose(self):
        self.strategy.study(False)
        self.lose_count += 1
        self.game_count += 1
    
    def even(self):
        self.game_count += 1
    
    def __str__(self):
        return f'{self.name}: {self.game_count} games, {self.win_count} win, {self.lose_count} lose.'

    # def get_histories(self):
    #     return self.strategy.histories

taro = Player('Taro', SimpleStrategy())
jiro = Player('Jiro', ComplexStrategy())

for _ in range(10):
    taro_hand = taro.next_hand()
    jiro_hand = jiro.next_hand()
    if taro_hand.is_win(jiro_hand):
        taro.win()
        jiro.lose()
    elif taro_hand.is_lose(jiro_hand):
        taro.lose()
        jiro.win()
    else:
        taro.even()
        jiro.even()

    # print(HandType(taro_hand.hand_index))
    # print(HandType(jiro_hand.hand_index))
    # print(jiro)
    # print(jiro.get_histories())

print(taro)
print(jiro)

# hand1 = Hand(2)
# hand2 = Hand(1)

# print(hand1.is_win(hand2))
# print(hand1.is_lose(hand2))
