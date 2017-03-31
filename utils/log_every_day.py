#!/usr/bin/env python

from subprocess import Popen, PIPE
import logging
import logging.handlers

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

f = logging.Formatter(fmt='%(levelname)s:%(name)s:(%(asctime)s; %(filename)s:%(lineno)d)  %(message)s ',
        datefmt="%Y-%m-%d %H:%M:%S")

hs = [
    logging.handlers.TimedRotatingFileHandler('test.log', when='D', interval=1, backupCount=0, encoding='utf8')
]

for h in hs:
    h.setFormatter(f)
    h.setLevel(logging.DEBUG)
    root_logger.addHandler(h)

def log_subprocess_output(pipe):
    for line in iter(pipe.readline, ''):
        logging.info(line)

def execcmd(cmd):
    logging.info(cmd)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    with p.stdout:
        log_subprocess_output(p.stdout)
    p.wait()
    return p.returncode

def main():
    execcmd("echo 123")

if __name__ == '__main__':
    main()
