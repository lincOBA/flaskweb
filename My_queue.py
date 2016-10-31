class que:
    def __init__(self):
        def F():
            return
        self.f=F
        self.fF = self.f()
    def put(self, n):
        if self.f():
            f = self.f
            def r():
                yield from f()
                yield n
            self.f = r
            self.fF = self.f()
        else:
            def r():
                yield n
            self.f = r
            self.fF = self.f()
    def push(self):
        try:
            result = self.fF.send(None)
            return result
        except:
            return None
if __name__ == "__main__":
    
    q = que()
    q.put(2)
    print(q.push())
