import io
import base64
from django.shortcuts import render
from django.db.models import Sum
import requests
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from .models import Currency
from .forms import TransactionForm
from .models import Transaction
import xml.etree.ElementTree as ET
from django.http import HttpResponse


def my_view(request):
    if request.method == "GET":
        url = "http://api.nbp.pl/api/exchangerates/tables/A/"
        response = requests.get(url, headers={"Accept": "application/xml"})

        if response.status_code == 200:
            try:
                root = ET.fromstring(response.content)
                rates = []
                for rate_element in root.findall(".//Rate"):
                    currency = rate_element.find("Currency").text
                    code = rate_element.find("Code").text
                    mid = rate_element.find("Mid")

                    if mid is not None:
                        mid = float(mid.text)
                    else:
                        mid = None
                    currenc, created = Currency.objects.get_or_create(symbol=code)
                    currenc.name = currency
                    currenc.price = mid
                    currenc.save()

                currencies = Currency.objects.all()

                return render(request, "currency_list.html", {"currencies": currencies})
            except ET.ParseError as e:
                return HttpResponse(f"Błąd parsowania XML: {e}")
        else:
            return HttpResponse("Błąd podczas pobierania danych z API")

    return HttpResponse("Nieobsługiwany typ żądania")


def wallet(request):
    transactions = Transaction.objects.all()
    latest_transaction = transactions.latest("id") if transactions else None

    names = transactions.values_list("name", flat=True).distinct()

    name_quantity_amount = []
    for name in names:
        quantity = (
            transactions.filter(name=name).aggregate(Sum("quantity"))["quantity__sum"]
            or 0
        )
        amount = (
            transactions.filter(name=name).aggregate(Sum("amount"))["amount__sum"] or 0
        )
        name_quantity_amount.append((name, quantity, amount))

    labels = [name for name, _, _ in name_quantity_amount]

    sums = [quantity * amount for _, quantity, amount in name_quantity_amount]

    fig, ax = plt.subplots()
    ax.pie(sums, labels=labels, autopct="%1.1f%%")
    ax.set_title("The percentage of your wallet")

    canvas = FigureCanvas(fig)
    buffer = io.BytesIO()
    canvas.print_png(buffer)
    buffer.seek(0)
    chart_url = base64.b64encode(buffer.getvalue()).decode()

    name_quantity_amount_with_sums = [
        (name, quantity, amount, quantity * amount)
        for name, quantity, amount in name_quantity_amount
    ]

    return render(
        request,
        "wallet.html",
        {
            "transactions": transactions,
            "latest_transaction": latest_transaction,
            "chart_url": chart_url,
            "name_quantity_amount": name_quantity_amount_with_sums,
        },
    )


def add(request):
    currency = Currency.objects.all()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            if transaction.type == "BUY":
                transaction.quantity = abs(transaction.quantity)
            elif transaction.type == "SELL":
                transaction.quantity = -abs(transaction.quantity)
            transaction.save()
            return render(request, "add.html", {"currency": currency})
    else:
        form = TransactionForm()
    return render(request, "add.html", {"currency": currency})
