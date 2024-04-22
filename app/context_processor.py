from . models import Solutions, Sector

def solutions(request):
    solutions_data = Solutions.objects.all()
    solution_category = [solution.title for solution in solutions_data]

    context = {
        'solution_category': solution_category
    }
    return context

def sectors(request):
    secots_all = Sector.objects.all()
    sector_category = [secotr.title for secotr in secots_all]

    context = {
        'sector_category': sector_category
    }
    return context