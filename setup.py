from setuptools import setup, find_packages

setup(
    name = 'expkit',
    packages = find_packages(),
    version = '0.0.1',
    description = 'A bunch of scripts facilitating experimentation on AWS.',
    author = 'All-less',
    author_email = 'all.less.mail@gmail.com',
    url = 'https://github.com/All-less/aws-experiment-kit',
    entry_points = {
        'console_scripts': [
            'expkit=expkit.cli:main'
        ]
    },
    keywords = [ 'aws' ],
    classifiers = [
        'Programming Language :: Python :: 3.6'
    ]
)
