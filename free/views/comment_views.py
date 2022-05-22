from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentFreeForm
from ..models import QuestionFree, AnswerFree, CommentFree

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    free 질문댓글등록
    """
    question = get_object_or_404(QuestionFree, pk=question_id)
    if request.method == "POST":
        form = CommentFreeForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_free = request.user
            comment.create_date_free = timezone.now()
            comment.question_free = question #질문에 대한 댓글이므로 comment에 question저장.
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('free:detail', question_id=comment.question_free.id), comment.id))
    else:
        form = CommentFreeForm()
    context = {'form': form}
    return render(request, 'free/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    free 질문댓글수정
    """
    comment = get_object_or_404(CommentFree, pk=comment_id)
    if request.user != comment.author_free:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('free:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentFreeForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_free = request.user
            comment.modify_date_free = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('free:detail', question_id=comment.question_free.id), comment.id))
    else:
        form = CommentFreeForm(instance=comment)
    context = {'form': form}
    return render(request, 'free/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    free 질문댓글삭제
    """
    comment = get_object_or_404(CommentFree, pk=comment_id)
    if request.user != comment.author_free:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('free:detail', question_id=comment.question_id)
    else:
        comment.delete()
    return redirect('free:detail', question_id=comment.question_id)

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """
    free 답글댓글등록
    """
    answer = get_object_or_404(AnswerFree, pk=answer_id)
    if request.method == "POST":
        form = CommentFreeForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_free = request.user
            comment.create_date_free = timezone.now()
            comment.answer_free = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('free:detail', question_id=comment.answer_free.question_free.id), comment.id))
    else:
        form = CommentFreeForm()
    context = {'form': form}
    return render(request, 'free/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    free 답글댓글수정
    """
    comment = get_object_or_404(CommentFree, pk=comment_id)
    if request.user != comment.author_free:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('free:detail', question_id=comment.answer_free.question_free.id)

    if request.method == "POST":
        form = CommentFreeForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_free = request.user
            comment.modify_date_free = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('free:detail', question_id=comment.answer_free.question_free.id), comment.id))
    else:
        form = CommentFreeForm(instance=comment)
    context = {'form': form}
    return render(request, 'free/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    free 답글댓글삭제
    """
    comment = get_object_or_404(CommentFree, pk=comment_id)
    if request.user != comment.author_free:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('free:detail', question_id=comment.answer_free.question_free.id)
    else:
        comment.delete()
    return redirect('free:detail', question_id=comment.answer_free.question_free.id)