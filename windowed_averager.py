import unittest

class WindowedAverager:
    """
    For the `window_size` defined in the constructor, when accept() is called,
    return the average of the last `window_size` values seen.  If we haven't
    seen `window_size` values yet, return the average of the values we have
    seen.

    i.e: If `window_size` == 3, then when accept(x) is called return the
    average of the last 3 numbers `accept` has recieved.
    """

    # Constructor
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.history = []

    def accept(self, x: int) -> float:
        """
        Args:
            x (int): The value to add to the window

        Returns:
            float: The average of the last `window_size` values seen.  If we
                haven't seen `window_size` values yet, return the average
                of all values currently in the window.
        """
        self.history.append(x)
        if len(self.history) < self.window_size:
            return sum(self.history)/len(self.history)
        else:
            if len(self.history) > self.window_size:
                self.history = self.history[1:]
            return sum(self.history)/self.window_size


# # RUNNER - DO NOT CHANGE
# class TestHandler(unittest.TestCase):
#     def test_handler(self):
#         sh = WindowedAverager(3)
#         self.assertEqual(sh.accept(1), 1.0)
#         self.assertEqual(sh.accept(2), 1.5)
#         self.assertEqual(sh.accept(3), 2.0)
#         self.assertEqual(sh.accept(4), 3.0)
#
# testclass = unittest.main(exit=False)
# if testclass.result.wasSuccessful():
#     print("Test pass -- woohoo!")

sh = WindowedAverager(3)
print(sh.accept(1))
print(sh.accept(2))
print(sh.accept(3))
print(sh.accept(4))
print(sh.accept(5))
