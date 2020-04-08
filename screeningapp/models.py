from django.db import models

# Create your models here.


QUESTION_TYPE=(
		('multiple choice','Multiple Choice'),
		('yes/no','Yes/No')

	)
LEVEL_OF_EXPERTISE=(
	('Entry Level','Entry Level'),
	('Intermediate','Intermediate'),
	('Advanced','Advanced'),
	('Expert','Expert')


	)
# Create your models here.
class Categorie(models.Model):
	category_id=models.AutoField(primary_key=True)
	category_name=models.CharField(max_length=100,unique=True)
	area=models.CharField(max_length=100)

	def __str__(self):
		return self.category_name

class Sub_categorie(models.Model):
	sub_category_id=models.AutoField(primary_key=True)
	sub_category_name=models.CharField(max_length=100,unique=True)
	category = models.ForeignKey(Categorie, on_delete=models.CASCADE)

	def __str__(self):
		return self.sub_category_name

class Question(models.Model):
	question_id=models.AutoField(primary_key=True)
	question=models.CharField(max_length=500)
	qtype=models.CharField(choices=QUESTION_TYPE, max_length=30)
	option_1=models.CharField(max_length=50)
	option_2=models.CharField(max_length=50)
	option_3=models.CharField(max_length=50)
	option_4=models.CharField(max_length=50)
	answer=models.CharField(max_length=50)
	category_name=models.ForeignKey(Categorie,on_delete=models.CASCADE)
	sub_category_name=models.ForeignKey(Sub_categorie,on_delete=models.CASCADE)

	def __str__(self):
		return self.question



class Candidate(models.Model):
	candidate_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=200)
	email=models.EmailField()
	level_of_expertise=models.CharField(choices=LEVEL_OF_EXPERTISE, max_length=30)
	area_of_expertise=models.CharField(max_length=200)
