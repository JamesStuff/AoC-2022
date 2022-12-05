import time


def tim(func):
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("\nProcessing time of %s():\t%.6f ms."
              % (func.__qualname__, (time.time() - start_time)*1000))
        return result

    return measure_time