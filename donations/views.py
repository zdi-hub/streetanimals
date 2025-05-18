from django.shortcuts import render, redirect
from .forms import DonationForm, TestimonialForm
from .models import Testimonial

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def testimonials(request):
    all_testimonials = Testimonial.objects.order_by('-created_at')
    return render(request, 'testimonials.html', {'testimonials': all_testimonials})

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'submit_testimonial.html', {'form': form})
