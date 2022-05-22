from django import forms
from minorboard.models import QuestionMinor, AnswerMinor, CommentMinor

#QuestionMinorForm은 QuestionMinor이라는 모델과 연결된 폼이고 속성으로 subject와 content를 사용한다고 정의
class QuestionMinorForm(forms.ModelForm): #모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 있음.
    class Meta: #Meta 클래스에는 사용할 모델과 모델의 속성을 적어주어야 함.
        model = QuestionMinor
        fields = ['subject_minor', 'content_minor']

        labels = {
            'subject_minor': '제목',
            'content_minor': '내용',
        }

class AnswerMinorForm(forms.ModelForm):
    class Meta:
        model = AnswerMinor
        fields = ['content_minor']
        labels = {
            'content_minor': '답변내용',
        }

class CommentMinorForm(forms.ModelForm):
    class Meta:
        model = CommentMinor
        fields = ['content_minor']
        labels = {
            'content_minor': '댓글내용',
        }