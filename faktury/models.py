from django.db import models

class Invoice(models.Model):
    cislo_faktury = models.CharField(max_length=20, unique=True)
    datum_vystavenia = models.DateField()
    datum_splatnosti = models.DateField()
    odberatel = models.CharField(max_length=255)
    suma_celkom = models.DecimalField(max_digits=10, decimal_places=2)
    stav_platby = models.CharField(max_length=20, choices=[('zaplatená', 'Zaplatená'), ('nezaplatená', 'Nezaplatená')])

    def __str__(self):
        return self.cislo_faktury

class InvoiceItem(models.Model):
    faktura = models.ForeignKey(Invoice, related_name='polozky', on_delete=models.CASCADE)
    nazov = models.CharField(max_length=255)
    mnozstvo = models.IntegerField()
    cena_za_jednotku = models.DecimalField(max_digits=10, decimal_places=2)
    sadzba_dph = models.IntegerField()

    def cena_s_dph(self):
        return self.mnozstvo * self.cena_za_jednotku * (1 + self.sadzba_dph / 100)

