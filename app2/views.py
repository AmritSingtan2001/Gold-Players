from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from django.views import View
from . decorators import login_required
from django.contrib import messages
from django.contrib import auth
from . forms import *
from app.models import *
from about.models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from . new_file_handler import validate_file
from django.http import JsonResponse



@login_required
def index(request):
    return render(request,'app2/index.html')




@login_required
def aboutUs(request):
    instance = None
    try:
        if id:
            instance = About.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the AboutUS.')
        return redirect('dashboard:aboutUs')

    if request.method == 'POST':
        form = AboutUSForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance: 
                messages.success(request, 'AboutUS edited successfully.')
                return redirect('dashboard:about') 
            else: 
                messages.success(request, 'AboutUS added successfully.')
                return redirect('dashboard:about') 
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutUSForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_about_us.html', context)


@login_required
def organizationsetting(request):
    instance = None
    try:
        if id:
            instance = OrganizationSetting.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the AboutUS.')
        return redirect('dashboard:organizations_setting')

    if request.method == 'POST':
        form = OrganizationSettingForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance: 
                messages.success(request, 'AboutUS edited successfully.')
                return redirect('dashboard:organizations_setting') 
            else: 
                messages.success(request, 'AboutUS added successfully.')
                return redirect('dashboard:organizations_setting') 
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = OrganizationSettingForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/organization_setting.html', context)


@login_required
def organization_objectives(request):
    instance = None
    try:
        if id:
            instance = Objective.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the AboutUS.')
        return redirect('dashboard:organizations_setting')

    if request.method == 'POST':
        form = ObjectiveForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance: 
                messages.success(request, 'AboutUS edited successfully.')
                return redirect('dashboard:organizations_setting') 
            else: 
                messages.success(request, 'AboutUS added successfully.')
                return redirect('dashboard:organizations_setting') 
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ObjectiveForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/organization_setting.html', context)




# #news categorei
# @login_required
# def add_edit_MainCategorie(request, id=None):
#     instance = None
#     try:
#         if id:
#             instance = MainCategorie.objects.get(pk=id)
#     except Exception as e:
#         messages.warning(request, 'An error occurred while retrieving the MainCategorie.')
#         return redirect('dashboard:add_MainCategorie')

#     if request.method == 'POST':
#         form = MainCategorieForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'MainCategorie edited successfully.')
#                 return redirect('dashboard:edit_MainCategorie', id=instance.id)  # Redirect to the edited MainCategorie's details page
#             else:  # Add operation
#                 messages.success(request, 'MainCategorie added successfully.')
#                 return redirect('dashboard:add_MainCategorie')  # Redirect to the page for adding new MainCategories
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = MainCategorieForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/create_MainCategorie.html', context)

# @login_required
# def mainCategories(request):
#     MainCategories=MainCategorie.objects.all()
#     p=Paginator(MainCategories,10)
#     page_number= request.GET.get('page')
#     MainCategories=p.get_page(page_number)
#     return render(request, 'app2/MainCategorie.html',{'details':MainCategories})

# @login_required
# def deleteMainCategorie(request, id):
#     record = get_object_or_404(MainCategorie, id=id)

#     if request.method == 'POST':
#         record.delete()
#         return redirect('dashboard:mainCategorie')  # Redirect to a list view after deletion
#     else:
#         return render(request, 'app2/MainCategorie.html', {'details': record})



# #news subcategorie
# @login_required
# def add_edit_SubCategories(request, id=None):
#     instance = None
#     try:
#         if id:
#             instance = SubCategorie.objects.get(pk=id)
#     except Exception as e:
#         messages.warning(request, 'An error occurred while retrieving the SubCategories.')
#         return redirect('dashboard:add_SubCategories')

#     if request.method == 'POST':
#         form = SubCategorieForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'SubCategories edited successfully.')
#                 return redirect('dashboard:edit_SubCategories', id=instance.id)  # Redirect to the edited SubCategories's details page
#             else:  # Add operation
#                 messages.success(request, 'SubCategories added successfully.')
#                 return redirect('dashboard:add_SubCategories')  # Redirect to the page for adding new SubCategoriess
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = SubCategorieForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/create_SubCategories.html', context)

