from django.urls import path
from . import views

#january 라는 url에 접속 성공시 view file의 index function 실행
#url config라고함.
urlpatterns= [
    # challenges/january
    # path("january", views.january),
    # path("february", views.february),

    #29 added new path
    #44. header를 클릭하면 index 화면으로 나오게 하기 위해 
    #url tag를 사용해야 한다. 따라서 밑에 있는 path 함수에 name을 추가했다.
    path("", views.index, name="index"), #/challenges/
    #dynamic url pathing using placeholder

    #int 동일한 이름의 변수인 month를 사용하는데 str을 사용한 path함수가 먼저 오면 "1"같은 숫자를 str로 받아버리기 때문에
    #결과에 영향을 줄 수 있다. 따라서 url에 입력된 값이 숫자인지 판별하고 아니면 2번째 path로 넘어가게끔 해야된다.
    path("<int:month>", views.monthly_challenge_by_number),

    #path함수 실행 시 challenge/month name 이런 식인데
    #성공시 views.py에 있는 monthly_challenge 함수 실행.
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    
    
]