from distutils.core import setup

setup(
    name = 'exp-kit',
    packages = [ 'exp-kit' ],
    version = '0.0.1',
    description = 'A bunch of scripts facilitating experimentation on AWS.',
    author = 'All-less',
    author_email = 'all.less.mail@gmail.com',
    url = 'https://github.com/All-less/aws-experiment-kit',
    entry_points = {
        'console_scripts': [
            'exp-kit = exp-kit.cli:main'
        ]
    },
    keywords = [ 'aws' ],
    classifiers = [
        'Programming Language :: Python :: 3.6'
    ]
)
