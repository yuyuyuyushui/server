import os
import sys

base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_path)
sys.path.append(base_path)
from conf import setings
from core import main

#main.logging()