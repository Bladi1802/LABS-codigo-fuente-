from abc import ABC, abstractmethod


# 1. Interfaz (Contrato)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float, account: str):
        pass


# 2. Implementaciones concretas
class PayPalPayment(PaymentMethod):
    def pay(self, amount: float, account: str):
        print(f"Procesando pago de ${amount:.2f} con PayPal para la cuenta {account}")


class StripePayment(PaymentMethod):
    def pay(self, amount: float, account: str):
        print(f"Procesando pago de ${amount:.2f} con Stripe para la cuenta {account}")


# 3. Clase de alto nivel
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: float, account: str):
        self.payment_method.pay(amount, account)


# 4. Uso del sistema
if __name__ == "__main__":
    paypal_processor = PaymentProcessor(PayPalPayment())
    paypal_processor.process_payment(150.00, "cliente_paypal@example.com")

    stripe_processor = PaymentProcessor(StripePayment())
    stripe_processor.process_payment(299.99, "cliente_stripe@example.com")


