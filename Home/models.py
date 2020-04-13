from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    DEPARTMENTS = [
        ('MF', 'Üretim'),
        ('SH', 'Nakliye'),
        ('AD', 'Yönetim'),
        ('HR', 'İnsan Kaynakları'),
        ('RD', 'AR-GE')
    ]

    dept = models.CharField(max_length=2, choices=DEPARTMENTS, default=DEPARTMENTS[3][0])
