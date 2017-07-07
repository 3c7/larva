from setuptools import setup

setup(
    name='Larva',
    version='0.2',
    py_modules=['larva', 'configurator', 'connector', 'writer', 'commander', 'commands'],
    install_requires=[
        'Click',
        'thehive4py',
        'termcolor'
    ],
    entry_points='''
        [console_scripts]
        larva=larva:larva
    '''
)
