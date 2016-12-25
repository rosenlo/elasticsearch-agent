#!/usr/bin/env python
# encoding: utf-8

"""
Author: Rosen
Mail: rosenluov@gmail.com
File: logging_conf.py
Created Time: 12/22/16 17:49
"""

import logging


def logging_conf(filename='/dev/null', level=logging.INFO):
    logging.basicConfig(level=level,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=filename,
                        filemode='a+'
                        )
    return logging
