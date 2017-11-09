
import sys, os

file = sys.argv[0]
pathname = os.path.dirname(file)
print ('running from %s' % os.path.abspath(pathname))
print ('file is %s' % file)