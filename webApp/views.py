from django.shortcuts import render


def landing_view(request):
    return render(request, "webApp/landing_page.html")

def register_refugee_view(request):
    return render(request, "webApp/register_refugee.html")

def register_volunteer_view(request):
    return render(request, "webApp/register_volunteer.html")

def question_view(request):
    return render(request, "webApp/ask_a_question.html")