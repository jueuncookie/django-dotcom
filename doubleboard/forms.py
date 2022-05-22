from django import forms
from doubleboard.models import QuestionDouble, AnswerDouble, CommentDouble

#QuestionDoubleForm은 QuestionDouble이라는 모델과 연결된 폼이고 속성으로 subject와 content를 사용한다고 정의
class QuestionDoubleForm(forms.ModelForm): #모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 있음.
    class Meta: #Meta 클래스에는 사용할 모델과 모델의 속성을 적어주어야 함.
        model = QuestionDouble
        fields = ['subject_double', 'content_double']

        labels = {
            'subject_double': '제목',
            'content_double': '내용',
        }

class AnswerDoubleForm(forms.ModelForm):
    class Meta:
        model = AnswerDouble
        fields = ['content_double']
        labels = {
            'content_double': '답변내용',
        }

class CommentDoubleForm(forms.ModelForm):
    class Meta:
        model = CommentDouble
        fields = ['content_double']
        labels = {
            'content_double': '댓글내용',
        }