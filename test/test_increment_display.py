import unittest

from memory_profiler import LineProfiler, profile, show_results
from io import StringIO


class TestIncrementDisplay(unittest.TestCase):
    """Tests memory incrementation / decrementation display"""
    def test_normal_incr(self):

        def normal_incr():
            use_some_memory = [1] * (10 ** 6)

        profiler = LineProfiler()
        wrapped = profiler(normal_incr)
        wrapped()

        show_results(profiler)
        results = list(list(profiler.code_map.values())[0].values())[-1]

    def test_loop_incr(self):

        def loop_incr():
            a = []
            for i in range(3):
                b = [2] * (2 * 10 ** 7)
                a.append(b)

        profiler = LineProfiler()
        wrapped = profiler(loop_incr)
        wrapped()

        show_results(profiler)
        results = list(list(profiler.code_map.values())[0].values())[-1]

    def test_loop_decr(self):

        def loop_with_del():
            for i in range(3):
                b = [2] * (2 * 10 ** 7)
            a = 1

        profiler = LineProfiler()
        wrapped = profiler(loop_with_del)
        wrapped()

        show_results(profiler)
        results = list(list(profiler.code_map.values())[0].values())[-1]


if __name__ == '__main__':
    unittest.main()
