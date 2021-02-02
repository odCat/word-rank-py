#!python

#   Copyright 2021 Mihai Gătejescu
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import unittest
import rankpy

class RankTests(unittest.TestCase):

    def test_read_from_file(self):
        data = rankpy.read_from_file('sample.txt')
        expected = (' casă, masă:  “carte”.\nsă-mi,\n- Linie de ‘dialog’' +
                    '\ncasă - masă?\ncasă parte!\n\npasă -parte\n\nte-\n' +
                    "levizor\n\"televizor\"\n'și'\n")
        self.assertEqual(data, expected)

    def test_remove_punctuation(self):
        data = rankpy.read_from_file('sample.txt')
        expected = (' casă masă  carte\nsă-mi\n Linie de dialog' +
                    '\ncasă  masă\ncasă parte\n\npasă parte\n\n'
                    'televizor\ntelevizor\nși\n')
        self.assertEqual(rankpy.remove_punctuation(data), expected)

    def test_text_to_list(self):
        data = rankpy.read_from_file('sample.txt')
        data = rankpy.text_to_list(data)
        expected = ['casă', 'masă', 'carte', 'să-mi', 'Linie', 'de',
                    'dialog', 'casă', 'masă', 'casă', 'parte', 'pasă',
                    'parte', 'televizor', 'televizor', 'și']
        self.assertEqual(data, expected)

    def test_sort_dictionary(self):
        data = {
                "key1": 1,
                "key2": 4,
                "key3": 2
                }
        data = rankpy.sort_dictionary(data)
        expected = {
                "key2": 4,
                "key3": 2,
                "key1": 1
                }
        self.assertEqual(data.keys(), expected.keys())

    def test_word_frequency(self):
        data = rankpy.read_from_file('sample.txt')
        data = rankpy.text_to_list(data)
        data = rankpy.word_frequency(data)
        expected = {
                "casă": 3,
                "masă": 2,
                "carte": 1,
                "să-mi": 1,
                "Linie": 1,
                "de": 1,
                "dialog": 1,
                "pasă": 1,
                "parte": 2,
                "televizor": 2,
                "și": 1
                }
        self.assertEqual(data, expected)

    def test_make_printable(sefl):
        data = {
                "key2": 4,
                "key3": 2,
                "key1": 1
                }
        data = rankpy.make_printable(data)
        expected = ('key2: 4\nkey3: 2\nkey1: 1\n')

if __name__ == '__main__':
    unittest.main()
