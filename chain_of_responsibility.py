# Chain of Responsibility

"""
  Chain of Responsibility֊ն  behavioral design pattern է, որը թույլ է տալիս փոխանցել հարցում հաջորդաբար մշակման շղթայով։
  Ամեն փուլում հաջորդ մշակողը որոշվում է հնարավոր կլինի մշակել հարցումը, թե փոխանցել հաջորդին։

"""

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request < 10:
            return f"Handled by 1: {request}"
        return super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if 10 <= request < 20:
            return f"Handled by 2: {request}"
        return super().handle(request)

chain = ConcreteHandler1(ConcreteHandler2(Handler()))

for request in [5, 10, 15, 25]:
    print(chain.handle(request))

