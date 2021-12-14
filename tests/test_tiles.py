import unittest

from mahjong.tiles import Tiles, NoTileError


class TilesTestCase(unittest.TestCase):
    TOTAL_COUNT = 136
    def test_capicity(self):
        tiles = Tiles()
        self.assertEqual(tiles.capicity, self.TOTAL_COUNT)

    def test_size(self):
        tiles = Tiles()
        self.assertEqual(tiles.size, self.TOTAL_COUNT)

    def test_draw(self):
        tiles = Tiles()
        for i in range(self.TOTAL_COUNT):
            self.assertEqual(tiles.size, self.TOTAL_COUNT - i)
            tiles.draw()
        self.assertEqual(tiles.size, 0)
        with self.assertRaises(NoTileError):
            tiles.draw()

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
        self.assertEqual(tiles.see(self.TOTAL_COUNT - 1), tiles.see(self.TOTAL_COUNT - 1))
        with self.assertRaises(NoTileError):
            tiles.see(self.TOTAL_COUNT)
