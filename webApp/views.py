from django.shortcuts import render


def landing_view(request):
    return render(request, "webApp/landing_page.html")

def register_refugee_view(request):
    return render(request, "webApp/register_refugee.html")

def register_volunteer_view(request):
    return render(request, "webApp/register_volunteer.html")

def question_view(request):
    return render(request, "webApp/ask_question.html")

def main_refugee_view(request):
    return render(request, "webApp/main_refugee.html")

def login_view(request):
    return render(request, "webApp/main_refugee.html")

def see_questions(request):
    return render(request, "webApp/see_questions.html")