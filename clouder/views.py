import io
import urllib, base64

from django.shortcuts import render
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from .models import TextComment
from .forms import TextCommentForm


def _create_image_as_bytes(cloud: WordCloud):
    plt.figure(figsize=(32, 18))
    plt.imshow(cloud, interpolation="bilinear", aspect="auto")
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read())


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

    cloud = WordCloud(background_color="white").generate(text)

    img_bytes = _create_image_as_bytes(cloud)

    uri = f"data:image/png;base64,{urllib.parse.quote(img_bytes)}"

    cnt = TextComment.objects.count()
    return render(
        request,
        "clouder/index.html",
        {
            "form": TextCommentForm(),
            "obj_count": cnt,
            "word_frequecies": cloud.words_,
            "image": uri,
        },
    )
