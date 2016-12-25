#!/usr/bin/env python
# encoding: utf-8

"""
Author: Rosen
Mail: rosenluov@gmail.com
File: daemonize.py
Created Time: 12/22/16 00:05
"""

from __future__ import print_function

import atexit
import os
import sys
import time
from datetime import datetime
from signal import SIGTERM

from utils.logging_conf import logging_conf


class Daemon(object):
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
        self.es_logger_out = logging_conf(stdout).getLogger('es_agent_out')
        self.es_logger_err = logging_conf(stderr).getLogger('es_agent_err')

    def _daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            self.es_logger_err.error('For #1 failed: %s  %s \n', (e.errno, e.strerror))
            sys.exit(1)

        os.chdir("/")  # 修改工作目录
        os.setsid()  # 设置新的会话连接
        os.umask(0)  # 重新设置文件创建权限

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            self.es_logger_err.error('Fork #2 failed: %s %s\n', (e.errno, e.strerror))
            sys.exit(1)

        # 重定向文件描述符
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # 注册退出函数，根据文件pid判断是否存在进程
        atexit.register(self.delpid)
        pid = str(os.getpid())
        open(self.pidfile, 'w+').write('{}\n'.format(pid))

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        # 检查pid文件是否存在以探测是否存在进程
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = 'pidfile %s already exist. Daemon already running!\n'
            self.es_logger_err.error(message, self.pidfile)
            sys.exit(1)

            # 启动监控
        self._daemonize()
        self.run()

    def stop(self):
        # 从pid文件中获取pid
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
            message = 'es_agent will be stop...\n'
            self.es_logger_out.info(message)
        except IOError:
            pid = None

        if not pid:  # 重启不报错
            message = 'pid file %s does not exist. Daemon not running!\n'
            self.es_logger_err.error(message, self.pidfile)
            return

            # 杀进程
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                self.es_logger_err.error(str(err))
                sys.exit(1)

    def restart(self):
        self.stop()
        self.start()

    @staticmethod
    def run():
        pass


if __name__ == '__main__':
    pass
