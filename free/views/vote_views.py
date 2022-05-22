from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import QuestionFree, AnswerFree


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    free 질문추천등록
    """
    question = get_object_or_404(QuestionFree, pk=question_id)
    if request.user == question.author_free:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter_free.add(request.user)
    return redirect('free:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    free 답글추천등록
    """
    answer = get_object_or_404(AnswerFree, pk=answer_id)
    if request.user == answer.author_free:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter_free.add(request.user)
    return redirect('free:detail', question_id=answer.question_free.id)