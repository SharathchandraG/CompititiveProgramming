import unittest
import math

def find_rotation_point(words):

    # Find the rotation point in the list
    if (len(words)) == 0:
      return -1

    left = 0
    right = len(words)-1

    while left <= right:
      if words[left] <= words[right]:
        return (right+1)%(len(words))
      mid = int(math.ceil( left + (right - left)/2))
      print(mid)
      if words[left] >= words[mid]:
        right = mid-1
      else:
        left = mid


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)