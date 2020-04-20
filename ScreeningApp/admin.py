

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
class Sub_CategoryInline(admin.TabularInline):
	model=Sub_category

class ScreeningInline(admin.TabularInline):
	model=Screenings
	extra=0
	readonly_fields=('screening_uuid',)
class Screenings_Questions_Inline(admin.TabularInline):
	model=Screenings_Questions
	extra=0
	readonly_fields=('question','candidate_ans','correct_ans','answer_correctness')
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_id','area','category_name')
	inlines =[Sub_CategoryInline]
	class meta:
		model=Category
admin.site.register(Category,CategoryAdmin)






class QuestionAdmin(admin.ModelAdmin):
	list_display=('category_name','sub_category_name','qtype','question','option_1','option_2','option_3','option_4','answer')
	class meta:
		model=Question
admin.site.register(Question,QuestionAdmin)



"""class ScreeningQuestionAdmin(admin.ModelAdmin):
	list_display=('id','screening_id',)
	class meta:
		model=Screenings_Questions
admin.site.register(Screenings_Questions,ScreeningQuestionAdmin)"""



class ScreeningAdmin(admin.ModelAdmin):
	list_display=('screening_uuid','candidate_id')
	readonly_fields=('screening_uuid',)
	inlines=[Screenings_Questions_Inline]
	class meta:
		model=Screenings
admin.site.register(Screenings,ScreeningAdmin)










class CandidateAdmin(admin.ModelAdmin):
	list_display=('name','email','level_of_expertise','area_of_expertise')
	inlines =[ScreeningInline]
	class meta:
		model=Candidate
admin.site.register(Candidate,CandidateAdmin)