# @login_required
# def subCategories(request):
#     SubCategories=MainCategorie.objects.all()
#     p=Paginator(SubCategories,4)
#     page_number= request.GET.get('page')
#     SubCategories=p.get_page(page_number)
#     return render(request, 'app2/SubCategories.html',{'details':SubCategories})

# @login_required
# def deleteSubCategories(request, id):
#     record = SubCategorie.objects.get(pk=id)
#     if request.method == 'POST':
#         record.delete()
#         messages.success(request,'Sub Categorie Deleted Successfully !')
#         return redirect('dashboard:subCategorie')  # Redirect to a list view after deletion
#     else:
#         return render(request, 'app2/SubCategories.html', {'details': record})



# @login_required 
# def newsList(request):
#     allnews = News.objects.all()
#     return render(request,'app2/news_table.html',{'allNews':allnews})


# # @login_required
# # def createNews(request):
# #     allcategorie= MainCategorie.objects.all()
# #     tag= Tag.objects.all()
# #     user= request.user
# #     if request.method=="POST":
# #         newstitle = request.POST['title']
# #         maincategorie= request.POST['categoryselect']
# #         mainctg = MainCategorie.objects.get(id=maincategorie)
# #         subcategorie = request.POST['subcategory']
# #         if subcategorie:
# #             subctg = SubCategorie.objects.get(id =subcategorie)
# #         else:
# #             subctg =None
# #         tag = request.POST['tag']
# #         headline = request.POST['headline']
# #         latest = request.POST['latest']
# #         # news_reporter =User.objects.get(id=reporter)
# #         trending_status=request.POST['trending']
# #         highlight=request.POST['highlight']
# #         # short_description = request.POST['shortdiscription']
# #         news_description = request.POST['description']
# #         news_image = request.FILES['newsimage']
# #         new_news= News.objects.create( 
# #                                       categorie=mainctg,
# #                                       subCategorie=subctg,
# #                                       title=newstitle,
# #                                       tag=tag,
# #                                       headline=headline,
# #                                       latest=latest,
# #                                       discriptions=news_description,
# #                                       image =news_image,
# #                                       highlight =highlight,
# #                                       trending= trending_status,
                                      
# #                                       )
# #         new_news.save()
# #         messages.success(request,'News added successfully !')
# #         return redirect('dashboard:createnews')

# #     else:
# #         return render(request,'app2/create_news.html',{'allcategorie':allcategorie,
# #                                                        'user':user,
# #                                                        'tag':tag
# #                                                        })
# # @login_required
# # def editeNews(request, slug=None):
# #     news = News.objects.get(news_slug =slug)
# #     allcategorie= MainCategorie.objects.all()
# #     user= request.user
# #     if request.method=="POST":
# #         news.title = request.POST['title']
# #         maincategorie= request.POST['categoryselect']
# #         news.categorie = MainCategorie.objects.get(id=maincategorie)
# #         subcategorie = request.POST['subcategory']
# #         if subcategorie:
# #             news.subCategorie = SubCategorie.objects.get(id =subcategorie)
# #         else:
# #             news.subCategorie =None

# #         news.trending=request.POST['trending']
# #         news.discriptions = request.POST['description']
# #         if 'newsimage' in request.FILES:
# #             news.image = request.FILES['newsimage']
    
        
# #         news.save()
# #         messages.success(request,'News updated successfully !')
# #         return redirect('dashboard:edite_news', slug=news.news_slug)

    
# #     return render(request,'app2/edite_news.html',{'news':news,
# #                                                   'allcategorie':allcategorie,
# #                                                     'user':user
# #                                                   })

# @login_required
# def deletenews(request, slug):
#     relatedNews= News.objects.get(news_slug=slug)
#     relatedNews.delete()
#     messages.success(request,"News deleted successfullY !")
#     return redirect('dashboard:allnews')

