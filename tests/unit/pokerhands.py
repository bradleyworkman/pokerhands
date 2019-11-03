import unittest

from pokerhands import parse_hands, compare, Card, constants

class TestHandParsing(unittest.TestCase):
    @unittest.skip("input contains only valid number of cards")
    def test_more_cards(self): raise NotImplementedError()

    @unittest.skip("input contains only valid number of cards")
    def test_less_cards(self): raise NotImplementedError()

    @unittest.skip("input contains no cases where the output is equal")
    def test_invalid_suits(self): raise NotImplementedError()

    @unittest.skip("input contains only valid ranks")
    def test_invalid_ranks(self): raise NotImplementedError()

    def test_full_cards(self):
        hand1,hand2 = parse_hands("8C TS KC 9H 4S 7D 2S 5D 3S AC")

class TestClassification(unittest.TestCase):
    @unittest.skip("TODO")
    def test_high_card(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_one_pair(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_two_pair(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_three_of_a_kind(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_straight(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_flush(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_full_house(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_four_of_a_kind(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_straight_flush(self): raise NotImplementedError()

    @unittest.skip("TODO")
    def test_royal_flush(self): raise NotImplementedError()

class TestHandComparison(unittest.TestCase):
    def test_less_than(self):
        cases = []
        for case in cases:
            self.assertEqual(compare(case[0],case[1]), -1)

    @unittest.skip("input contains no cases where the output is equal")
    def test_equals(self): raise NotImplementedError()

    def test_greater_than(self):
        cases = []
        for case in cases:
            self.assertEqual(compare(case[0],case[1]), 1)