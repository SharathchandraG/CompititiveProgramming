import unittest

def kS(W, wt, val, n):
    K = [0 for x in range(W+1)]
 
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[w] = 0
            elif wt[i-1] <= w:
                if wt[i-1] == 0:
                    if val[i-1] == 0:
                        K[w] = 0
                    else:
                        return float('inf')
                else:
                    K[w] = max(val[i-1]*(w//wt[i-1]) + K[w%wt[i-1]],  K[w])
    return K[W]



def max_duffel_bag_value(cake_tuples, weight_capacity):

    # Calculate the maximum value we can carry
    l = [list(t) for t in zip(*cake_tuples)]

    return kS(weight_capacity, l[0], l[1], len(l[0]))

# Complexity O(m,n)

# Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)