from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentDoubleForm
from ..models import QuestionDouble, AnswerDouble, CommentDouble

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    doubleboard 질문댓글등록
    """
    question = get_object_or_404(QuestionDouble, pk=question_id)
    if request.method == "POST":
        form = CommentDoubleForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_double = request.user
            comment.create_date_double = timezone.now()
            comment.question_double = question #질문에 대한 댓글이므로 comment에 question저장.
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('doubleboard:detail', question_id=comment.question_double.id), comment.id))
    else:
        form = CommentDoubleForm()
    context = {'form': form}
    return render(request, 'doubleboard/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    doubleboard 질문댓글수정
    """
    comment = get_object_or_404(CommentDouble, pk=comment_id)
    if request.user != comment.author_double:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('doubleboard:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentDoubleForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_double = request.user
            comment.modify_date_double = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('doubleboard:detail', question_id=comment.question_double.id), comment.id))
    else:
        form = CommentDoubleForm(instance=comment)
    context = {'form': form}
    return render(request, 'doubleboard/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    doubleboard 질문댓글삭제
    """
    comment = get_object_or_404(CommentDouble, pk=comment_id)
    if request.user != comment.author_double:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('doubleboard:detail', question_id=comment.question_id)
    else:
        comment.delete()
    return redirect('doubleboard:detail', question_id=comment.question_id)

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """
    doubleboard 답글댓글등록
    """
    answer = get_object_or_404(AnswerDouble, pk=answer_id)
    if request.method == "POST":
        form = CommentDoubleForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_double = request.user
            comment.create_date_double = timezone.now()
            comment.answer_double = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('doubleboard:detail', question_id=comment.answer_double.question_double.id), comment.id))
    else:
        form = CommentDoubleForm()
    context = {'form': form}
    return render(request, 'doubleboard/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    doubleboard 답글댓글수정
    """
    comment = get_object_or_404(CommentDouble, pk=comment_id)
    if request.user != comment.author_double:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('doubleboard:detail', question_id=comment.answer_double.question_double.id)

    if request.method == "POST":
        form = CommentDoubleForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_double = request.user
            comment.modify_date_double = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('doubleboard:detail', question_id=comment.answer_double.question_double.id), comment.id))
    else:
        form = CommentDoubleForm(instance=comment)
    context = {'form': form}
    return render(request, 'doubleboard/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    doubleboard 답글댓글삭제
    """
    comment = get_object_or_404(CommentDouble, pk=comment_id)
    if request.user != comment.author_double:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('doubleboard:detail', question_id=comment.answer_double.question_double.id)
    else:
        comment.delete()
    return redirect('doubleboard:detail', question_id=comment.answer_double.question_double.id)