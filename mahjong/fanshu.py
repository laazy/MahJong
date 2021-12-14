from typing import List, Tuple, Iterator
from itertools import combinations

MianZi = Tuple[int, int, int]
QueTou = Tuple[int, int]
Pattern = (Tuple[MianZi, MianZi, MianZi, MianZi, QueTou] |
           Tuple[MianZi, MianZi, MianZi, QueTou] |
           Tuple[MianZi, MianZi, QueTou] |
           Tuple[MianZi, QueTou] |
           Tuple[QueTou])


class PatternMatcher:
    def __init__(self) -> None:
        pass

    @classmethod
    def is_same(cls, tiles: List[int]) -> bool:
        return len(set(tiles)) == 1

    @classmethod
    def is_same_type(cls, tiles: List[int]) -> bool:
        return len({i // 10 for i in tiles}) == 1

    @classmethod
    def is_continues(cls, tiles: List[int]) -> bool:
        if not cls.is_same_type(tiles):
            return False
        num = sorted([i % 10 for i in tiles])
        for i in range(len(num)):
            if num[i] - num[0] != i:
                return False
        return True

    @classmethod
    def match_mian_zi(cls, m: MianZi) -> bool:
        return cls.is_same(m) or cls.is_continues(m)

    @classmethod
    def _iter_pattern(cls, tiles: List[int]) -> Iterator[Pattern]:
        if len(tiles) == 2:
            yield [tiles]
            return
        for m in combinations(tiles, 3):
            m = list(m)
            for i in m:
                tiles.remove(i)
            for o in cls._iter_pattern(tiles):
                yield [m] + o
            for i in m:
                tiles.append(i)

    @classmethod
    def match(cls, tiles: List[int]) -> bool:
        tiles = tiles.copy()
        for *ms, q in cls._iter_pattern(tiles):
            if all(map(cls.match_mian_zi, ms)) and cls.is_same(q):
                return True
        return False  


# class Fanshu:
#     def __init__(self) -> None:
#         pass
if __name__ == "__main__":
    pm = PatternMatcher()
    res = pm.match([11, 12, 13, 22, 22])
    print(res)
    res = pm.match([11, 12, 14, 11, 12, 14, 22, 22])
    print(res)
