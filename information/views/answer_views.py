from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerInformationForm
from ..models import QuestionInformation, AnswerInformation

@login_required(login_url='common:login')#로그아웃 상태에서 @login_required 어노테이션이 적용된 함수가 호출되면 자동으로 로그인 화면으로 이동
def answer_create(request, question_id):
    """
    information 답변등록
    """
    question = get_object_or_404(QuestionInformation, pk=question_id)
    if request.method == "POST":
        form = AnswerInformationForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author_information = request.user  # 추가한 속성 author 적용, reqeust.user는 현재 로그인한 계정의 User모델 객체
            answer.create_dat_information = timezone.now()
            answer.question_information = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('information:detail', question_id=question.id), answer.id))#redirect함수는 페이지 이동을 위해 장고가 제공하는 함수, #QuestionInformation과 AnswerInformation 모델은 서로 ForeignKey 로 연결되어 있기때문에  question.answer_set은 질문의 답변을 의미
    else:
        form = AnswerInformationForm()
    context = {'question': question, 'form': form}
    return render(request, 'information/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    information 답변수정
    """
    answer = get_object_or_404(AnswerInformation, pk=answer_id)
    if request.user != answer.author_information:
        messages.error(request, '수정권한이 없습니다')
        return redirect('information:detail', question_id=answer.question_information.id)

    if request.method == "POST":
        form = AnswerInformationForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author_information = request.user
            answer.modify_date_information = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('information:detail', question_id=answer.question_information.id), answer.id)) #information:detail url에 #answer_7와같은 앵커태그를 추가하기 위해 format, resolve_url사용. resolve_url은 실제 호출되는 url 문자열을 리턴해주는 장고함수.
    else:
        form = AnswerInformationForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'information/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    information 답변삭제
    """
    answer = get_object_or_404(AnswerInformation, pk=answer_id)
    if request.user != answer.author_information:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('information:detail', question_id=answer.question_information.id)
