from django.db import models


class Machine(models.Model):
    machine_id = models.AutoField(primary_key=True)
    has_aedes = models.BooleanField(default=False)
