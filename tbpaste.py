#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''tbpaste

Usage:
    tbpaste [<command>] [options]
    tbpaste sentiment [options]
    tbpaste chunks [options]
    tbpaste lang
    tbpaste lang [--from <lang1> --to <lang2>]
    tbpaste tag

Options:
    -h --help               Show this screen.
    -v --version            Show version.
    -s --sentences=(t|f)    Whether to break up text into sentence [default: t].
    -f --from <lang1>       The language to translate from
    -t --to <lang2>         The language to translate to
'''

from __future__ import unicode_literals, print_function
import sys
import xerox
from text.blob import TextBlob as tb
from docopt import docopt
from clint.textui import puts, colored

__version__ = '0.2.0'
__author__ = 'Steven Loria'
__license__ = "MIT"

# 2/3 Compatiblity
PY2 = sys.version_info[0] == 2
if PY2:
    unicode = unicode
else:
    unicode = str

THRESHOLDS = {
    'positive': (0.1, 'green'),
    'negative': (-0.1, 'red')
}

NEUTRAL_COL = 'blue'

def main():
    '''Main entry point for the tbpaste CLI.'''
    args = docopt(__doc__, version=__version__)
    command = args["<command>"]
    text = unicode(xerox.paste())
    blob = tb(text)
    tokenize = 't' in args['--sentences'].lower()
    if command == 'lang' or args['--to'] or args['--from']:
        return lang(blob, from_lang=args['--from'], to=args['--to'])
    elif command == 'chunks':
        return chunks(blob, tokenize)
    elif command == 'tag':
        return tag(blob)
    else:
        return sentiment(blob, tokenize)
    sys.exit(0)

def color_sent(text, polarity):
    '''Color text based on polarity score.'''
    if polarity < THRESHOLDS['negative'][0]:
        return getattr(colored, THRESHOLDS['negative'][1])(text)
    elif polarity > THRESHOLDS['positive'][0]:
        return getattr(colored, THRESHOLDS['positive'][1])(text)
    else:
        return getattr(colored, NEUTRAL_COL)(text)

def sentiment(blob, tokenize=True):
    '''Output sentiment analysis.'''
    if tokenize:
        for s in blob.sentences:
            formatted_polarity = numformat(s.polarity)
            formatted_subjectivity = numformat(s.subjectivity)
            print(s.raw)
            output = " polarity: {0}, subjectivity: {1}"\
                            .format(formatted_polarity, formatted_subjectivity)
            puts(color_sent(output, s.polarity))
    else:
        print(blob.raw)
        print('')
        puts("Overall sentiment:")
        formatted_polarity = numformat(blob.polarity)
        formatted_subjectivity = numformat(blob.subjectivity)
        puts("polarity: " + color_sent(formatted_polarity, blob.polarity))
        puts("subjectivity: " + color_sent(formatted_subjectivity, blob.polarity))
    return None

def chunks(blob, tokenize=True):
    '''Output noun phrases.'''
    if tokenize:
        for s in blob.sentences:
            print(s.raw)
            print(colored.yellow("chunks: " + " | ".join(s.noun_phrases)))
    else:
        print(blob.raw)
        print("")
        puts("Chunks:")
        for np in set(blob.noun_phrases):
            print(colored.yellow("* {0}".format(np)))
    return None

def lang(blob, from_lang=None, to=None):
    '''Output language translation/detection.'''
    if from_lang and to:
        print(unicode(blob.translate(from_lang=from_lang, to=to)))
    elif from_lang and not to:
        print(unicode(blob.translate(from_lang=from_lang, to="en")))
    elif to and not from_lang:
        detected = blob.detect_language()
        print(unicode(blob.translate(from_lang=detected, to=to)))
    else:
        print(blob.detect_language())
    return None

def tag(blob):
    '''Output POS tags.'''
    for word, tag in blob.tags:
        print(word +  " " + colored.yellow("[{tag}] ".format(tag=tag)), end="")
    print()

def numformat(num):
    return unicode(str((round(num, 2))))

if __name__ == '__main__':
    main()
