import ctypes
import sys
import traceback


def trace(func, filename, line, method, self, mglo, args):
    # print('%s:%d %s%r' % (filename, line, func, args), ctypes.windll.opengl32.glGetError())
    pass


def _trace(*args):
    try:
        trace(*args)
    except:
        sys.last_type, sys.last_value, last_tb = ei = sys.exc_info()
        sys.last_traceback = last_tb
        try:
            lines = traceback.format_exception(ei[0], ei[1], last_tb.tb_next)
            if sys.excepthook is sys.__excepthook__:
                sys.stderr.write(''.join(lines))
            else:
                sys.excepthook(ei[0], ei[1], last_tb)
        finally:
            last_tb = ei = None
