from setuptools import setup, find_packages

setup(
    name='Larva',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'Click',
        'thehive4py',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'larva=larva.larva:larva'
        ]
    }
)
