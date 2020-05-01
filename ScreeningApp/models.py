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
class Expertise_Area(models.Model):
    expertise_area_id = models.AutoField(primary_key=True)
    area_of_expertise = models.CharField(max_length=300)#eng
    category_of_expertise = models.CharField(max_length=300)#py

    class Meta:
        verbose_name = "Expertise_Area"
        verbose_name_plural = "Expertise_Areas"

    def __str__(self):
        return self.category_of_expertise

"""class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=300, unique=True)
    area = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name"""
"""class Sub_category(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=300, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sub_Category"
        verbose_name_plural = "Sub_Categories"

    def __str__(self):
        return self.sub_category_name"""

class Expertise(models.Model):
    expertise_id = models.AutoField(primary_key=True)
    expertise = models.CharField(max_length=300)
    category_of_expertise = models.ForeignKey(Expertise_Area, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertises"

    def __str__(self):
        return self.expertise


class Question(models.Model):
    category_of_expertise = models.ForeignKey(Expertise_Area, on_delete=models.CASCADE)
    expertise = models.ForeignKey(
        Expertise, on_delete=models.CASCADE)
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
        #temp='{0.question} ,{0.answer},{0.option_1},{0.option_2},{0.option_3},{0.option_4}'
        #return temp.format(self)
        return self.question


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





class Screenings(models.Model):
    screening_id = models.AutoField(primary_key=True)
    #screening_id = models.IntegerField(null=True,blank=True)
    screening_uuid = models.CharField(max_length=50, blank=True)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE,verbose_name='Candidate Name')
    @classmethod
    def create(cls):

        questions = Question.objects.order_by('?')[:5]
        print(questions)

        screen = Screenings.objects.last()
        #print(screen)
        for question in questions:
            screening_question = Screenings_Questions.objects.create(
                screening_id=screen)
            screening_question.question.add(question)
            screening_question.correct_ans = question.answer
            screening_question.save()

        """for ques in questions:
            screening_question.question.add(ques)"""
        #screening_question.question.set(question)

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
        self.create()

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
