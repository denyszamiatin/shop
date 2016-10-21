from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Good, Comment
from .forms import Feedback


# Create your views here.
def index(request):
    goods = Good.objects.all()
    return render(request, 'index.html', {'goods': goods})


def detail(request, slug):
    good = get_object_or_404(Good, slug=slug)
    if request.method == 'POST':
        feedback = Feedback(request.POST)
        if feedback.is_valid():
            Comment.objects.create(
                email=feedback.cleaned_data['email'],
                name=feedback.cleaned_data['name'],
                text=feedback.cleaned_data['text'],
                good=good
            )
    feedback = Feedback()

    return render(request, 'detail.html',
                  {
                      'good': good,
                      'feedback': feedback,
                      'feedbacks': Comment.objects.filter(good=good),
                  }
                  )


def templ(request):
    return render(request, 'templ.html', {'a': {'a': 1, 'b': [1,2,3]}})