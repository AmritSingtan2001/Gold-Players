from . models import Solutions, Sector,Location

def solutions(request):
    solutions_data = Solutions.objects.all()

    context = {
        'solution_category': solutions_data
    }
    return context

def sectors(request):
    secots_all = Sector.objects.all()

    context = {
        'secotrs':secots_all
    }
    return context
