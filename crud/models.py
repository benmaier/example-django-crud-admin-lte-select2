from django.db import models

class Geoname(models.Model):
    name = models.CharField(max_length=255)
    population = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(Geoname,models.SET_NULL,blank=True,null=True)
    responsible_for_places = models.ManyToManyField(Geoname,blank=True,related_name='responsible_institutions')
    
    def __str__(self):
        return self.name

class CooperationalRelationship(models.Model):
    institution = models.ForeignKey(Institution,models.CASCADE,related_name='cooperational_relationships')
    city = models.ForeignKey(Geoname,models.CASCADE,related_name='institutional_relationships')
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{} <-> {}".format(self.institution, self.city)
