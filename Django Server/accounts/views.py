from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import User
from recommend.serializers import UserProfileSerializer
from fin_product.serializers import GETDepositOptionsSerializer, GetSavingOptionsSerializer
from community.serializers import PostSerializer, NestedCommentSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserRelatedData(request):
    user = User.objects.get(id=request.user.id)

    profile = user.userprofile_set.all()
    profile_serializer = UserProfileSerializer(profile, many=True).data

    into_deposit_options = user.into_deposit_options.all()
    into_deposit_options_serializer = GETDepositOptionsSerializer(into_deposit_options, many=True).data

    into_saving_options = user.into_saving_options.all()
    into_saving_options_serializer = GetSavingOptionsSerializer(into_saving_options, many=True).data

    posts = user.post_writer.all()
    posts_serializer = PostSerializer(posts, many=True).data

    liked_posts = user.like_post.all()
    like_post_serializer = PostSerializer(liked_posts, many=True).data

    comments = user.comment_writer.all()
    comments_serializer = NestedCommentSerializer(comments, many=True).data

    liked_comment = user.like_comment.all()
    liked_comment_serializer = NestedCommentSerializer(liked_comment, many=True).data

    return Response({
        'profile': profile_serializer,
        'deposits': into_deposit_options_serializer,
        'savings': into_saving_options_serializer,
        'posts': posts_serializer,
        'likePost': like_post_serializer,
        'comment': comments_serializer,
        'liked_comment': liked_comment_serializer

    })