from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

#25. dictionary 추가
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
    "december": "12th view"
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

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)



# challenges/urls.py에 path함수 안에 parameter를 <month>라는 dynamic segment로 받았다.
# 이후 path에서 views.py에 있는 monthly_challenge함수를 호출하는데
# path에서 사용한 <month> 변수를 받기 위해 parameter가 request말고도 1개 추가된다.
def monthly_challenge(request, month):
    try:
        challenge_month = monthly_challenges[month] #페이지 방문시 화면에 표시될 것. 값은 dictionary를 하나 준다.
        return HttpResponse(challenge_month)
    # try 실패시 responsenotfound
    except:
        return HttpResponseNotFound("error")
    # if month == 'january':
    #     challenge_month = "1st view"
    # elif month == 'march':
    #     challenge_month = "3rd view"
    # elif month == 'february':
    #     challenge_month = "2nd view"
    # else:
    #     # 1 ~ 12월이 아닌 다른 것이 url에 입력되면 에러표시. 여기서는 1 2 3월만 해놔서 나머지가 안됨.
    #     return HttpResponseNotFound("this month is not supported")