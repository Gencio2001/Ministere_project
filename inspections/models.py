from django.db import models

class Rapport(models.Model):
    STATUS_CHOICES = [
        ('Brouillon', 'Brouillon'),
        ('Transmis', 'Transmis'),
        ('Validation', 'En attente de validation'),
    ]

    reference = models.CharField(max_length=20, unique=True)
    date_inspection = models.DateField()
    structure = models.CharField(max_length=255)
    type_rapport = models.CharField(max_length=100) # ex: Routine
    departement = models.CharField(max_length=100)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Brouillon')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference} - {self.structure}"