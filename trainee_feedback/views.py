from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TraineeFeedback

def feedback_view(request):
    all_feedback_form_answers = TraineeFeedback.objects.all()
    return render(
        request, 
        'feedback.html'
    )

def add_feedback_view(request):
    #print(request.POST.get['content'])
    # Get feedback
    questionOne = request.POST['question_one']
    questionTwo = request.POST['question_two']
    questionThree = request.POST['question_three']
    questionFour = request.POST['question_four']
    questionFive = request.POST['question_five']
    #print('questionOne-'+questionOne+'\n'+'questionTwo-'+questionTwo+'\n'+'questionThree-'+questionThree+'\n'+'questionFour-'+questionFour+'\n'+'questionFive-'+questionFive)
    new_feedback = TraineeFeedback(
        questionOne = request.POST['question_one'],
        questionTwo = request.POST['question_two'],
        questionThree = request.POST['question_three'],
        questionFour = request.POST['question_four'],
        questionFive = request.POST['question_five'])

    # Save to DB
    new_feedback.save()

    # Redirect
    return HttpResponseRedirect('/thankyou/')


def thankyou_view(request):
    return render(request, 'thankyou.html')

def trainer_view(request):
    all_feedback_form_answers = TraineeFeedback.objects.all()
    return render(request, 'trainer.html', {'all_feedback_form_answers': all_feedback_form_answers})

def report_view(request):
 return render(request, 'report.html')