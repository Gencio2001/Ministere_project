from django.db import models
from django.contrib.auth.models import User
from structures.models import Structure

class Rapport(models.Model):
    reference = models.CharField(max_length=20, unique=True, editable=False)
    date_debut = models.DateField()
    date_fin = models.DateField()
    departement = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    type_inspection = models.CharField(max_length=20, default='routine')
    
    # ÉQUIPE : Changement en ManyToMany pour autoriser plusieurs délégués
    delegues = models.ManyToManyField(User, related_name='delegue_rapports')
    membres_supplementaires = models.ManyToManyField(User, related_name='equipe_rapports', blank=True)
    
    # STRUCTURE : Changement en ManyToMany pour autoriser plusieurs structures inspectées
    type_structure = models.CharField(max_length=100)
    structures_inspectees = models.ManyToManyField(Structure, related_name='rapports_set')
    
    # Saisine et Observations
    emetteur_saisine = models.CharField(max_length=255, null=True, blank=True)
    date_saisine = models.DateField(null=True, blank=True)
    moyen_saisine = models.CharField(max_length=100, null=True, blank=True)
    motif_saisine = models.TextField(null=True, blank=True)
    observations_generales = models.TextField(null=True, blank=True)

    statut = models.CharField(max_length=20, default='BROUILLON')
    date_creation = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            last = Rapport.objects.all().order_by('id').last()
            num = (int(last.reference.split('-')[1]) + 1) if last and last.reference.startswith('RI-') else 1
            self.reference = f'RI-{num:04d}'
        super().save(*args, **kwargs)