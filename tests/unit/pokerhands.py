import unittest

from pokerhands import parse_hands, compare, classify, Card, constants

def _parse_hand(line):
    # nasty hack, just add junk second hand onto the line to reuse function
    return parse_hands(line + " QH TD JC 2D 8S")[0]

class TestHandParsing(unittest.TestCase):
    @unittest.skip("input contains only valid combination of cards")
    def test_combinations(self): raise NotImplementedError()

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

        self.assertEqual(len(hand1), 5)
        self.assertEqual(len(hand2), 5)

        for c in hand1 + hand2:
            self.assertIsInstance(c, Card)

class TestClassification(unittest.TestCase):
    def test_high_card(self):
        cases = ["3H 7H 6S KC JS","3H 4H 5S KC TS"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.HIGH_CARD, c[0])

    def test_one_pair(self):
        cases = ["3H 7H 6S JC JS","3H 4H 3S KC TS"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.ONE_PAIR, c[0])

    def test_two_pair(self):
        cases = ["3H 3D 6S JC JS","3H 4H 3S KC KS"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.TWO_PAIR, c[0])

    def test_three_of_a_kind(self):
        cases = ["3H 3D 3C KC JS","4H 4C 4S KC JS"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.THREE_OF_A_KIND, c[0])

    def test_straight(self):
        cases = ["2D 3C 4S 5H 6D","AS KD QH JC TD"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.THREE_OF_A_KIND, c[0])

    def test_flush(self):
        cases = ["2D 3D 8D TD 6D","AC 8C 2C 4C JC"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.THREE_OF_A_KIND, c[0])

    def test_full_house(self):
        cases = ["3H 3D 3C KC KS","4H 4C 4S JC JS"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.FULL_HOUSE, c[0])

    def test_four_of_a_kind(self):
        cases = ["3H 3D 3C 3S JS","4H 4C 4S 4D JS"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.THREE_OF_A_KIND, c[0])

    def test_straight_flush(self):
        cases = ["2D 3D 4D 5D 6D","AS KS QS JS TS"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.THREE_OF_A_KIND, c[0])

    def test_royal_flush(self):
        cases = ["AS KS QS JS TS", "AD TD KD JD QD"]

        for c in cases:
            c = classify(_parse_hand(c))
            self.assertEqual(constants.hands.THREE_OF_A_KIND, c[0])

class TestHandComparison(unittest.TestCase):
    def test_less_than(self):
        cases = [parse_hands("8C TS KC 9H 4S 7D 2S 5D 3S AC")]
        for case in cases:
            self.assertEqual(compare(case[0],case[1]), -1)

    @unittest.skip("input contains no cases where the output is equal")
    def test_equals(self): raise NotImplementedError()

    def test_greater_than(self):
        cases = [parse_hands("5C AD 5D AC 9C 7C 5H 8D TD KS")]
        for case in cases:
            self.assertEqual(compare(case[0],case[1]), 1)