from django.shortcuts import render, redirect
from app.models import Coffee, Transaction
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        home = Coffee.objects.all()
        return render(request, "app/coffee_list.html", {"coffees": home})


class TransactionDetail(View):
    def get(self, request, id):
        purchases = Transaction.objects.get(id=id)
        return render(
            request, "app/transaction_detail.html", {"transaction": purchases}
        )


class BuyCoffee(View):
    def post(self, request, id):
        home = Coffee.objects.get(id=id)
        t = Transaction.objects.create(item=home, pre_tax=home.price, tax=home.price * 0.07)
        return redirect("transaction_detail", t.id)
