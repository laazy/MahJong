import unittest

from mahjong.tiles import Tiles


class TilesTestCase(unittest.TestCase):
    def test_capicity(self):
        tiles = Tiles()
        self.assertEqual(tiles.capicity, 144)

    def test_size(self):
        tiles = Tiles()
        self.assertEqual(tiles.size, 144)

    def test_draw(self):
        tiles = Tiles()
        for i in range(144):
            self.assertEqual(tiles.size, 144 - i)
            tiles.draw()
        self.assertEqual(tiles.size, 0)

    def test_shuffle(self):
        '''我认为两次打乱后依然相同是实际不可能的'''
        tiles = Tiles()
        tiles.shuffle()
        old = tiles.tiles.copy()
        tiles.shuffle()
        new = tiles.tiles.copy()
        self.assertTrue(old != new)

    def test_see(self):
        tiles = Tiles()
        self.assertEqual(tiles.see(), tiles.see())
        self.assertEqual(tiles.see(0), tiles.see(0))
        self.assertEqual(tiles.see(55), tiles.see(55))
        self.assertEqual(tiles.see(143), tiles.see(143))
