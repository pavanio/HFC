from django.db import models
import itertools
import random

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
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other','Other'),

)
EDUCATION = (
    ('Intermediate', 'Intermediate'),
    ('Bachelors', 'Bachelors'),
    ('Masters','Masters'),

)
STATUS=(
    ('Open','Open'),
    ('Closed','Closed'),
    ('Passed','Passed'),
    ('Failed','Failed'),
)
OPTION=(
    ('option_1','option_1'),
    ('option_2','option_2'),
    ('option_3','option_3'),
    ('option_4','option_4'),
)
PUBLISH=(
    ('True','True'),
    ('False','False'),
)
class Expertise_Area(models.Model):
    expertise_area_id = models.AutoField(primary_key=True)
    area_of_expertise = models.CharField(max_length=300)#eng
    #category_of_expertise = models.CharField(max_length=300)#py

    class Meta:
        verbose_name = "Expertise_Area"
        verbose_name_plural = "Expertise_Areas"

    def __str__(self):
        return self.area_of_expertise

class Expertise(models.Model):
    expertise_id = models.AutoField(primary_key=True)
    expertise = models.CharField(max_length=300)
    category_of_expertise = models.ForeignKey(Expertise_Area, on_delete=models.CASCADE)
    is_published = models.CharField(choices=PUBLISH, max_length=10,blank=True,null=True)

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertises"

    def __str__(self):
        return self.expertise

class Question(models.Model):
    category_of_expertise = models.ForeignKey(Expertise_Area, on_delete=models.CASCADE)
    expertise = models.ForeignKey(
        Expertise, on_delete=models.CASCADE)
    level=models.CharField(
        choices=LEVEL_OF_EXPERTISE, max_length=100)
    topic=models.CharField(max_length=200)
    question_id = models.AutoField(primary_key=True)
    qtype = models.CharField(choices=QUESTION_TYPE, max_length=100)
    question = models.TextField()
    option_1 = models.TextField(blank=True,null=True)
    option_2 = models.TextField(blank=True,null=True)
    option_3 = models.TextField(blank=True,null=True)
    option_4 = models.TextField(blank=True,null=True)
    answer = models.CharField(choices=OPTION, max_length=100,blank=True,null=True)
    question_img = models.URLField(blank=True,null=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        #temp='{0.question} ,{0.answer},{0.option_1},{0.option_2},{0.option_3},{0.option_4}'
        #return temp.format(self)
        return self.question


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER,max_length=50,blank=True,null=True) 
    dob = models.DateField(blank=True,null=True) 
    highest_education = models.CharField(choices=EDUCATION,max_length=50) 
    level_of_expertise = models.CharField(
        choices=LEVEL_OF_EXPERTISE, max_length=100)
    profession = models.ForeignKey(Expertise_Area, on_delete=models.CASCADE)
    area_of_expertise = models.ManyToManyField('Expertise')
    
    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    def __str__(self):
        return self.name
    def areaofexpertise(self):
        return ",".join([area.expertise for area in self.area_of_expertise.all()])

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

class Screenings(models.Model):
    screening_id = models.AutoField(primary_key=True)
    #screening_id = models.IntegerField(null=True,blank=True)
    screening_uuid = models.CharField(max_length=50, blank=True)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE,verbose_name='Candidate Name')
    status=models.CharField(choices=STATUS, max_length=50,default='Open')
    screening_result=models.CharField(max_length=50, blank=True)
    @classmethod
    def create(cls,candidate_id):
        print('candidate id',candidate_id)
        category_of_expertise=candidate_id.profession
        print(category_of_expertise)
        level=candidate_id.level_of_expertise
        print(level)
        Expertises=candidate_id.area_of_expertise.all()
        print(Expertises)
        #questions=Question.objects.filter(category_of_expertise=category_of_expertise).filter(level=level).filter(expertise__in=Expertises).order_by('?')[:5]
        #questions=Question.objects.filter(expertise__in=Expertises)
        questions_list=Question.objects.filter(category_of_expertise=category_of_expertise).filter(level=
        level).filter(expertise__in=Expertises).values_list('question_id', flat=True)
        random_question_id_list = random.sample(list(questions_list), min(len(questions_list), 10))
        questions = Question.objects.filter(question_id__in=random_question_id_list)   
        print('candidate screening questions', questions)
        screen = Screenings.objects.last()
        #print(screen)
        for question in questions:
            screening_question = Screenings_Questions.objects.create(
                screening_id=screen)
            screening_question.question.add(question)
            screening_question.correct_ans = question.answer
            screening_question.save()

    def get_questions(self, screening_id):
        questions = Screenings_Questions.objects.filter(
            screening_id=self.screening_id)
        for question in questions:
            for item in question:
                item.option_1
        return self.questions

    def save(self, *args, **kwargs):
        self.screening_uuid = generateUuid(self.candidate_id)
        print(self.screening_uuid)
        super(Screenings, self).save(*args, **kwargs)
        self.create(self.candidate_id)

    class Meta:
        verbose_name = "Screening"
        verbose_name_plural = "Screenings"

    def __str__(self):
        #screening_id = str(self.screening_id)
        return self.screening_uuid


class Screenings_Questions(models.Model):
    screening_id = models.ForeignKey(
        Screenings, on_delete=models.CASCADE, verbose_name='candidate_name')
    #screening_uuid = models.ForeignKey(Screenings, on_delete=models.CASCADE)
    question = models.ManyToManyField('Question', related_name='questions')
    candidate_ans = models.CharField(max_length=50, blank=True)
    correct_ans = models.CharField(max_length=50, blank=True)
    answer_correctness = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = "Screening_Question"
        verbose_name_plural = "Screenings_Questions"
    """def __str__(self):
        return self.screening_uuid """
