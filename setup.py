from setuptools import setup

setup(
    name='mist_tools',
    version='0.1',
    py_modules=['mist_tools'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mist_tools=mist_tools:cli
    ''',
)