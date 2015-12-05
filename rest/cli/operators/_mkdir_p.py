# coding: utf-8
"""
    _mkdir_p
    ~~~~~~~~

        _mkdir_p(path)
        _mkdir_p(path) function (:sys mkdir -p path:)
"""

import os, errno


def _mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if (e.errno == errno.EEXIST) and (os.path.isdir(path)):
            # path already exits
            # we do not need error msg
            pass
        else: raise
