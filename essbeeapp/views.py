import json
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Blog, Contact,Appointment,Testimonials,Clients,Email_subscription,Blog_Comment
from essbee.settings import EMAIL_HOST_USER
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib import messages


# Create your views here.
def index(request):
    blog= Blog.objects.all().order_by('-date')[:4]
    test=Testimonials.objects.all()
    clients=Clients.objects.all()

    context = {
        'blog': blog,
        'test':test,
        'client':clients,

    }
    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    recent_blog= Blog.objects.all().order_by('-date')[:3]
    blogs = Blog.objects.all()[:3]
    context = {
        'blogss': recent_blog,
        'blogs': blogs,
    }

    return render(request, 'blog.html', context)


def blog_details(request, b_slug):
    recent_blog = Blog.objects.all().order_by('-date')[:3]
    blog = Blog.objects.get(slug=b_slug)
    blog_comment = Blog_Comment.objects.filter(slug=b_slug)
    blog_count=blog_comment.count()

    context = {
        'blog': blog,
        'recent_blog':recent_blog,
        'reviews': blog_comment,
        'blog_count':blog_count,

    }

    return render(request, 'blog-details.html', context)


def chat_bot(request):
    clients = Clients.objects.all()
    context = {

        'client': clients
    }
    return render(request, 'chatbot.html',context)


def iot(request):
    return render(request, 'Iot.html')


def ai(request):
    clients = Clients.objects.all()
    context = {

        'client': clients
    }
    return render(request, 'ai.html',context)


def mobile_development(request):
    return render(request, 'mobiledevelop.html')


def network(request):
    clients = Clients.objects.all()
    context = {

        'client': clients
    }
    return render(request, 'network.html',context)


def web_design(request):
    return render(request, 'webdesign.html')


def career(request):
    return render(request, 'career.html')


def contact(request):
    return render(request, 'contact.html')


def ContactView(request):
    if request.method == 'POST':
        name = request.POST['name']
        from_email = request.POST['from_email']
        mobile_num = request.POST['mobile_num']
        subject = request.POST['subject']
        message = request.POST['message']

        # ''' Begin reCAPTCHA validation '''

        captcha_token = request.POST.get('g-recaptcha-response')
        cap_url = 'https://www.google.com/recaptcha/api/siteverify'
        cap_secret = '6Lfnoc8aAAAAAGf3VbYh4gVBMX8nhuMmkc6TpvTs'
        cap_data = {'secret': cap_secret, 'response': captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)
        # ''' End reCAPTCHA validation '''

        if cap_json['success'] == True:
            contact = Contact(name=name, mobile_num=mobile_num, from_email=from_email, message=message, subject=subject)
            contact.save()
            if name and from_email:
                try:
                    send_mail('Essbee Infotech',
                              'Thank you for getting in touch! We appreciate you contacting us. One of our colleagues will get back in touch with you soon!Have a great day!',
                              EMAIL_HOST_USER,
                              [from_email, 'shibilymuhammed@essbeeinfotech.com', 'ajaymol@essbeeinfotech.com'],
                              fail_silently=False)
                    print("mail send")
                    messages.info(request, "Thank you for contacting us.")
                    return redirect('contact')

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                messages.info(request, "invalid entry.")
        else:

            messages.error(request, "Invalid Captcha, Try Again")
            return redirect('contact')

        return render(request, 'contact.html')
def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        website= request.POST['website']
        appointment=Appointment(name=name,email=email,phone=phone,website=website)
        appointment.save()
        messages.info(request, "Thank you for contacting us.")
        return redirect('index')
    else:
        return render(request, 'index.html')

def consultation(request):
    if request.method == 'POST':
        name = request.POST['name']
        from_email = request.POST['from_email']
        mobile_num = request.POST['mobile_num']
        subject = request.POST['subject']
        message = request.POST['message']

        # ''' Begin reCAPTCHA validation '''

        captcha_token = request.POST.get('g-recaptcha-response')
        cap_url = 'https://www.google.com/recaptcha/api/siteverify'
        cap_secret = '6Lfnoc8aAAAAAGf3VbYh4gVBMX8nhuMmkc6TpvTs'
        cap_data = {'secret': cap_secret, 'response': captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)
        # ''' End reCAPTCHA validation '''

        if cap_json['success'] == True:
            contact = Contact(name=name, mobile_num=mobile_num, from_email=from_email, message=message, subject=subject)
            contact.save()
            if name and from_email:
                try:
                    send_mail('Essbee Infotech',
                              'Thank you for getting in touch! We appreciate you contacting us. One of our colleagues will get back in touch with you soon!Have a great day!',
                              EMAIL_HOST_USER,
                              [from_email, 'shibilymuhammed@essbeeinfotech.com', 'ajaymol@essbeeinfotech.com'],
                              fail_silently=False)
                    print("mail send")
                    messages.info(request, "Thank you for contacting us.")
                    return redirect('about')

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                messages.info(request, "invalid entry.")
        else:

            messages.error(request, "Invalid Captcha, Try Again")
            return redirect('about')

        return render(request, 'about.html')

def email_subscription(request):
    if request.method=='POST':
        email=request.POST['email']
        subscribe=Email_subscription(email=email)
        subscribe.save()
        messages.info(request,"Thank you! Subscribed Succesfully")
        return redirect('/')
    else:
        return render(request, 'index.html')

def add_reviews(request):
    if request.method == "POST":
        slug = request.POST.get("slug")
        blog = Blog.objects.get(slug=slug)
        name = request.POST['name']
        email=request.POST['email']
        message = request.POST['message']
        reviews = Blog_Comment(blog=blog, message=message, slug=slug,name=name,email=email)
        reviews.save()
        messages.success(request, "Thank you for reviewing this blog!!")
    return redirect(f"/blog/{blog.slug}")



