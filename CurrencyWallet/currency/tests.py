from django.test import TestCase
from django.urls import reverse
from .models import Currency, Transaction


class CurrencyTestCase(TestCase):
    def test_currency_creation(self):
        currency = Currency.objects.create(name="USD", symbol="USD", price=1.0)
        self.assertEqual(currency.name, "USD")
        self.assertEqual(currency.symbol, "USD")
        self.assertEqual(currency.price, 1.0)


class TransactionTestCase(TestCase):
    def test_transaction_creation(self):
        transaction = Transaction.objects.create(
            name="USD", type="BUY", quantity=1.0, amount=50000.0
        )
        self.assertEqual(transaction.name, "USD")
        self.assertEqual(transaction.type, "BUY")
        self.assertEqual(transaction.quantity, 1.0)
        self.assertEqual(transaction.amount, 50000.0)


class MyViewTestCase(TestCase):
    def setUp(self):
        Currency.objects.create(name="USD", symbol="USD", price=1.0)
        Currency.objects.create(name="EUR", symbol="EUR", price=1.2)

    def test_my_view(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "currency_list.html")
        self.assertContains(response, "USD")
        self.assertContains(response, "EUR")


class WalletTestCase(TestCase):
    def setUp(self):
        Transaction.objects.create(name="USD", type="BUY", quantity=1.0, amount=1000.0)
        Transaction.objects.create(name="EUR", type="BUY", quantity=2.0, amount=2400.0)

    def test_wallet(self):
        response = self.client.get(reverse("wallet"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wallet.html")
        self.assertContains(response, "USD")
        self.assertContains(response, "EUR")


class AddTestCase(TestCase):
    def test_add(self):
        response = self.client.get(reverse("add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add.html")
