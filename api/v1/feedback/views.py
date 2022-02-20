from rest_framework.generics import CreateAPIView

from api.v1.feedback.serializers import FeedbackSerailizer


class CreateFeedbackView(CreateAPIView):
    serializer_class = FeedbackSerailizer