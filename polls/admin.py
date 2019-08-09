from django.contrib import admin
from .models import Question,Choice,Student
# Register your models here.



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 列表页属性
    # 关联StudentsInfo，创建班级时，填写两个学生的信息
    # inlines = [StudentsInfo]
    list_display = ['id', 'question_text', 'pub_date']
    list_filter = ['id']
    search_fields = ['question_text']
    list_per_page = 5
    inlines = [ChoiceInline]
    # 修改页,fields,fieldsets不能同时使用
    # fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
    # fieldsets = [
    #     ("num", {"fields": ['ggirlnum', 'gboynum']}),
    #     ("base", {"fields": ['gname', 'gdate', 'isDelete']})
    # ]

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Student)