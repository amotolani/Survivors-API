import uuid
from django.db import models


# Create your model for Passenger data.
class Passenger(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    passengerClass = models.PositiveSmallIntegerField(blank=False, choices=[
                                                          (1, 'First Class'),
                                                          (2, 'Second Class'),
                                                          (3, 'Third Class')
                                                        ])
    sex = models.CharField(max_length=20, choices=[
                               ('male', 'Male'),
                               ('female', 'Female'),
                               ('non-binary', 'Non-Binary'),
                               ('transgender', 'Transgender'),
                           ])
    age = models.PositiveSmallIntegerField(blank=False)
    siblingsOrSpousesAboard = models.PositiveSmallIntegerField(blank=False)
    parentsOrChildrenAboard = models.PositiveSmallIntegerField(blank=False)
    survived = models.BooleanField(blank=False)
    fare = models.FloatField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'passengers'
