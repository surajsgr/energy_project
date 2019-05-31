# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from projects.models import Project
from .form import  EnergyForm


def team_info(request):

    return render(request,'projects/team.html')

def project_index(request):
    
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request,pk=1):

    project = Project.objects.get(pk=1)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html',context)


def energy(request,pk=1):

    project = Project.objects.get(pk=1)

    if request.method == 'POST':
        form = EnergyForm(request.POST)
        if form.is_valid():
            
            Month = float(form.cleaned_data.get('Month'))
            Day=float(form.cleaned_data.get('Day'))
            Hour=float(form.cleaned_data.get('Hour'))
            Age_lt_5=float(form.cleaned_data.get('Age_lt_5'))
            Age_range_5_to_18=float(form.cleaned_data.get('Age_range_5_to_18'))
            Age_range_18_to_25=float(form.cleaned_data.get('Age_range_18_to_25'))
            Age_range_25_to_65=float(form.cleaned_data.get('Age_range_25_to_65'))
            Age_gt_65=float(form.cleaned_data.get('Age_gt_65'))
            Days_of_week=float(form.cleaned_data.get('Days_of_week'))
            School_Day=float(form.cleaned_data.get('School_Day'))
            Cloud_Cover_Fraction=float(form.cleaned_data.get('Cloud_Cover_Fraction'))
            Dew_point=float(form.cleaned_data.get('Dew_point'))
            Humidity_Fraction=float(form.cleaned_data.get('Humidity_Fraction'))
            Precipitable_Water=float(form.cleaned_data.get('Precipitable_Water'))
            Temperature=float(form.cleaned_data.get('Temperature'))
            Visibility=float(form.cleaned_data.get('Visibility'))
            Sector_FOOD_SERVICE=float(form.cleaned_data.get('Sector_FOOD_SERVICE'))
            Sector_Grocery=float(form.cleaned_data.get('Sector_Grocery'))
            Sector_K12_school=float(form.cleaned_data.get('Sector_K12_school'))
            Sector_Lodging=float(form.cleaned_data.get('Sector_Lodging'))
            Sector_office=float(form.cleaned_data.get('Sector_office'))
            Sector_residental=float(form.cleaned_data.get('Sector_residental'))
            Sector_STAND_ALONE_RETAIL=float(form.cleaned_data.get('Sector_STAND_ALONE_RETAIL'))
            
            print(Sector_Lodging)
            print(Sector_residental)

            Y = (1.226*(2.72**-5 )* Month) + (-7.214*(2.72**-7) * Day) + (4.384*(2.72**-5) * Hour) + (-0.0003 * Age_lt_5 ) + (2.167*(2.72**-6) * Age_range_5_to_18)
                                                                                                        
            +(0.0005 * Age_range_18_to_25) + (-0.0004 * Age_range_25_to_65) + (0.0002 * Age_gt_65 ) + (3.24*(2.72**-5) * Days_of_week)
                                                                                                       
            +(0.0002 * School_Day) + (0.0002 * Cloud_Cover_Fraction) + (-5.1*(2.72**-6) *Dew_point)+(-0.0024 * Humidity_Fraction)
                                                                                       
            + (3.058*(2.72**-5) * Precipitable_Water) + (-2.602*(2.72**-6) * Temperature)+(-3.18*(2.72**-5) * Visibility)+ (0.0022 * Sector_FOOD_SERVICE)
            
            +(0.0028 *Sector_Grocery)+(-2.504*(2.72**-5) * Sector_K12_school)+ (0.0002 *Sector_Lodging)+(-2.041*(2.72**-5) * Sector_office) + (-4.458*(2.72**-6) * Sector_residental)
            
            +(-0.0034 * Sector_STAND_ALONE_RETAIL) + (0.0019)
            context={
                'value':Y,
                'project':project
            }
            
            print(Y)
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request,'projects/result.html',context)
        # else:
        #
        #     return HttpResponse("<h1>Please check and enter the value in given range</h1>")
    else:
        form = EnergyForm()
    return render(request, 'projects/energy.html', {'form': form,'project':project})


def visualisation(request,pk=1):

    project = Project.objects.get(pk=1)
    context = {
        'project': project
    }
    
    return render(request,'projects/visualisation.html',context)

