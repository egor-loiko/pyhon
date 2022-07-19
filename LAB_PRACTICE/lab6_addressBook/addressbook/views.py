from django.shortcuts import get_object_or_404, render, redirect
from .models import Person, Address


# главная страница со списком персонов
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
# создание HTML-страницы по шаблону index.html
# с заданными параметрами latest_persons и message
    return render(
        request,
        "index.html",
    {
        "latest_persons":
            Person.objects.order_by('person_text')[:5],
            "message": message
    }
)


# страница с адресом для персона
def address(request, person_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "address.html",
    {
        "person": get_object_or_404(Person, pk=person_id),
        "error_message": error_message
    }
)