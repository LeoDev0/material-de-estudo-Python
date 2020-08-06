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
        """
        Essa sintaxe <ClassName>.<attribute> deve ser usada para referenciar
        atributos de classe fora do escopo da classe (ex: funções em outra
        parte do programa) pois o uso do self nesse caso poderia causar um
        problema de "prioridade" no caso de existir um atributo de instância
        com o mesmo nome "tax".
        E também, trocar o valor desse atributo de classe usando self,
        o valor só vai ser trocado dentro dessa instância e não em todas
        as classes. É como se vc transformasse esse atributo de classe
        em um atributo de instância.
        """
        return amount * CashRegister.tax
        # return amount * self.tax  # Sintaxe errada
        
register = CashRegister("Melanie", "3453513")
register.display_total(5022.5)
