from django.db import models
from django.utils import timezone
from core.models import Rapport 
# CORRECTION : On importe la Structure de ton app Django, pas celle de Python (ctypes)
from structures.models import Structure 

class Recommandation(models.Model):
    PRIORITE_CHOICES = [
        ('critique', 'Critique'),
        ('haute', 'Haute'),
        ('moyenne', 'Moyenne'),
        ('faible', 'Faible'),
    ]

    STATUT_CHOICES = [
        ('brouillon', 'Brouillon'),
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('soldee', 'Soldée'),
        ('non_realisee', 'Non réalisée'),
    ]

    # Identifiants et Liaisons
    reference = models.CharField(max_length=20, unique=True, verbose_name="Référence Reco")
    # Utilisation de ManyToMany pour lier plusieurs rapports
    rapports_lies = models.ManyToManyField(Rapport, related_name='recommandations')
    
    # Contenu de la recommandation
    titre = models.CharField(max_length=255)
    constat = models.TextField(verbose_name="Constat / Problème")
    recommandation_detaillee = models.TextField()
    
    # Paramètres de suivi
    # Augmentation de max_length à 20 par précaution pour les choix
    priorite = models.CharField(max_length=20, choices=PRIORITE_CHOICES, default='moyenne')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='brouillon')
    
    # Responsabilités (Plusieurs structures possibles)
    structures_responsables = models.ManyToManyField(Structure, related_name='recommandations_a_charger')
    date_echeance = models.DateField()
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Recommandation"
        verbose_name_plural = "Recommandations" # Pour un affichage propre dans l'admin
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.reference} - {self.titre}"

    def est_en_retard(self):
        """Vérifie si l'échéance est dépassée pour une reco non soldée"""
        return self.date_echeance < timezone.now().date() and self.statut != 'soldee'