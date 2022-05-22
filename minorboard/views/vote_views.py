from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import QuestionMinor, AnswerMinor


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    minorboard 질문추천등록
    """
    question = get_object_or_404(QuestionMinor, pk=question_id)
    if request.user == question.author_minor:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter_minor.add(request.user)
    return redirect('minorboard:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    minorboard 답글추천등록
    """
    answer = get_object_or_404(AnswerMinor, pk=answer_id)
    if request.user == answer.author_minor:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter_minor.add(request.user)
    return redirect('minorboard:detail', question_id=answer.question_minor.id)