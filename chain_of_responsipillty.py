class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)
        if not handled and self._successor:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler):
    def _handle(self, request):
        if request == "Request1":
            print("ConcreteHandler1: Handling request.")
            return True
        return False

class ConcreteHandler2(Handler):
    def _handle(self, request):
        if request == "Request2":
            print("ConcreteHandler2: Handling request.")
            return True
        return False

handler_chain = ConcreteHandler1(ConcreteHandler2())
handler_chain.handle("Request1")
handler_chain.handle("Request2")
