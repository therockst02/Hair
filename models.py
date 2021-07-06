from django.db import models

class Saloni(models.Model):
    NomeSalone = models.CharField(max_length = 30)
    Indirizzo = models.CharField(max_length = 50)
    Cittá = models.CharField(max_length = 40)
    Descrizione = models.CharField(max_length = 200)
    Immagine = models.ImageField()
    RecapitoTelefonico = models.CharField(max_length = 11)
    ORARI = (
            ('07:00:00', '07:00:00'),
            ('07:30:00', '07:30:00'),
            ('08:00:00', '08:00:00'),
            ('08:30:00', '08:30:00'),
            ('09:00:00', '09:00:00'),
            ('09:30:00', '09:30:00'),
            ('10:00:00', '10:00:00'),
            ('10:30:00', '10:30:00'),
            ('11:00:00', '11:00:00'),
            ('11:30:00', '11:30:00'),
            ('12:00:00', '12:00:00'),
            ('12:30:00', '12:30:00'),
            ('01:00:00', '01:00:00'),
            ('01:30:00', '01:30:00'),
            ('03:00:00', '03:00:00'),
            ('03:30:00', '03:30:00'),
            ('04:00:00', '04:00:00'),
            ('04:30:00', '04:30:00'),
            ('05:00:00', '05:00:00'),
            ('05:30:00', '05:30:00'),
            ('06:00:00', '06:00:00'),
            ('06:30:00', '06:30:00'),
            ('07:00:00', '07:00:00'),
            ('07:30:00', '07:30:00'),
            ('08:00:00', '08:00:00'),
            ('08:30:00', '08:30:00'),
    )
    OrarioAperturaMattino = models.CharField(max_length = 11, choices = ORARI)
    OrarioChiusurMattino = models.CharField(max_length = 11, choices = ORARI)
    OrarioAperturaPomeriggio = models.CharField(max_length = 11, choices = ORARI)
    OrarioChiusuraPomeriggio = models.CharField(max_length = 11, choices = ORARI)
    class Meta:
         verbose_name = "Salone"
         verbose_name_plural = "Saloni"
    def __str__(self):
        return self.NomeSalone

class Iva(models.Model):
    IVA = (
            ('22%', '22 Percento'),
    )
    Percentuale = models.CharField(max_length = 3, choices = IVA)
    class Meta:
         verbose_name = "Iva"
         verbose_name_plural = "Iva"
    def __str__(self):
        return self.Percentuale

class Trattamenti(models.Model):
    TipoTrattamento = models.CharField(max_length = 40)
    CostoEsentasse = models.PositiveIntegerField()
    IdIva = models.ForeignKey(Iva, null = True, on_delete=models.SET_NULL)
    Descrizione = models.TextField(max_length = 200)
    class Meta:
         verbose_name = "Trattamento"
         verbose_name_plural = "Trattamenti"
    def __str__(self):
        return self.TipoTrattamento

class Dipendenti(models.Model):
    Salone = models.ForeignKey(Saloni, null = True, on_delete=models.SET_NULL)
    Cognome = models.CharField(max_length = 30)
    Nome = models.CharField(max_length = 30)
    SEX = (
            ('F','Femmina'),
            ('M','Maschio'),
            ('U','Non sicuro'),
    )
    Sesso = models.CharField(max_length = 1, choices = SEX)
    DataNascita = models.DateField()
    Indirizzo = models.CharField(max_length = 50)
    RecapitoTelefonico = models.CharField(max_length = 11)
    Email = models.EmailField()
    DocumentoIdentitá = models.CharField(max_length = 9)
    class Meta:
         verbose_name = "Dipendente"
         verbose_name_plural = "Dipendenti"
    def __str__(self):
        return self.Cognome

class Clienti(models.Model):
    Cognome = models.CharField(max_length = 30)
    Nome = models.CharField(max_length = 30)
    SEX = (
            ('F','Femmina'),
            ('M','Maschio'),
            ('U','Non sicuro'),
    )
    Sesso = models.CharField(max_length = 1, choices = SEX)
    DataNascita = models.DateField()
    Indirizzo = models.CharField(max_length = 50)
    RecapitoTelefonico = models.CharField(max_length = 11)
    Email = models.EmailField()
    DocumentoIdentitá = models.CharField(max_length = 9)
    class Meta:
         verbose_name = "Cliente"
         verbose_name_plural = "Clienti"
    def __str__(self):
        return self.Cognome
       
class Appuntamenti(models.Model):
      Id_Salone = models.ForeignKey(Saloni,null = True, on_delete=models.SET_NULL)
      Id_Trattamento = models.ForeignKey(Trattamenti, null = True, on_delete=models.SET_NULL)
      Id_Dipendente = models.ForeignKey(Dipendenti, null = True, on_delete=models.SET_NULL)
      Data = models.DateField()
      Ora = models.TimeField()
      class Meta:
         verbose_name = "Appuntamento"
         verbose_name_plural = "Appuntamenti"
      def __str__(self):
        return self.Id_Salone.NomeSalone + "/" + str(self.Data) + "/" + str(self.Ora)

class FeedbackCliente(models.Model):
    Id_Appuntamento = models.ForeignKey(Appuntamenti, null = True, on_delete=models.CASCADE)
    STELLE = (
            ('1', '1 Stella'),
            ('2', '2 Stelle'),
            ('3', '3 Stelle'),
            ('4', '4 Stelle'),
            ('5', '5 Stelle'),

    )
    Stelle = models.CharField(max_length = 8, choices = STELLE)
    class Meta:
         verbose_name = "Feedback"
         verbose_name_plural = "Feedback"
    



