import io
import urllib, base64

import matplotlib.pyplot as plt
from wordcloud import WordCloud


class WordCloudGenerator:
    def __init__(self, *args, **kwargs):
        self.cloud_generator = WordCloud(**kwargs)

    def get_word_counters(self, text: str) -> dict:
        return self.cloud_generator.process_text(text)

    def get_image_bytes(self, text: str) -> bytes:
        cloud = self.cloud_generator.generate(text)
        plt.figure(figsize=(32, 18))
        plt.imshow(cloud, interpolation="bilinear", aspect="auto")
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        return base64.b64encode(buf.read())
