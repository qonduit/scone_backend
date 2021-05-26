from django.db import models


class Schemes (models.Model):
    name = models.TextField()
    address = models.TextField()


class Residents (models.Model):
    forename = models.TextField()
    middle_names = models.TextField(blank=True)
    surname = models.TextField()
    dob = models.DateField()
    previous_address = models.TextField(blank=True)
    scheme = models.ForeignKey('Schemes', on_delete=models.CASCADE)


class OPP (models.Model):
    resident_id = models.ForeignKey(
        'Residents', on_delete=models.CASCADE, primary_key=True)
    t1 = models.TextField()
    t2 = models.TextField()


class RAG (models.Model):
    colour = models.TextField()


class Risks (models.Model):
    resident_id = models.ForeignKey(
        'Residents', on_delete=models.CASCADE)
    risk = models.TextField()
    mitigation = models.TextField()
    rag = models.ForeignKey('RAG', on_delete=models.CASCADE)

class Sup (models.Model):
    resident_id = models.ForeignKey(
        'Residents', on_delete=models.CASCADE)
    entries = models.TextField()

