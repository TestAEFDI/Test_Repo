import os

HERE = os.path.dirname(__file__)
with open(os.path.join(HERE, 'VERSION'), 'r', encoding='utf-8') as f:
    version = f.readlines()[0].strip()

__version__ = version
