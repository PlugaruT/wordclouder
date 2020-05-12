from django.shortcuts import render

from .models import TextComment
from .forms import TextCommentForm


def index(request):
    obj = TextCommentForm(request.POST)
    obj.save()

    cnt = TextComment.objects.count()
    return render(
        request, "clouder/index.html", {"form": TextCommentForm(), "obj_count": cnt}
    )
