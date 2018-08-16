import unittest

# You can skip a whole test class

@unittest.skip(reason="May fail intermittently")
class OrderDependentExample(unittest.TestCase):
    def test_foo(self):
        with open('/tmp/bla', 'w') as f:  # this is a bad idea anyway,
                                          # you should use randomized names for temporary files
            f.write('bla')

    def test_bar(self):
        with open('/tmp/bla') as f:
            f.read()

    # you can also skip a test method
    @unittest.skip(reason="Fails work for some reason ;) Tracked in https://github.com/stardust85/python-unittests/issues/1")
    def test_baz(self):
        assert 1 == 2
