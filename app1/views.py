from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, request
from .models import ContactSubmission
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib.auth.decorators import login_required



@csrf_exempt
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Get IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Save to database
        submission = ContactSubmission(
            name=name,
            email=email,
            message=message,
            ip_address=ip
        )
        submission.save()

        return JsonResponse({'status': 'success', 'message': 'Thank you for your message!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



@login_required
def view_submissions(request):
    submissions = ContactSubmission.objects.all().order_by('-submission_date')
    return render(request, 'view_submissions.html', {'submissions': submissions})


def home(request):
    return render(request, 'index.html')
