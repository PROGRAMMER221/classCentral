from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.HomeView, name="home"),
    url(r'^login/$', views.LoginView, name="login"),
    url(r'^signup/$', views.SignupView, name="login"),
    url(r'^subjects/$', views.SubjectsView, name="login"),
    url(r'^universities/$', views.universitiesView, name="login"),

    url(r'^institution/amazon/$', views.InstitutionViewAmazon, name="login"),
    url(r'^institution/british-council/$', views.InstitutionViewBritishCouncil, name="login"),
    url(r'^institution/google/$', views.InstitutionViewgoogle, name="login"),
    url(r'^institution/ibm/$', views.InstitutionViewibm, name="login"),
    url(r'^institution/kaggle/$', views.InstitutionViewkaggle, name="login"),
    url(r'^institution/linuxfoundation/$', views.InstitutionViewlinuxfoundation, name="login"),
    url(r'^institution/microsoft/$', views.InstitutionViewmicrosoft, name="login"),
    url(r'^institution/learn/$', views.InstitutionViewlearn, name="login"),
    url(r'^institution/oakley/$', views.InstitutionViewoakley, name="login"),
    url(r'^institution/salesforce/$', views.InstitutionViewsalesforce, name="login"),
    url(r'^institution/smithsonian/$', views.InstitutionViewsmithsonian, name="login"),
    url(r'^institution/united-nations/$', views.InstitutionViewnations, name="login"),
    url(r'^institutions/$', views.InstitutionsView, name="login"),

    url(r'^university/harvard/$', views.UniversitiesHarvard, name="login"),
    url(r'^university/stanford/$', views.Universitiesstanford, name="login"),
    url(r'^university/mit/$', views.Universitiesmit, name="login"),
    url(r'^university/iitk/$', views.Universitiesiitk, name="login"),
    url(r'^university/rice/$', views.Universitiesrice, name="login"),
    url(r'^university/iitm/$', views.Universitiesiitm, name="login"),
    url(r'^university/columbia/$', views.Universitiescolumbia, name="login"),
    url(r'^university/cornell/$', views.Universitiescornell, name="login"),
    url(r'^university/edinburgh/$', views.Universitiesedinburgh, name="login"),
    url(r'^university/purdue/$', views.Universitiespurdue, name="login"),
    url(r'^university/duke/$', views.Universitiesduke, name="login"),
    url(r'^university/penn/$', views.Universitiespenn, name="login"),
    url(r'^university/umich/$', views.Universitiesumich, name="login"),

    url(r'^providers/$', views.Providers, name="login"),
    url(r'^provider/coursera/$', views.ProvidersCoursera, name="login"),
    url(r'^provider/edx/$', views.ProvidersEDX, name="login"),
    url(r'^provider/futurelearn/$', views.ProvidersfutureLean, name="login"),
    url(r'^provider/udemy/$', views.ProvidersUdemy, name="login"),
    url(r'^provider/swayam/$', views.Providersswayam, name="login"),
    url(r'^provider/linkedin-learning/$', views.ProvidersLinkedin_learning, name="login"),
    url(r'^provider/skillshare/$', views.ProviderSkillShare, name="login"),


    

]