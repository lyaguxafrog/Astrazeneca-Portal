from django.db import models

class ParentModel(models.Model):
    name = models.CharField(max_length=100)

class ChildModel1(models.Model):
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    # Добавьте поля для ChildModel1
    test = models.CharField(null=True, blank=True)

class ChildModel2(models.Model):
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    test = models.CharField(null=True, blank=True)
    # Добавьте поля для ChildModel2
