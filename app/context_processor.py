from . models import Solutions, Sector
from careers.models import Category
from about.models import OrganizationSetting
from app.models import Office,AssocialtedCompany

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

def career_category(request):
    categories = Category.objects.all()
    return({
        'careers_categories':categories
    })


def organizationsetting(request):
    organization_setting = OrganizationSetting.objects.first()
    return ({
        'organization_settings': organization_setting
    })


def locations(request):
    all_office_locations = Office.objects.all()[:5]
    return({
        'office_locations':all_office_locations
    })


def associated_compnay(request):
    associated_companies = AssocialtedCompany.objects.all()
    return ({
        'associated_companies':associated_companies
    })