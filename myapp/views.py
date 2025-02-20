from django.shortcuts import render, HttpResponse

# Create your views here.

# class = [name, article, due_date, location, picture_url]
# category = [name, article, picture_url, classlist = [classname, classname, ... ]]

class_1 = ["해녀의 바당요리", "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께해요", "2025-07-12", "제주시 이도2동", ""]
class_2 = ["해녀의 바당요리", "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께해요", "2025-07-12", "제주시 이도2동", ""]
class_3 = ["해녀의 바당요리", "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께해요", "2025-07-12", "제주시 이도2동", ""]
class_4 = ["해녀의 바당요리", "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께해요", "2025-07-12", "제주시 이도2동", ""]
class_5 = ["해녀의 바당요리", "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께해요", "2025-07-12", "제주시 이도2동", ""]
class_6 = ["해녀의 바당요리", "해녀의 불턱에서 성게국과 옥돔구이를 만드는 소중한 시간을 함께해요", "2025-07-12", "제주시 이도2동", ""]

category_1 = ["바다의 기억", "파도가 전하는 제주 바다의 맛", "", [class_1, class_2, class_3, class_4, class_5, class_6]]
category_2 = ["바다의 기억", "파도가 전하는 제주 바다의 맛", "", [class_1, class_2, class_3, class_4, class_5, class_6]]
category_3 = ["바다의 기억", "파도가 전하는 제주 바다의 맛", "", [class_1, class_2, class_3, class_4, class_5, class_6]]
category_4 = ["바다의 기억", "파도가 전하는 제주 바다의 맛", "", [class_1, class_2, class_3, class_4, class_5, class_6]]
category_5 = ["바다의 기억", "파도가 전하는 제주 바다의 맛", "", [class_1, class_2, class_3, class_4, class_5, class_6]]
category_6 = ["바다의 기억", "파도가 전하는 제주 바다의 맛", "", [class_1, class_2, class_3, class_4, class_5, class_6]]

category = [category_1, category_2, category_3, category_4, category_5, category_6]

def splash_function(request):
    
    return HttpResponse('splash')

def intro_function(request):
    return HttpResponse('intro')

def classlist_function(request):
    return HttpResponse('classlist')

def class_function(request,id):
    return HttpResponse(f'class, {id}')

def classmodal_function(request,id):
    return HttpResponse(f'classmodal, {id}')