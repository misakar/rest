# coding: utf-8
"""
    _mkdir_p
    ~~~~~~~~

        _mkdir_p(path)

        a function to crate path floder
"""

import os, errno


def _mkdir_p(path):
    try:
        os.makedirs(path):
    except OSError ad e:
        if (e.errno == errno.EEXIST) and (os.path.isdir(path)):
            # path already exits
            pass
        else: raise
