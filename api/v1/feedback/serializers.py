
from rest_framework import serializers

from index.models import Feedback


class FeedbackSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
