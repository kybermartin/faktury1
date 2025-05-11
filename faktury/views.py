from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Invoice
from .forms import InvoiceForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.core.mail import EmailMessage

def index(request):
    faktury = Invoice.objects.all()
    return render(request, 'faktury/index.html', {'faktury': faktury})

def detail(request, faktura_id):
    faktura = get_object_or_404(Invoice, id=faktura_id)
    return render(request, 'faktury/detail.html', {'faktura': faktura})

def export_pdf(request, faktura_id):
    faktura = get_object_or_404(Invoice, id=faktura_id)
    template = get_template('faktury/pdf_sablona.html')
    html = template.render({'faktura': faktura})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="faktura_{faktura.cislo_faktury}.pdf"'
    pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=response)
    return response

def posli_email(request, faktura_id):
    faktura = get_object_or_404(Invoice, id=faktura_id)
    template = get_template('faktury/pdf_sablona.html')
    html = template.render({'faktura': faktura})
    result = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)
    email = EmailMessage(
        subject=f"Faktúra {faktura.cislo_faktury}",
        body="V prílohe nájdete faktúru.",
        from_email='spak.martin@gmail.com',
        to=['spak.martin@gmail.com']
    )
    email.attach(f'faktura_{faktura.cislo_faktury}.pdf', result.getvalue(), 'application/pdf')
    email.send()
    return HttpResponse("Email odoslaný")

def nova_faktura(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InvoiceForm()
    return render(request, 'faktury/formular.html', {'form': form})

def upravit_fakturu(request, faktura_id):
    faktura = get_object_or_404(Invoice, id=faktura_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=faktura)
        if form.is_valid():
            form.save()
            return redirect('detail', faktura_id=faktura.id)
    else:
        form = InvoiceForm(instance=faktura)
    return render(request, 'faktury/formular.html', {'form': form})
