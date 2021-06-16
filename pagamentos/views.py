import mercadopago
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings


# Create your views here.
def process(request):
    if request.method == "POST":
        sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_KEY)

        payment_data = {
            "transaction_amount": float(request.POST.get("transactionAmount")), #valo total
            "token": request.POST.get("token"),  #
            "description": request.POST.get("description"),
            "installments": 1,  #int(request.POST.get("installments")),
            "payment_method_id": request.POST.get("paymentMethodId"),
            "payer": {
                "email": request.POST.get("email"),
                "identification": {
                    "type": request.POST.get("docType"),
                    "number": request.POST.get("cardNumber")
                }
            }
        }

        payment = sdk.payment().create(payment_data)
        if payment['status'] == 201:
            if payment['response']['status'] == 'approved':
                return redirect('sucesso')
            else:
                return HttpResponse('Erro nos pagamentos')
        else:
            return HttpResponse('Erro')
    return render(request, 'form_pagamento.html')


def sucesso(request):
    return render(request, 'sucesso.html')
