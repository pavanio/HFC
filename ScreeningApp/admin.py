# Register your models here.
from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
# Register your models here.
class ExpertiseInline(admin.TabularInline):
	model=Expertise
	extra=0
	


class ScreeningInline(admin.TabularInline):
	model=Screenings
	extra=0
	readonly_fields=('screening_uuid','status','screening_result')
	show_change_link=True
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
class Screenings_Questions_Inline(admin.TabularInline):
	model=Screenings_Questions
	verbose_name ='Question'
	verbose_name_plural='Questions'
	extra=0
	readonly_fields=('question','correct_ans','candidate_ans','answer_correctness')
	def get_questions(self, obj):
		return "\n".join([p.question for p in obj.Screenings_Questions.all()])
	get_questions.short_description='question'
	
	def get_correct_ans(self,obj):
		pass

		
	 
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False

class Expertise_AreaAdmin(admin.ModelAdmin):
	list_display = ('area_of_expertise',)
	inlines =[ExpertiseInline]
	class meta:
		model=Expertise_Area
admin.site.register(Expertise_Area,Expertise_AreaAdmin)

class ExpertiseAdmin(admin.ModelAdmin):
	list_display = ('expertise','category_of_expertise')
	class meta:
		model=Expertise
admin.site.register(Expertise,ExpertiseAdmin)



class QuestionAdmin(admin.ModelAdmin):
	list_display=('category_of_expertise','expertise','level','topic','qtype','question','option_1','option_2','option_3','option_4','answer')
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':60})},
        }
	list_filter = ('category_of_expertise', 'expertise', 'level', )
	class meta:
		model=Question
admin.site.register(Question,QuestionAdmin)




class ScreeningAdmin(admin.ModelAdmin):
	list_display=('screening_uuid','candidate_id','first_reminder_date','second_reminder_date','third_reminder_date','status','screening_result')
	readonly_fields=('screening_uuid','status','screening_result')
	inlines=[Screenings_Questions_Inline]
	class meta:
		model=Screenings
admin.site.register(Screenings,ScreeningAdmin)










class CandidateAdmin(admin.ModelAdmin):
	list_display=('name','email','contact_number','gender','dob','highest_education','level_of_expertise','profession','areaofexpertise')
	inlines =[ScreeningInline]
	class meta:
		model=Candidate
admin.site.register(Candidate,CandidateAdmin)
