from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentInformationForm
from ..models import QuestionInformation, AnswerInformation, CommentInformation

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    information 질문댓글등록
    """
    question = get_object_or_404(QuestionInformation, pk=question_id)
    if request.method == "POST":
        form = CommentInformationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_information = request.user
            comment.create_date_information = timezone.now()
            comment.question_information = question #질문에 대한 댓글이므로 comment에 question저장.
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('information:detail', question_id=comment.question_information.id), comment.id))
    else:
        form = CommentInformationForm()
    context = {'form': form}
    return render(request, 'information/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    information 질문댓글수정
    """
    comment = get_object_or_404(CommentInformation, pk=comment_id)
    if request.user != comment.author_information:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('information:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentInformationForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_information = request.user
            comment.modify_date_information = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('information:detail', question_id=comment.question_information.id), comment.id))
    else:
        form = CommentInformationForm(instance=comment)
    context = {'form': form}
    return render(request, 'information/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    information 질문댓글삭제
    """
    comment = get_object_or_404(CommentInformation, pk=comment_id)
    if request.user != comment.author_information:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('information:detail', question_id=comment.question_id)
    else:
        comment.delete()
    return redirect('information:detail', question_id=comment.question_id)

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """
    information 답글댓글등록
    """
    answer = get_object_or_404(AnswerInformation, pk=answer_id)
    if request.method == "POST":
        form = CommentInformationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_information = request.user
            comment.create_date_information = timezone.now()
            comment.answer_information = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('information:detail', question_id=comment.answer_information.question_information.id), comment.id))
    else:
        form = CommentInformationForm()
    context = {'form': form}
    return render(request, 'information/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    information 답글댓글수정
    """
    comment = get_object_or_404(CommentInformation, pk=comment_id)
    if request.user != comment.author_information:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('information:detail', question_id=comment.answer_information.question_information.id)

    if request.method == "POST":
        form = CommentInformationForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_information = request.user
            comment.modify_date_information = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('information:detail', question_id=comment.answer_information.question_information.id), comment.id))
    else:
        form = CommentInformationForm(instance=comment)
    context = {'form': form}
    return render(request, 'information/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    information 답글댓글삭제
    """
    comment = get_object_or_404(CommentInformation, pk=comment_id)
    if request.user != comment.author_information:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('information:detail', question_id=comment.answer_information.question_information.id)
    else:
        comment.delete()
    return redirect('information:detail', question_id=comment.answer_information.question_information.id)