from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentMinorForm
from ..models import QuestionMinor, AnswerMinor, CommentMinor

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    minorboard 질문댓글등록
    """
    question = get_object_or_404(QuestionMinor, pk=question_id)
    if request.method == "POST":
        form = CommentMinorForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_minor = request.user
            comment.create_date_minor = timezone.now()
            comment.question_minor = question #질문에 대한 댓글이므로 comment에 question저장.
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('minorboard:detail', question_id=comment.question_minor.id), comment.id))
    else:
        form = CommentMinorForm()
    context = {'form': form}
    return render(request, 'minorboard/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    minorboard 질문댓글수정
    """
    comment = get_object_or_404(CommentMinor, pk=comment_id)
    if request.user != comment.author_minor:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('minorboard:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentMinorForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_minor = request.user
            comment.modify_date_minor = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('minorboard:detail', question_id=comment.question_minor.id), comment.id))
    else:
        form = CommentMinorForm(instance=comment)
    context = {'form': form}
    return render(request, 'minorboard/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    minorboard 질문댓글삭제
    """
    comment = get_object_or_404(CommentMinor, pk=comment_id)
    if request.user != comment.author_minor:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('minorboard:detail', question_id=comment.question_id)
    else:
        comment.delete()
    return redirect('minorboard:detail', question_id=comment.question_id)

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """
    minorboard 답글댓글등록
    """
    answer = get_object_or_404(AnswerMinor, pk=answer_id)
    if request.method == "POST":
        form = CommentMinorForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_minor = request.user
            comment.create_date_minor = timezone.now()
            comment.answer_minor = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('minorboard:detail', question_id=comment.answer_minor.question_minor.id), comment.id))
    else:
        form = CommentMinorForm()
    context = {'form': form}
    return render(request, 'minorboard/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    minorboard 답글댓글수정
    """
    comment = get_object_or_404(CommentMinor, pk=comment_id)
    if request.user != comment.author_minor:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('minorboard:detail', question_id=comment.answer_minor.question_minor.id)

    if request.method == "POST":
        form = CommentMinorForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_minor = request.user
            comment.modify_date_minor = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('minorboard:detail', question_id=comment.answer_minor.question_minor.id), comment.id))
    else:
        form = CommentMinorForm(instance=comment)
    context = {'form': form}
    return render(request, 'minorboard/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    minorboard 답글댓글삭제
    """
    comment = get_object_or_404(CommentMinor, pk=comment_id)
    if request.user != comment.author_minor:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('minorboard:detail', question_id=comment.answer_minor.question_minor.id)
    else:
        comment.delete()
    return redirect('minorboard:detail', question_id=comment.answer_minor.question_minor.id)