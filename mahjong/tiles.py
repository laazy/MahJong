import random


class NoTileError(BaseException):
    '''无牌错误'''


class Tiles:
    '''
    牌堆，主要用来存储麻将牌并提供打乱、摸牌、指定位置摸牌功能。
    这是一个简单的只能从头到尾抽，并看固定位置的牌堆。

    数牌：筒条万1~9 *4
    字牌：东南西北中发白 *4
    花牌：春夏秋冬梅兰竹菊 *1
    上述牌以下述规则对应：
    x筒：1x，x条：2x，x万：3x
    东南西北中发白：40 41 42 43 50 51 52
    '''
    DEFAULT_COUNT = 4

    def __init__(self) -> None:
        self.tiles = []
        for i in range(9):
            self.tiles += [11+i, 21+i, 31+i]
        self.tiles += [40, 41, 42, 43, 50, 51, 52]
        self.tiles *= 4
        self.tiles = sorted(self.tiles)
        self.current_pos = 0

    @property
    def capicity(self):
        ''' 牌堆大小，总容量'''
        return len(self.tiles)

    @property
    def size(self):
        '''牌堆还剩多少张牌'''
        return 0 if self.empty else self.capicity - self.current_pos

    @property
    def empty(self):
        return self.current_pos >= self.capicity

    def shuffle(self) -> None:
        random.shuffle(self.tiles)

    def draw(self) -> int:
        if self.empty:
            raise NoTileError('没牌可以抽啦！')
        val = self.tiles[self.current_pos]
        self.current_pos += 1
        return val

    def see(self, pos=None) -> int:
        pos = self.current_pos if pos is None else pos
        if pos >= self.capicity:
            raise NoTileError(f'这里没牌给你看！你在看{pos}，最多只能看{self.capicity}！')
        return self.tiles[pos]
