from django import forms
from free.models import QuestionFree, AnswerFree, CommentFree

#QuestionFreeForm은 QuestionFree이라는 모델과 연결된 폼이고 속성으로 subject와 content를 사용한다고 정의
class QuestionFreeForm(forms.ModelForm): #모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 있음.
    class Meta: #Meta 클래스에는 사용할 모델과 모델의 속성을 적어주어야 함.
        model = QuestionFree
        fields = ['subject_free', 'content_free']

        labels = {
            'subject_free': '제목',
            'content_free': '내용',
        }

class AnswerFreeForm(forms.ModelForm):
    class Meta:
        model = AnswerFree
        fields = ['content_free']
        labels = {
            'content_free': '답변내용',
        }

class CommentFreeForm(forms.ModelForm):
    class Meta:
        model = CommentFree
        fields = ['content_free']
        labels = {
            'content_free': '댓글내용',
        }