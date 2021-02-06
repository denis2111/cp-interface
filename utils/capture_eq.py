class CaptureEq:
    'Object wrapper that remembers "other" for successful equality tests.'

    def __init__(self, obj):
        self.obj = obj
        self.match = obj

    def __hash__(self):
        return hash(self.obj)

    def __eq__(self, other):
        result = (self.obj == other)
        if result:
            self.match = other
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getattr__(self, name):  # support hash() or anything else needed by __contains__
        return getattr(self.obj, name)
