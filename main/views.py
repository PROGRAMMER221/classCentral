from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, 'index.html')

def LoginView(request):
    return render(request, 'login.html')

def SignupView(request):
    return render(request, 'signup.html')

def SubjectsView(request):
    return render(request, 'subjects.html')

def universitiesView(request):
    return render(request, 'universities.html')

def InstitutionViewAmazon(request):
    return render(request, 'institution/amazon.html')
    
def InstitutionViewBritishCouncil(request):
    return render(request, 'institution/british-council.html')

def InstitutionViewgoogle(request):
    return render(request, 'institution/google.html')

def InstitutionViewibm(request):
    return render(request, 'institution/ibm.html')

def InstitutionViewkaggle(request):
    return render(request, 'institution/kaggle.html')

def InstitutionViewlinuxfoundation(request):
    return render(request, 'institution/linuxfoundation.html')

def InstitutionViewmicrosoft(request):
    return render(request, 'institution/microsoft.html')

def InstitutionViewlearn(request):
    return render(request, 'institution/minna-learn.html')

def InstitutionViewoakley(request):
    return render(request, 'institution/oakley.html')

def InstitutionViewsalesforce(request):
    return render(request, 'institution/salesforce.html')

def InstitutionViewsmithsonian(request):
    return render(request, 'institution/smithsonian.html')

def InstitutionViewnations(request):
    return render(request, 'institution/united-nations.html')

def InstitutionsView(request):
    return render(request, "institutions.html")

def UniversitiesHarvard(request):
    return render(request, 'university/harvard.html')

def Universitiesstanford(request):
    return render(request, 'university/stanford.html')

def Universitiesmit(request):
    return render(request, 'university/mit.html')

def Universitiesiitk(request):
    return render(request, 'university/iitk.html')

def Universitiesrice(request):
    return render(request, 'university/rice.html')

def Universitiesiitm(request):
    return render(request, 'university/iitm.html')

def Universitiescolumbia(request):
    return render(request, 'university/columbia.html')

def Universitiescornell(request):
    return render(request, 'university/cornell.html')

def Universitiesedinburgh(request):
    return render(request, 'university/edinburgh.html')

def Universitiespurdue(request):
    return render(request, 'university/purdue.html')

def Universitiesduke(request):
    return render(request, 'university/duke.html')

def Universitiespenn(request):
    return render(request, 'university/penn.html')

def Universitiesumich(request):
    return render(request, 'university/umich.html')