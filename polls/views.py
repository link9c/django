import datetime

# from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic, View

from .models import Question, Choice, Student


# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_data')[:5]
#     # output = ','.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

def IndexView(request):
    ip = request.META['REMOTE_ADDR']
    # print(ip)
    return render(request, 'polls/home.html', {"ip": ip})


# class IndexView(generic.ListView):
#     model = Question
#     template_name = 'polls/index.html'


class QuestionView(generic.ListView):
    template_name = 'polls/question.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        :return:the last five published questions.
        """
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         # question = get_object_or_404(Question, pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # print(reverse('polls:results', args=(question.id,)))
        # return HttpResponse("ok")
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def queryStudent(request):
    stu = ""
    if request.method == "POST" and request.POST:
        stu = Student.objects.all()
    return render(request, 'polls/queryStudent.html', {"student_name": stu})


@csrf_exempt
def addStudent(request):
    # if request.method == "POST" and request.POST:
    #     # 表单提交
    #     db = Student()
    #     db.name = request.POST['stu_name']
    #     db.add_date = datetime.datetime.utcnow()
    #     db.save()
    #     print(request.POST)
    #     return  HttpResponseRedirect(reverse('polls:queryStudent'))
    if request.is_ajax():
        # print(request.body)  # 原始的请求体数据
        db = Student()
        db.name = request.POST.get('name')

        db.add_date = datetime.datetime.now()
        db.save()
    # print(request.FILES)  # 上传的文件数据
    return HttpResponse("ok")


def randomStu(request):
    stu = Student.objects.all()
    return render(request, 'polls/randomStu.html', {"student_name": stu})

# def get_valid_img(request):
#     # 获取随机颜色的函数
#     def get_random_color():
#         return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#
#     # 生成一个图片对象
#     img_obj = Image.new(
#         'RGB',
#         (220, 35),
#         get_random_color()
#     )
#     # 在生成的图片上写字符
#     # 生成一个图片画笔对象
#     draw_obj = ImageDraw.Draw(img_obj)
#     # 加载字体文件， 得到一个字体对象
#     font_obj = ImageFont.truetype("static/font/kumo.ttf", 28)
#     # 开始生成随机字符串并且写到图片上
#     tmp_list = []
#     for i in range(5):
#         u = chr(random.randint(65, 90))  # 生成大写字母
#         l = chr(random.randint(97, 122))  # 生成小写字母
#         n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型
#
#         tmp = random.choice([u, l, n])
#         tmp_list.append(tmp)
#         draw_obj.text((20 + 40 * i, 0), tmp, fill=get_random_color(), font=font_obj)
#
#     # 保存到session
#     request.session["valid_code"] = "".join(tmp_list)
#     # 加干扰线
#     width = 220  # 图片宽度（防止越界）
#     height = 35
#     for i in range(5):
#         x1 = random.randint(0, width)
#         x2 = random.randint(0, width)
#         y1 = random.randint(0, height)
#         y2 = random.randint(0, height)
#         draw_obj.line((x1, y1, x2, y2), fill=get_random_color())
#
#     # 加干扰点
#     for i in range(40):
#         draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
#         x = random.randint(0, width)
#         y = random.randint(0, height)
#         draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())
#
#     # 不需要在硬盘上保存文件，直接在内存中加载就可以
#     io_obj = BytesIO()
#     # 将生成的图片数据保存在io对象中
#     img_obj.save(io_obj, "png")
#     # 从io对象里面取上一步保存的数据
#     data = io_obj.getvalue()
#     return HttpResponse(data)
