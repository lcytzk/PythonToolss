#!/usr/bin/env python

import os,sys
import time
import atexit


class Daemon(object):

    def __init__(self, pidfile, stdin='/dev/null', stdout='std.out', stderr='std.err'):
	self.stdin = stdin
	self.stdout = stdout
	self.stderr = stderr
	self.pidfile = pidfile

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

	os.chdir("/home/liangchenye/daemon")
        os.setsid()
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

	sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

	atexit.register(self.delpid)
        pid = str(os.getpid())
	file(self.pidfile,'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
	try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

	if pid:
	    message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        self.daemonize()
        self.run()

    def run(self):
        count = 0
        while True:
            sys.stdout.write("alive\n")
            sys.stdout.flush()
            time.sleep(3)
            count += 1
            if count == 10:
                break

def test():
    d = Daemon('test.pid')
    d.start()

if __name__ == '__main__':
    test()
