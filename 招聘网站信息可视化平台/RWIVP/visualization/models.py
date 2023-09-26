from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=45)
    salary = models.CharField(null=True,max_length=45)
    min_salary = models.CharField(null=True,max_length=45)
    max_salary = models.CharField(null=True,max_length=45)
    city = models.CharField(max_length=45)
    experience = models.CharField(max_length=45)
    education = models.CharField(max_length=45)
    tags = models.CharField(max_length=255)
    company_name = models.CharField(max_length=45)
    company_nature = models.CharField(max_length=45)
    company_size = models.CharField(max_length=45)
    industry = models.CharField(max_length=45)
    remarks_str = models.TextField()
    job_link = models.URLField()
