from collections import defaultdict

from django.shortcuts import render

from .models import TextComment
from .forms import TextCommentForm
from .services import WordCloudGenerator


def index(request):
    obj = TextCommentForm(request.POST)
    if obj.is_valid():
        obj.save()

    text = " ".join([v["content"] for v in TextComment.objects.all().values("content")])

    if not text:
        return render(
            request,
            "clouder/index.html",
            {
                "form": TextCommentForm(),
                "obj_count": 0,
                "word_frequecies": {},
                "image": "",
            },
        )

    generator = WordCloudGenerator(background_color=None, mode="RGBA")
    word_counters = generator.get_word_counters(text)
    img_bytes = generator.get_image_bytes(text)

    freq = defaultdict(list)

    for word, frequency in word_counters.items():
        freq[frequency].append(word)

    return render(
        request,
        "clouder/index.html",
        {
            "form": TextCommentForm(),
            "obj_count": TextComment.objects.count(),
            "word_frequecies": dict(freq),
            "image": f"data:image/png;base64,{urllib.parse.quote(img_bytes)}",
        },
    )
