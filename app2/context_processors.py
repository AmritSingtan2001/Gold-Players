from app.models import AboutUS

def aboutus(request):
    aboutus = AboutUS.objects.first()
    return {'aboutUs': aboutus}