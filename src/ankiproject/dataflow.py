#from functools import reduce, partial
#from itertools import chain

#def compose(*functions):
#    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

class DataFlow:
    def __init__(self, meta = {}, data = [], pipeline = []):
        self.meta = meta
        self.data = data
        self.pipeline = pipeline

    def run(self):
        for item in self.data:
            results = [item]
            for func in self.pipeline:
                kwargs = {}
                argnames = func.__code__.co_varnames
                for key, value in self.meta.items():
                    if key in argnames:
                        kwargs[key] = value
                results = func(results, **kwargs)
            for result in results:
                yield result