# @login_required
# def load_sub_category(request):
#     main_ctg_id = request.GET.get('programming')
#     print(main_ctg_id)
#     sub_category = SubCategorie.objects.filter(maincategorie=main_ctg_id)
#     return render(request,'app2/listdropdow.html',{'sub_category':sub_category})




# # ads sections
# @login_required
# def add_edit_HorizontalAds(request, id=None):
#     instance = None
#     try:
#         if id:
#             instance = HorizontalAds.objects.get(pk=id)
#     except Exception as e:
#         print(e)
#         messages.warning(request, 'An error occurred while retrieving the HorizontalAds.')
#         return redirect('dashboard:add_HorizontalAds')

#     if request.method == 'POST':
#         form = HorizontalAdsForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'HorizontalAds edited successfully.')
#                 return redirect('dashboard:edit_HorizontalAds', id=instance.id)  # Redirect to the edited HorizontalAds's details page
#             else:  # Add operation
#                 messages.success(request, 'HorizontalAds added successfully.')
#                 return redirect('dashboard:add_HorizontalAds')  # Redirect to the page for adding new HorizontalAdss
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = HorizontalAdsForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/create_horizontal_ads.html', context)

# @login_required
# def horizontalAds(request):
#     horizontalAds=HorizontalAds.objects.all()
#     p=Paginator(horizontalAds,10)
#     page_number= request.GET.get('page')
#     horizontalAds=p.get_page(page_number)
#     return render(request, 'app2/horizontalAds.html',{'details':horizontalAds})

# @login_required
# def deletehorizontalAds(request, id):
#     record = get_object_or_404(HorizontalAds, id=id)

#     if request.method == 'POST':
#         record.delete()
#         return redirect('dashboard:horizontalAds')  # Redirect to a list view after deletion

#     return render(request, 'app2/horizontalAds.html', {'details': record})



# # ads sections
# @login_required
# def add_edit_verticleAds(request, id=None):
#     instance = None
#     try:
#         if id:
#             instance = VerticleAds.objects.get(pk=id)
#     except Exception as e:
#         print(e)
#         messages.warning(request, 'An error occurred while retrieving the verticleAds.')
#         return redirect('dashboard:add_verticleAds')

#     if request.method == 'POST':
#         form = VerticleAdsForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'verticleAds edited successfully.')
#                 return redirect('dashboard:edit_verticleAds', id=instance.id)  # Redirect to the edited verticleAds's details page
#             else:  # Add operation
#                 messages.success(request, 'verticleAds added successfully.')
#                 return redirect('dashboard:add_verticleAds')  # Redirect to the page for adding new verticleAdss
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = VerticleAdsForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/create_verticle_ads.html', context)

# @login_required
# def verticleAds(request):
#     verticleAds=VerticleAds.objects.all()
#     p=Paginator(verticleAds,10)
#     page_number= request.GET.get('page')
#     verticleAds=p.get_page(page_number)
#     return render(request, 'app2/verticle_ads.html',{'details':verticleAds})

# @login_required
# def deleteverticleAds(request, id):
#     record = get_object_or_404(HorizontalAds, id=id)

#     if request.method == 'POST':
#         record.delete()
#         return redirect('dashboard:verticleAds')  # Redirect to a list view after deletion

#     return render(request, 'app2/verticleAds.html', {'details': record})

# @login_required
# def popUpAds(request):
#     instance = None
#     try:
#         if id:
#             instance = PopUpAds.objects.first()
#     except Exception as e:
#         messages.warning(request, 'An error occurred while retrieving the AboutUS.')
#         return redirect('dashboard:popUpAds')

#     if request.method == 'POST':
#         form = PopUpAdsForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'Pop-Up Ads updated successfully.')
#                 return redirect('dashboard:popUpAds')  # Redirect to the edited popUpAds's details page
#             else:  # Add operation
#                 messages.success(request, 'Pop-Up Ads updated successfully.')
#                 return redirect('dashboard:popUpAds')  # Redirect to the page for adding new popUpAdss
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = PopUpAdsForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/popupads.html', context)


