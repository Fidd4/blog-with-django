from haystack import indexes

from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Поиск осуществляется по полям title_post и text модели Post.
    """
    text = indexes.CharField(document=True, use_template=True)
    title_post = indexes.CharField(model_attr='title_post')
    body_text = indexes.CharField(model_attr='text')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
