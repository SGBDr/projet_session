"""
Error implamentaion : phase 2
"""

class ErreurDate(RuntimeError):
    """
    Erreur Date exeption
    """
    def __init__(self, message="Date error, date are upperthan today date"):
        self.message = message
        super().__init__(self.message)

class ErreurQuantite(RuntimeError):
    """
    Erreur Qantity exeption
    """
    def __init__(self, message="Quantity error"):
        self.message = message
        super().__init__(self.message)

class LiquiditeInsuffisante(RuntimeError):
    """
    Erreur Liquidity exeption
    """
    def __init__(self, message="Insuffisant liquidity"):
        self.message = message
        super().__init__(self.message)
