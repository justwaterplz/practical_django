from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# reverse
from django.urls import reverse


#25. dictionary 추가
# 각 달의 이름 url(key) - 그에 맞는 값 화면에 출력(value)
monthly_challenges = {
    "january": "1st view",
    "february": "2nd view",
    "march": "3rd view",
    "april": "4th view",
    "may": "5th view",
    "june": "6th view",
    "july": "7th view",
    "august": "8th view",
    "september": "9th view",
    "october": "10th view",
    "november": "11th view",
    "december": None
}

# Create your views here.
# a view is a function or a class that 
# that handles requests and returns responses.

# view with function
# 25. 일일히 쓰기보단 dictionary를 하나 만들어서 재사용함.
# def january(request):
#     return HttpResponse("is this working??")

# def february(request):
#     return HttpResponse("2nd view")

#29 new view function index
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    # 39. shortcut render 사용
    return render(request, "challenges/index.html", {
        "months": months,
    })

    # "<li> ... </li><li> ... </li>"    
# urls.py에 있는 path path("<int:month>", views.monthly_challenge_by_number)를 사용할 때 
# int형 변수 month를 받기 위해 함수 parameter에 month 추가됨.

def monthly_challenge_by_number(request, month):
    # 26. redirect
    # dictionary의 key에 해당하는 값(달 이름) list로 가짐.
    #months list의 index = 0 ~ 11(12개)
    months = list(monthly_challenges.keys())

    #parameter로 받은 month가 invalid함.
    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month-1]

    #reverse 함수로 url 생성.
    redirect_path = reverse("month-challenge", args=[redirect_month]) # challenge/january

    # redirect해서 
    # return HttpResponseRedirect("/challenge/" + redirect_month)
    # reverse 사용시
    return HttpResponseRedirect(redirect_path)

# challenges/urls.py에 path함수 안에 parameter를 <month>라는 dynamic segment로 받았다.
# 이후 path에서 views.py에 있는 monthly_challenge함수를 호출하는데
# path에서 사용한 <month> 변수를 받기 위해 parameter가 request말고도 1개 추가된다.
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month] #페이지 방문시 화면에 표시될 것. 값은 dictionary를 하나 준다.
        # render_to_string으로 template파일 string으로 변환해서 HttpResponse 하는 것도 있는데
        # render가 있으면 굳이 사용하지 않아도 된다.
        # 또한 render는 3가지 args를 갖는데 1번은 request, 2번은 template파일 경로 및 이름, 
        # 
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    # try 실패시 responsenotfound
    except:
        return HttpResponseNotFound("<h1>error</h1>")
