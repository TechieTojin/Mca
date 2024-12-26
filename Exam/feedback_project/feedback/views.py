from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Here you can handle the data, save it to the database or send an email
            return render(request, 'feedback/thank_you.html', {'form': form})
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})
