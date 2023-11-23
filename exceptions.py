"""
Error implamentaion : phase 2
"""

class ErreurDate(RuntimeError):
    def __init__(self, message="Date error, date are upperthan today date"):
        self.message = message
        super().__init__(self.message)

class ErreurQuantite(RuntimeError):
    def __init__(self, message="Quantity error"):
        self.message = message
        super().__init__(self.message)

class LiquiditeInsuffisante(RuntimeError):
    def __init__(self, message="Insuffisant liquidity"):
        self.message = message
        super().__init__(self.message)