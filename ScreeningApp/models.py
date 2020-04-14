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
class Category(models.Model):
	category_id=models.AutoField(primary_key=True)
	category_name=models.CharField(max_length=300,unique=True)
	area=models.CharField(max_length=300)
	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category_name

class Sub_category(models.Model):
	sub_category_id=models.AutoField(primary_key=True)
	sub_category_name=models.CharField(max_length=300,unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	class Meta:
		verbose_name = "Sub_Category"
		verbose_name_plural = "Sub_Categories"

	def __str__(self):
		return self.sub_category_name

class Question(models.Model):
	question_id=models.AutoField(primary_key=True)
	question=models.TextField() 
	qtype=models.CharField(choices=QUESTION_TYPE, max_length=100)
	option_1=models.TextField(blank=True) 
	option_2=models.TextField(blank=True) 
	option_3=models.TextField(blank=True) 
	option_4=models.TextField(blank=True) 
	answer=models.TextField(blank=True) 
	category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
	sub_category_name=models.ForeignKey(Sub_category,on_delete=models.CASCADE)
	class Meta:
		verbose_name = "Question"
		verbose_name_plural = "Questions"

	def __str__(self):
		return self.question



class Candidate(models.Model):
	candidate_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=500)
	email=models.EmailField()
	level_of_expertise=models.CharField(choices=LEVEL_OF_EXPERTISE, max_length=100)
	area_of_expertise=models.CharField(max_length=500)
	class Meta:
		verbose_name = "Candidate"
		verbose_name_plural = "Candidates"

	def __str__(self):
		return self.name


class Screening_Question(models.Model):
	screening_id=models.AutoField(primary_key=True)
	question_id=models.ManyToManyField(Question,blank=True)
	candidate_ans=models.CharField(max_length=50,blank=True)
	correct_ans=models.CharField(max_length=50,blank=True)
	answer_correctness=models.CharField(max_length=10,blank=True)



	





class Candidate_Screening(models.Model):
	id=models.AutoField(primary_key=True)
	screening_id=models.ForeignKey(Screening_Question,on_delete=models.CASCADE)
	candidate_id=models.ForeignKey(Candidate,on_delete=models.CASCADE)
	screening_uuid=models.CharField(max_length=200)

	def __str__(self):
		return self.screening_uuid
		
