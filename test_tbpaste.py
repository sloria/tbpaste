# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from nose.tools import *  # PEP8 asserts
import xerox
from textblob import TextBlob
from subprocess import check_output

class TestTbPaste(unittest.TestCase):

    '''Unit tests for tbpaste'''

    def setUp(self):
        self.text = "This is a great car. I hate this ice cream, though."
        self.blob = TextBlob(self.text)
        xerox.copy(self.text)

    def test_base_command(self):
        result = run_cmd("tbpaste")
        assert_in(self.blob.sentences[0].raw, result)
        assert_in(str(round(self.blob.sentences[0].polarity, 2)), result)

    def test_sentiment(self):
        result = run_cmd("tbpaste sentiment")
        assert_in(self.blob.sentences[0].raw, result)
        sent = str(round(self.blob.sentences[0].polarity, 2))
        assert_in(sent, result)

    def test_chunks(self):
        result = run_cmd("tbpaste chunks")
        assert_in(self.blob.sentences[0].raw, result)
        np = self.blob.sentences[0].noun_phrases
        joined = ", ".join(np)
        assert_in(joined, result)

    def test_no_sentences(self):
        result = run_cmd("tbpaste --sentences=f")
        assert_in(self.text, result)
        assert_in("polarity: ", result)
        assert_in(str(round(self.blob.polarity, 2)), result)
        assert_in('subjectivity: ', result)
        assert_in(str(round(self.blob.subjectivity, 2)), result)

    def test_lang(self):
        result = run_cmd("tbpaste lang")
        assert_in("en", result)

    def test_translate(self):
        result = run_cmd("tbpaste lang --to es")
        assert_in("Este es un gran coche", result)

    def test_tags(self):
        result = run_cmd("tbpaste tag")
        assert_in("This [DT] is [VBZ] a [DT] great [JJ]", result)

def run_cmd(cmd):
    return check_output(cmd, shell=True).decode('utf-8')

if __name__ == '__main__':
    unittest.main()
