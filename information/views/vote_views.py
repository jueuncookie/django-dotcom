from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import QuestionInformation, AnswerInformation


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    information 질문추천등록
    """
    question = get_object_or_404(QuestionInformation, pk=question_id)
    if request.user == question.author_information:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter_information.add(request.user)
    return redirect('information:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    information 답글추천등록
    """
    answer = get_object_or_404(AnswerInformation, pk=answer_id)
    if request.user == answer.author_information:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter_information.add(request.user)
    return redirect('information:detail', question_id=answer.question_information.id)