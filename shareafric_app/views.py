from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import *

# Create your views here.
def main(request):
    page = Webdata.objects.first()
    client = Client.objects.all()
    fact = Facts.objects.first()
    service = Service.objects.all()
    skillright = SkillRight.objects.all()
    skillleft = SkillLeft.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    portfolio = Portfolio.objects.all()
    service = Service.objects.all()
    client = Client.objects.all()


    return render(request, 'MyResume/index.html',{
        'pages': page,
        'client': client,
        'fact': fact,
        'service': service,
        'skillright': skillright,
        'skillleft': skillleft,
        'education':education,
        'experience':experience,
        'portfolio': portfolio,
        'service': service,
        'client': client,
        })

def handle_error_page(request, exception):
    page = Webdata.objects.first()
    client = Client.objects.all()
    fact = Facts.objects.first()
    service = Service.objects.all()
    skillright = SkillRight.objects.all()
    skillleft = SkillLeft.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    portfolio = Portfolio.objects.all()
    service = Service.objects.all()
    client = Client.objects.all()  
    return render(request, 'pages/404.html',{
        'pages': page,
        'client': client,
        'fact': fact,
        'service': service,
        'skillright': skillright,
        'skillleft': skillleft,
        'education':education,
        'experience':experience,
        'portfolio': portfolio,
        'service': service,
        'client': client,  # Use the assigned value of 'partners'
    })
# def home(request):
#     return render(request, 'shareafric_app/test.html')


# def about(request):
#     webdata = Webdata.objects.first()
#     team_members = theTeam.objects.all()
#     services = service.objects.all()
#     return render(request, 'pages/about.html',{
#         'webdata': webdata,
#         'team_members': team_members,
#         'services': services,
        
#         })

def contactUs(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message= request.POST.get('message')

        # Data validation
        if not name and not email and not subject and not message:
            response = {'message': 'Please provide all info necessary to contact me!'}
            return JsonResponse(response, status=400)

        # Save the form data to a model
        form_data = ContactUs(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        form_data.save()

        context = {'user': name, 'message': message}
        html_message = render_to_string('shareafric_app/info.html', context)
        html_message2 = render_to_string('shareafric_app/info2.html', context)
        send_mail('Welcome to Wisteen Technology', '', 'wisteen.technology@shareafric.com', [email], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')
        send_mail('Hello Wisdom Some one have contacted you!', '', 'wisteen.technology@shareafric.com', ["wisdomisaac168@gmail.com", "okuwisdom8@gmail.com"], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

        # Return a success JSON response
        response = {'message': 'Form submitted successfully We will get back throught your email'}
        return JsonResponse(response)
    else:
        return render(request, 'MyResume/index.html')  # Render the form template initially

def error_400_view(request, exception):
    return render(request, 'home/400.html', status=400)

def error_403_view(request, exception):
    return render(request, 'home/403.html', status=403)

def error_404_view(request, exception):
    return render(request, 'home/404.html', status=404)

def error_500_view(request):
    return render(request, 'home/500.html', status=500)

def error_401_view(request, exception=None):
    return render(request, 'home/401.html', status=401)
