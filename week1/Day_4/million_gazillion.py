import unittest


class Trie(object):

    # Implement a trie and use it to efficiently store strings
    def __init__(self):
        self.root = {}
        self.valid = False

    def add_word(self, key):
        if len(key) == 0:
            node = Trie()
            if key in self.root:
                return False
            else:
                node = Trie()
                node.valid = True
                self.root[key] = node
                return True
        head = key[0]
        if head in self.root:
            node = self.root[head]
        else:
            node = Trie()
            self.root[head] = node

        if len(key) > 1:
            p = key[1:]
            return node.add_word(p)
        else:
            if node.valid:
                return False
            else:
                self.root[head].valid = True
                return True  


# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)