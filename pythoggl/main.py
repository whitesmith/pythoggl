"""
Created by Nuno Lopes
@lopesrb from whitesmith.co
"""

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from togglwrapper import *

wrapper = TogglWrapper('','')
print(wrapper.workspaces().text)
