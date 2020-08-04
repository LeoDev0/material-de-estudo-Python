class CashRegister:

    tax = 0.05

    def __init__(self, cashier, serial):
        self.cashier = cashier
        self._serial = serial

    @property
    def serial(self):
        return self._serial

    def display_total(self, subtotal):
        print("=== Welcome to our store ===")
        print("The subtotal is:", subtotal)
        print("The tax is:", self._calculate_tax(subtotal))  # Para chamar métodos dentro de outros métodos é necessário usar o self.
        print("-----------------------")
        print("The total is:", self._calculate_total(subtotal))

    """
    Helper function protegida. Só deve ser utilizada dentro da classe
    para ser chamada dentro do método 'display_total', e não diretamente.
    """
    def _calculate_total(self, subtotal):
        return subtotal + self._calculate_tax(subtotal)

    """Helper function protegida"""
    def _calculate_tax(self, amount):
        # return amount * CashRegister.tax  # Essa é outra possibilidade para referenciar a classe que não usando o self: colocando diretamente o nome da classe.
        return amount * self.tax
        
register = CashRegister("Melanie", "3453513")
register.display_total(5022.5)