# @login_required
# def Contact_Us(request):
#     ContactUs_details=ContactUs.objects.all()
#     p=Paginator(ContactUs_details,4)
#     page_number= request.GET.get('page')
#     ContactUs_details=p.get_page(page_number)
#     return render(request,'app2/contact_Us.html',{'details':ContactUs_details})

# @login_required
# def deleteContactUs(request, id):
#     record = get_object_or_404(ContactUs, id=id)

#     if request.method == 'POST':
#         record.delete()
#         return redirect('dashboard:contactUs')  # Redirect to a list view after deletion

#     return render(request, 'app2/Contact_Us.html', {'details': record})



# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             # update_session_auth_hash(request, user)  # Important to update the session after password change
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('dashboard:change_password')  # Redirect to the same view after successful password change
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = PasswordChangeForm(request.user)
    
#     return render(request, 'app2/change_password.html', {'form': form})


# # @login_required
# # def audio(request):
# #     instance = None
# #     try:
# #         if id:
# #             instance = RadioStream.objects.first()
# #     except Exception as e:
# #         messages.warning(request, 'An error occurred while retrieving the Audio.')
# #         return redirect('dashboard:audio')
# #     if request.method == 'POST':
# #         form = RadioStreamForm(request.POST, request.FILES, instance=instance)
# #         if form.is_valid():
# #             form.save()
# #             if instance:  # Edit operation
# #                 messages.success(request, 'audio edited successfully.')
# #                 return redirect('dashboard:audio')  # Redirect to the edited audio's details page
# #             else:  # Add operation
# #                 messages.success(request, 'audio added successfully.')
# #                 return redirect('dashboard:audio')  # Redirect to the page for adding new audios
# #         else:
# #             messages.warning(request, 'Form is not valid. Please correct the errors.')
# #     else:
# #         form = RadioStreamForm(instance=instance)
# #     context = {'form': form, 'instance': instance}
# #     return render(request, 'app2/create_audio.html', context)



# # @login_required
# # def about(request):
# #     about= AboutUS.objects.first()
# #     return render(request,'app2/about.html',{'about':about})

# # @login_required
# # def update_about(request):
# #     if request.method=="POST":
# #         id= request.POST['id']
# #         about = AboutUS.objects.get(id= id)
# #         about.introduction= request.POST['introduction']
# #         about.our_story= request.POST['our_story']
# #         if 'story_image' in request.FILES:
# #             image_file = request.FILES['image1']
# #             about.story_image = image_file
# #         about.our_values= request.POST['our_values']
# #         about.our_mission= request.POST['our_mission']
# #         if 'mission_image' in request.FILES:
# #             image_file = request.FILES['image2']
# #             about.mission_image = image_file
# #         about.our_team= request.POST['our_team']

# #         about.save()
# #         messages.info(request,'Update successfully !')
# #         return redirect('dashboard:about')
# #     return redirect('dashboard:about')

# from django.http import JsonResponse

# @login_required
# def add_edit_news(request, id=None):
#     user = request.user
#     allcategorie = MainCategorie.objects.all()
#     news_instance = None
    
#     if id:
#         news_instance = get_object_or_404(News, id=id)

#     if request.method == "POST":
#         if news_instance:
#             form = NewsForm(request.POST, request.FILES, instance=news_instance)
#         else:
#             form = NewsForm(request.POST, request.FILES)

#         if form.is_valid():
#             new_news = form.save(commit=False)
#             new_news.save()
#             if news_instance:
#                 messages.success(request, 'News updated successfully!')
#                 return redirect('dashboard:update_news', id=news_instance.id)
#             else:
#                 messages.success(request, 'News added successfully!')
#                 return redirect('dashboard:create_news')
#         else:
#             messages.error(request, 'form is not valid. please check the form again')
#     else:
#         if news_instance:
#             form = NewsForm(instance=news_instance)
#         else:
#             form = NewsForm()
    
#     return render(request, 'app2/update_news.html', {'allcategorie': allcategorie, 'user': user, 'form': form, 'news_instance': news_instance})

