from django.db import models
from django.contrib.gis.db import models as gismodels

# Create your models here.
class app_user(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.lname}, {self.fname}"

class project(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(app_user)
    manager = models.ForeignKey(app_user, on_delete=models.SET_NULL, blank=True,null=True, related_name="manager")

    def __str__(self):
        return self.name

class species(models.Model):
    latin_name = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    invasive = models.BooleanField()
    CDC_rank = models.IntegerField()

    def __str__(self):
        return f"{self.latin_name}, {self.name}"
    class Meta:
        verbose_name_plural='species'
        ordering=['latin_name']

class map_data(gismodels.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE, blank=True, null=True)
    time = models.DateTimeField()
    location = gismodels.PointField()
    species = models.ForeignKey(species,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='map data'

class survey_method_types(models.Model):
    type_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural="survey method types"

class survey_methods(models.Model):
    type_name = models.ForeignKey(survey_method_types, on_delete=models.CASCADE)
    method_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.type_name}, {self.method_name}"
    class Meta:
        verbose_name_plural="survey methods"
        unique_together = ('type_name','method_name')


class survey_questions(models.Model):
    question = models.CharField(max_length=500)
    species = models.ForeignKey(species, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural='survey questions'

class survey_data(models.Model):
    user = models.ForeignKey(app_user, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    question = models.ForeignKey(survey_questions, on_delete=models.CASCADE)
    data = models.CharField(max_length=500)
    public = models.BooleanField()

    class Meta:
        verbose_name_plural='survey data'

class survey_template(models.Model):
    questions = models.ManyToManyField(survey_questions)
    project = models.ForeignKey(project, on_delete=models.SET_NULL, blank=True, null=True)
    public = models.BooleanField()

    class Meta:
        verbose_name_plural='survey templates'

class observation_type(models.Model):
    observation_type = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural='observation types'

class incedent_observations(gismodels.Model):
    user = models.ForeignKey(app_user,on_delete=models.CASCADE)
    observation_type = models.ForeignKey(observation_type, on_delete=models.CASCADE)
    location = gismodels.PointField()
    species = models.ForeignKey(species, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    public = models.BooleanField()
    class Meta:
        verbose_name_plural='incedent observations'
    