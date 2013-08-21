=======
tbpaste
=======

``tbpaste`` is a command-line utility that runs sentiment analysis on the contents of your clipboard.

Usage
-----

1. Copy some text to your clipboard.
2. Run ``tbpaste`` in your shell for the magic.

.. image:: http://i.imgur.com/npxon.gif

More magic
----------

``tbpaste sentiment``
    Run sentiment analysis. This is the default behavior (same as running ``tbpaste``). The sentiment score is within the range [-1.0, 1.0]. The subjectivity score is within the range [0.0, 1.0].

``tbpaste chunks``
    Extract noun phrases.

``tbpaste --sentences=t``
    Process each sentence in the copied text. This is the default behavior. Set ``--sentences=f`` to suppress tokenization.

``tbpaste lang``
    Detect language. `Language code reference`_.

``tbpaste lang --from en --to fr``
    Translate between languages. If ``--from`` is omitted, tbpaste will try to detect the source language. `Language code reference`_.

.. _`Language code reference`: https://developers.google.com/translate/v2/using_rest#language-params

Features
--------

* Sentiment analysis
* Noun phrase extraction
* Translation
* Colored output
* Cross-platform

Get it now
----------

::

    $ pip install -U tbpaste
    $ curl https://raw.github.com/sloria/TextBlob/master/download_corpora.py | python

You should now be able to run the ``tbpaste`` command.

Requirements
------------

- Python >= 2.7 or >= 3.3

License
-------

`MIT Licensed <http://sloria.mit-license.org>`_.