# # def add_edit_news(request, id=None):
# #     instance = None
# #     try:
# #         if id:
# #             instance = News.objects.get(pk=id)
# #     except News.DoesNotExist:
# #         instance = None

# #     main_categories = MainCategorie.objects.all()  # Retrieve all main categories

# #     if request.method == 'POST':
# #         form = NewsForm(request.POST, request.FILES, instance=instance)
# #         if form.is_valid():
# #             form.save()
# #             if instance:  # Edit operation
# #                 messages.success(request, 'News edited successfully.')
# #                 return redirect('dashboard:edit_News', id=instance.id)
# #             else:  # Add operation
# #                 messages.success(request, 'News added successfully.')
# #                 return redirect('dashboard:add_News')
# #         else:
# #             messages.warning(request, 'Form is not valid. Please correct the errors.')
# #     else:
# #         form = NewsForm(instance=instance)

# #     context = {'form': form, 'news_instance': instance, 'main_categories': main_categories}
# #     return render(request, 'app2/update_news.html', context)


# # @login_required
# # def createNews(request):
# #     allcategorie = MainCategorie.objects.all()
# #     user = request.user
# #     if request.method == "POST":
# #         form = NewsForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             new_news = form.save(commit=False)
# #             new_news.save()
# #             messages.success(request, 'News added successfully!')
# #             return redirect('dashboard:createnews')
# #         else:
# #             messages.error(request, 'Form is not valid. Please check the input data.')
# #     else:
# #         form = NewsForm()
# #     return render(request, 'app2/create_news.html', {'allcategorie': allcategorie, 'user': user, 'form': form})

# # @login_required
# # def updateNews(request, id):
# #     news_instance = get_object_or_404(News, id=id)
# #     allcategorie = MainCategorie.objects.all()
# #     user = request.user
# #     if request.method == "POST":
# #         form = NewsForm(request.POST, request.FILES, instance=news_instance)
# #         if form.is_valid():
# #             form.save()
# #             messages.success(request, 'News updated successfully!')
# #             # return redirect('dashboard:update_news', news_instance.id)
# #         else:
# #             messages.error(request, form.errors)
# #     else:
# #         form = NewsForm(instance=news_instance)
# #     return render(request, 'app2/update_news.html', {'allcategorie': allcategorie, 'user': user, 'form': form, 'news_instance': news_instance})

# from django.http import JsonResponse
# from app.models import SubCategorie

# def get_subcategories(request):
#     main_category_id = request.GET.get('main_category_id')
#     subcategories = SubCategorie.objects.filter(maincategorie_id=main_category_id).values('id', 'subcategorie_name')
#     return JsonResponse(list(subcategories), safe=False)


# from django.forms import inlineformset_factory

# # def create_or_edit_feature(request, feature_id=None):
# #     if feature_id:
# #         feature_instance = get_object_or_404(Feature, id=feature_id)
# #     else:
# #         feature_instance = Feature.objects.create()

# #     ImageFormSet = inlineformset_factory(Feature, Image, form=ImageForm, extra=1)

# #     if request.method == 'POST':
# #         feature_form = FeatureForm(request.POST, instance=feature_instance)
# #         formset = ImageFormSet(request.POST, request.FILES, instance=feature_instance)

# #         if feature_form.is_valid() and formset.is_valid():
# #             feature_form.save()
# #             formset.save()
# #             messages.success(request, 'Feature saved successfully.')
# #             return redirect('dashboard:edit_feature', feature_id=feature_instance.id)
# #         else:
# #             messages.warning(request, 'Please correct the errors in the form.')
# #     else:
# #         feature_form = FeatureForm(instance=feature_instance)
# #         formset = ImageFormSet(instance=feature_instance)

# #     context = {
# #         'feature_form': feature_form,
# #         'formset': formset,
# #         'is_inline_formset_used': True,
# #     }

# #     return render(request, 'app2/create_feature.html', context)




# def create_or_edit_feature(request, feature_id=None):
#     if feature_id:
#         feature_instance = get_object_or_404(Feature, id=feature_id)
#     else:
#         feature_instance = Feature()

