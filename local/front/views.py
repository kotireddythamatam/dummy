from django.shortcuts import render
from .models import Registration_Model
from .forms import Registration_Form
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
import logging
logger = logging.basicConfig(filename='mahesh.log',filemode="a",format='%(asctime)s :: %(levelname)s :: %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create your views here.
def front(request):
    if request.session.has_key('email_id'):
        return render(request,'front/front.html')
    return HttpResponseRedirect('/front/login')

def login_view1(request):
    if request.method=="GET":
        return render(request,'front/login.html')

def login_view2(request):
    if request.method=="GET":
        un=request.GET.get('e')
        pw=request.GET.get('p')
        print(un,pw)
        model_obj=Registration_Model.objects.filter(email_id=un,password=pw)
        if model_obj:
            request.session['email_id']=un
            request.session.set_expiry(60)
            return HttpResponseRedirect('front/login.html')
            # data="ok"
            # return HttpResponse(data)
        else:
            # return render(request,'front/login.html')
            data="fail"
            return HttpResponse(data)

def registration_view(request):
    if request.method=="GET":
        logger.critical('new form created')
        form=Registration_Form()
        return render(request,'front/registration.html',{'form':form})
    elif request.method=="POST":
        logger.warning('it is post method')
        form=Registration_Form(request.POST)
        if form.is_valid():
            model_obj=Registration_Model(
            first_name=form.cleaned_data['First_name'],
            last_name=form.cleaned_data['Last_name'],
            email_id=form.cleaned_data['Email_id'],
            password=form.cleaned_data['Password'],
            conform_password=form.cleaned_data['Conform_password'],
            phone=form.cleaned_data['Phone_number'],
            gender=form.cleaned_data['Gender']
            )
            model_obj.save()
            logger.info('data saved')
            messages.success(request,'Registration is successfull')
            return HttpResponseRedirect('/front/login1')
        return render(request,'front/registration.html',{'form':form})


em=""
obj_id=0
def to_mail(request):
    if request.method=="GET":
        return render(request,'front/to_mail.html')
    elif request.method=="POST":
        global em
        em=request.POST.get('e')
        model_obj=Registration_Model.objects.get(email_id=em)
        obj_id=model_obj.id
        if model_obj:
            return render(request,'front/links.html')
        return HttpResponse('send current mail')

def otp_to_mail(request):
    if request.method=="GET":
        otp=random.randrange(1000,9999)
        mail=smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_PORT_PASSWORD)
        subject='from django'
        massege='otp:'+str(otp)
        To=[em,]
        send_mail(subject,massage,settings.EMAIL_HOST_USER,To,fail_silently=True)
        response=render(request,'front/otp.html')
        response.set_cookie('otp',otp)
        return response
    elif request.method=="POST":
        user_otp=request.POST['otp']
        print(request.COOKIES['otp'])
        print(user_otp)
        if request.COOKIES['otp'] == user_otp:
            return HttpResponseRedirect('/front/change_password')
        return HttpResponse('otp not matched')

def change_password(request):
    if request.method == "GET":
        return render(request,'front/change_password.html')
    elif request.method == "POST":
        p1 = request.POST['p1']
        p2 = request.POST.get('p2')
        if p1 == p2:
            model_obj = Registration_Model.objects.get(id=obj_id)
            model_obj.password = p1
            model_obj.conform_password = p2
            model_obj.save()
            return HttpResponse('password changed')
        else:
            return HttpResponse('two fields must be same')

def link_to_mail(request):
        if request.method == "GET":
            mail = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
            mail.ehlo()
            mail.starttls()
            mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
            subject = 'from smtp'
            message = "Link : " + "http://127.0.0.1:8080/front/change_password"
            To = [em,]
            send_mail(subject,message,settings.EMAIL_HOST_USER,To,fail_silently=True)
            return HttpResponse('plese click on link')
