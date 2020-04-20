from django.db import models
import itertools


# Create your models here.


QUESTION_TYPE = (
    ('multiple choice', 'Multiple Choice'),
    ('yes/no', 'Yes/No')

)
LEVEL_OF_EXPERTISE = (
    ('Entry Level', 'Entry Level'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    ('Expert', 'Expert')


)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=300, unique=True)
    area = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Sub_category(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=300, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sub_Category"
        verbose_name_plural = "Sub_Categories"

    def __str__(self):
        return self.sub_category_name


class Question(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.ForeignKey(
        Sub_category, on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()
    qtype = models.CharField(choices=QUESTION_TYPE, max_length=100)
    option_1 = models.TextField(blank=True)
    option_2 = models.TextField(blank=True)
    option_3 = models.TextField(blank=True)
    option_4 = models.TextField(blank=True)
    answer = models.TextField(blank=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        temp='{0.question} ,{0.answer},{0.option_1},{0.option_2},{0.option_3},{0.option_4}'
        return temp.format(self)


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.EmailField()
    level_of_expertise = models.CharField(
        choices=LEVEL_OF_EXPERTISE, max_length=100)
    area_of_expertise = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    def __str__(self):
        return self.name


def generateUuid(self):
    candidate_id = self.candidate_id
    name = Candidate.objects.get(candidate_id=candidate_id)

    candidate_name = name.name

    uuid_list = []
    uuid_list.append(candidate_name[0].upper())
    for i in range(1, len(candidate_name) - 1):
        if (candidate_name[i] == ' '):
            uuid_list.append(candidate_name[i + 1].upper())
    uuid_list.append(candidate_name[-2].upper())
    uuid_list.append(candidate_name[-1].upper())
    screen_count = Screenings.objects.filter(candidate_id=candidate_id).count()
    screen_count += 1
    uuid_name = "SCRNG"+"".join(uuid_list)
    uuid = uuid_name+str('%02d' % screen_count)
    return uuid
def setQuestion():
    questions=Question.objects.order_by('?')[:5]
    #candidate_id=self.candidate_id
    #screen = Screenings.objects.get(candidate_id=candidate_id)
    question_list=[]
    ans_list=[]
    for question in questions:
        question_list.append(question.question)
        ans_list.append(question.answer)
    return question_list,ans_list


class Screenings(models.Model):
    screening_id = models.AutoField(primary_key=True)
    #screening_id = models.IntegerField(null=True,blank=True)
    screening_uuid = models.CharField(max_length=50, blank=True)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    @classmethod
    def create(cls):
        question_list,ans_list=setQuestion()
        screen = Screenings.objects.last()
        for question,ans in zip(question_list,ans_list):
            #print(question,ans)
            screening_question = Screenings_Questions(screening_id=
	 		screen, question =question,
	  		correct_ans =ans )
            screening_question.save()


    def save(self, *args, **kwargs):
        self.screening_uuid = generateUuid(self.candidate_id)
        print(self.screening_uuid)
        super(Screenings, self).save(*args, **kwargs)
        self.create()
    

        

    class Meta:
        verbose_name = "Screening"
        verbose_name_plural = "Screenings"

    def __str__(self):
        #screening_id = str(self.screening_id)
        return self.screening_uuid



    



class Screenings_Questions(models.Model):
    screening_id = models.ForeignKey(Screenings, on_delete=models.CASCADE)
    #screening_uuid = models.ForeignKey(Screenings, on_delete=models.CASCADE)
    question = models.TextField(blank=True)
    candidate_ans = models.CharField(max_length=50, blank=True)
    correct_ans = models.CharField(max_length=50, blank=True)
    answer_correctness = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = "Screening_Question"
        verbose_name_plural = "Screenings_Questions"
    def __str__(self):
        return self.question



		

	
