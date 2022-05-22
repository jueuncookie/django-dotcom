from django import forms
from information.models import QuestionInformation, AnswerInformation, CommentInformation

#QuestionInformationForm은 QuestionInformation이라는 모델과 연결된 폼이고 속성으로 subject와 content를 사용한다고 정의
class QuestionInformationForm(forms.ModelForm): #모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 있음.
    class Meta: #Meta 클래스에는 사용할 모델과 모델의 속성을 적어주어야 함.
        model = QuestionInformation
        fields = ['subject_information', 'content_information']

        labels = {
            'subject_information': '제목',
            'content_information': '내용',
        }

class AnswerInformationForm(forms.ModelForm):
    class Meta:
        model = AnswerInformation
        fields = ['content_information']
        labels = {
            'content_information': '답변내용',
        }

class CommentInformationForm(forms.ModelForm):
    class Meta:
        model = CommentInformation
        fields = ['content_information']
        labels = {
            'content_information': '댓글내용',
        }