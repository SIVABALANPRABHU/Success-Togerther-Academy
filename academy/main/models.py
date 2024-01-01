from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    preferred_exam = models.CharField(max_length=50, choices=[
        ('tnpsc_group1', 'TNPSC Group 1'),
        ('tnpsc_group4', 'TNPSC Group 4'),
        ('tnusrp_si', 'TNUSRP SI Open Quota'),
        ('bc_exam', 'BC Exam'),
    ])
