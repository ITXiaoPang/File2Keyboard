# -*- coding: utf-8 -*-
__author__ = 'ITXiaoPang'

from functools import wraps
import sys
import os
import autopy
import time

keys_with_shift = '`!@#%^&*()_+{}|:"<>?'

def toggle_key(my_toggle_key):
    def decorator(fn):
        @wraps(fn)
        def wrapper(myText):
            for v in myText:
                if v in keys_with_shift:
                    autopy.key.toggle(my_toggle_key,True)
                fn(v)
                if v in keys_with_shift:
                    autopy.key.toggle(my_toggle_key,False)
        return wrapper
    return decorator


@toggle_key(autopy.key.K_SHIFT)
def type_text(myText):
    for v in myText:
        autopy.key.type_string(v)


if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]):
    for v in range(5,0,-1):
        print(v)
        time.sleep(1)
    try:
        f = open(sys.argv[1])
        current_line = f.readline()
        while current_line:
            type_text(current_line)
            current_line = f.readline()
    except Exception,e:
        print(e)
    finally:
        if 'f' in dir():
            f.close()