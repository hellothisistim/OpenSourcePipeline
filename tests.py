import unittest
import osp

class UnicodeTests(unittest.TestCase):

    def test_base_section_names_are_in_unicode(self):
        base_section = osp.BaseShowSection('foo', u'bar')
        self.assertTrue(type(base_section.name()) == unicode)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