#     if request.method == 'POST':
#         feature_form = FeatureForm(request.POST, instance=feature_instance)
#         formset = ImageFormSet(request.POST, request.FILES, instance=feature_instance)

#         if feature_form.is_valid() and formset.is_valid():
#             feature_instance = feature_form.save(commit=False)
#             feature_instance.save()

#             formset.instance = feature_instance
#             formset.save()

#             messages.success(request, 'Feature successfully Created.')
#             return redirect('dashboard:edit_feature', feature_id=feature_instance.id)
         
#     else:
#         feature_form = FeatureForm(instance=feature_instance)
#         formset = ImageFormSet(instance=feature_instance)

#     context = {
#         'feature_form': feature_form,
#         'formset': formset,
#     }

#     return render(request, 'app2/create_feature.html', context)


# @login_required
# def add_edit_Video(request, id=None):
#     instance = None
#     try:
#         if id:
#             instance = Video.objects.get(pk=id)
#     except Exception as e:
#         messages.warning(request, 'An error occurred while retrieving the Video.')
#         return redirect('dashboard:add_Video')

#     if request.method == 'POST':
#         form = VideoForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'Video edited successfully.')
#                 return redirect('dashboard:edit_Video', id=instance.id)  # Redirect to the edited Video's details page
#             else:  # Add operation
#                 messages.success(request, 'Video added successfully.')
#                 return redirect('dashboard:add_Video')  # Redirect to the page for adding new Videos
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = VideoForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/create_newsVideo.html', context)

# @login_required
# def Videos(request):
#     Videos=Video.objects.all()
#     p=Paginator(Videos,10)
#     page_number= request.GET.get('page')
#     Videos=p.get_page(page_number)
#     return render(request, 'app2/newsVideo.html',{'details':Videos})

# @login_required
# def deleteVideo(request, id):
#     record = get_object_or_404(Video, id=id)

#     if request.method == 'POST':
#         record.delete()
#         return redirect('dashboard:Video')  # Redirect to a list view after deletion
#     else:
#         return render(request, 'app2/newsVideo.html', {'details': record})



# @login_required
# def Features(request):
#     Features=Feature.objects.all()
#     p=Paginator(Features,10)
#     page_number= request.GET.get('page')
#     Features=p.get_page(page_number)
#     return render(request, 'app2/feature.html',{'details':Features})

# @login_required
# def deletefeature(request, id):
#     record = get_object_or_404(Feature, id=id)

#     if request.method == 'POST':
#         record.delete()
#         return redirect('dashboard:feature')  # Redirect to a list view after deletion
#     else:
#         return render(request, 'app2/feature.html', {'details': record})
        
        
        


# # @user_role_required('admin')
# def add_edit_Tag(request, id=None):
#     instance = None
#     try:
#         if id:
#             instance = Tag.objects.get(pk=id)
#     except Exception as e:
#         messages.warning(request, 'An error occurred while retrieving the Tag.')
#         return redirect('dashboard:add_Tag')

#     if request.method == 'POST':
#         form = TagForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'Tag edited successfully.')
#                 return redirect('dashboard:edit_Tag', id=instance.id)  # Redirect to the edited Tag's details page
#             else:  # Add operation
#                 messages.success(request, 'Tag added successfully.')
#                 return redirect('dashboard:add_Tag')  # Redirect to the page for adding new Tags
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = TagForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     return render(request, 'app2/create_Tag.html', context)

# # @user_role_required('admin')
# def Tags(request):
#     Tags=Tag.objects.all()
#     p=Paginator(Tags,4)
#     page_number= request.GET.get('page')
#     Tags=p.get_page(page_number)
#     return render(request, 'app2/Tag.html',{'details':Tags})


# # @user_role_required('admin')
# def deleteTag(request, id):
#     record = Tag.objects.get(pk=id)
#     if request.method == 'POST':
#         record.delete()
#         messages.success(request,'Sub Categorie Deleted Successfully !')
#         return redirect('dashboard:Tag')  # Redirect to a list view after deletion
#     else:
#         return render(request, 'app2/Tag.html', {'details': record})
    
    
    


# # 