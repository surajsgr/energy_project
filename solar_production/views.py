from django.shortcuts import render,HttpResponse
from .form import SolarForm
from projects.models import  Project

'''
Y = (1005.0092 * Solar Elevation) + ( -1.643e+04 * Cloud_Cover_Fraction) + (-1662.2771 * Dew_Point) + (-1.963e+04 * Humidity_Fraction) +
 ( -754.3373 *  Precipitation) + ( 47.0157 * Pressure) + (1044.2367 * Temperature) + (149.8066 * Visibility) + ( -156.0822 * Wind_Speed) 

'''

def solar_model(request,pk=2):
    project = Project.objects.get(pk=2)




    if request.method=='POST':
        form=SolarForm(request.POST)

        if form.is_valid():
            solar_Elevation=float(form.cleaned_data.get('Solar_Elevation'))
            print(solar_Elevation)
            Cloud_Cover=float(form.cleaned_data.get('Cloud_Cover_Fraction'))
            Dew_Point=float(form.cleaned_data.get('Dew_Point'))
            print(Dew_Point)
            Humidity=float(form.cleaned_data.get('Humidity_Fraction'))
            Precipitation=float(form.cleaned_data.get('Precipitation'))
            Pressure=float(form.cleaned_data.get('Pressure'))
            Temperature=float(form.cleaned_data.get('Temperature'))
            Visibility=float(form.cleaned_data.get('Visibility'))
            Wind_Speed=float(form.cleaned_data.get('WindSpeed'))

            print(Wind_Speed)

            Y = (1005.0092 * solar_Elevation) + ((-1.643*2.72**4)* Cloud_Cover) + (-1662.2771 * Dew_Point) + ((-1.963*2.72**4) * Humidity)

            + (-754.3373 * Precipitation) + (47.0157 * Pressure) + (1044.2367 * Temperature) + (149.8066 * Visibility) + ( -156.0822 * Wind_Speed)
            print(Y)
            context = {
                'value': Y,
                'project': project
            }

            return render(request, 'solar/result.html', context)
        else:
            return HttpResponse("<h1>Please check and enter the value in given range</h1>")
    else:


        form = SolarForm()
        return render(request, 'solar/model.html', {'form': form,'project':project})

def visualisation(request,pk=2):
    project = Project.objects.get(pk=2)
    context = {

        'project': project
    }

    return render(request, 'solar/visualisation.html',context)

def solar_detail(request):

    project = Project.objects.get(pk=2)

    context={

        'project':project
    }



    return render(request, 'solar/solar_detail.html',context)

def project_index(request):

    projects = Project.objects.all()

    context = {
            'projects': projects
        }
    return render(request, 'projects/project_index.html', context)





        # Create your views here.
