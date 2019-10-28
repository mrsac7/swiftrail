from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pnr_status(request):
    return render(request, 'pnr-status.html')

def train_enquiry(request):
    return render(request, 'train-enquiry.html')

def train_schedule(request):
    return render(request, 'train-schedule.html')

def train_search(request):
    return render(request, 'train-search.html')

def book_ticket(request):
    return render(request, 'book-ticket.html')