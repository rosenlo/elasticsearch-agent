#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
Author: Rosen
Mail: rosenluov@gmail.com
File: common.py
Created Time: Mon Dec 26 15:28:28 2016
"""

import logging
from traceback import print_exc

import yaml


def load_yaml_data(filename=None):
    try:
        with open(filename, 'r') as f:
            data = yaml.load(f)
            return data
    except IOError:
        print_exc()


def logging_conf(level=logging.INFO):
    logging.basicConfig(level=level,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        # filename=filename,
                        filemode='a+'
                        )
    return logging
