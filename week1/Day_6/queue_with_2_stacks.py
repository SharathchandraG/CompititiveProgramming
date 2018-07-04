import unittest


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.elements = []

    def push(self, item):
        """Push new item to stack"""
        self.elements.append(item)

    def pop(self):
        if not self.elements:
            return None
        return self.elements.pop()

    def peek(self):
        """See what the last item is"""
        if not self.elements:
            return None
        return self.elements[-1]

class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack = Stack()
        self.count = 0

    def enqueue(self, item):
        stack = Stack()
        for k in range(self.count):
            stack.push(self.stack.pop())
        self.stack.push(item)
        for k in range(self.count):
            self.stack.push(stack.pop())
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception('Exception')
        self.count -= 1
        return self.stack.pop()


# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)