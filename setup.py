import sys
import subprocess

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PUBLISH_CMD = "python setup.py register sdist bdist_wheel upload"
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist bdist_wheel upload -r test'
TEST_CMD = 'nosetests'

if 'publish' in sys.argv:
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'run_tests' in sys.argv:
    try:
        __import__('nose')
    except ImportError:
        print('nose required. Run `pip install nose`.')
        sys.exit(1)

    status = subprocess.call(TEST_CMD, shell=True)
    sys.exit(status)

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='tbpaste',
    version="0.2.0",
    description='Sentiment analysis, as easy as copy-and-paste',
    long_description=read("README.rst"),
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/tbpaste',
    py_modules=['tbpaste'],
    install_requires=[
        'docopt',
        'clint',
        'textblob',
        'xerox'
    ],
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    test_suite='tests',
    tests_require=['nose', 'xerox', 'textblob'],
    entry_points={
        'console_scripts': [
            "tbpaste = tbpaste:main"
        ]
    },
)