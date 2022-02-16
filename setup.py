from setuptools import setup

setup(
    name='hello',
    version='0.1.0',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'greet = hello:hello',
        ],
    },
)
