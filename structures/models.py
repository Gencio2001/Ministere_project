from django.db import models
from django.contrib.auth.models import User

class Structure(models.Model):
    TYPE_CHOICES = [
        ('direction', 'Direction Centrale'),
        ('service', 'Service Déconcentré'),
        ('etablissement', 'Établissement Public'),
    ]

    code = models.CharField(max_length=20, unique=True, editable=False)
    nom = models.CharField(max_length=255)
    type_structure = models.CharField(max_length=50, choices=TYPE_CHOICES)
    departement = models.CharField(max_length=100)
    
    # On utilise 'responsable' comme nom de champ technique
    responsable = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Responsable de la structure",
        related_name="structures_gerees"
    )
    
    # Cette propriété permet à ton template d'afficher le nom complet 
    # via {{ st.responsable_nom }} sans changer ton code HTML actuel
    @property
    def responsable_nom(self):
        if self.responsable:
            return f"{self.responsable.last_name} {self.responsable.first_name}"
        return "Non défini"

    est_operationnelle = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            # Récupère le dernier ID pour générer le code STR-XXX
            last_struct = Structure.objects.all().order_by('id').last()
            next_id = (last_struct.id + 1) if last_struct else 1
            self.code = f'STR-{next_id:03d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.nom}"

    class Meta:
        verbose_name = "Structure"
        verbose_name_plural = "Structures"