from django.test import TestCase
from django.utils import timezone
from polls.models import Question
import datetime
# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.delta(days=30)
        future_question = Question(time_pub=time)
        self.assertIs(future_question.was_published_recently(), False)