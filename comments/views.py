from rest_framework import mixins, viewsets

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    博客评论视图集
    create:
    创建博客评论
    """

    serializer_class = CommentSerializer

    def get_queryset(self):  # pragma: no cover
        return Comment.objects.all()