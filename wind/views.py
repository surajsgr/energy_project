from django.shortcuts import render,HttpResponse
from .form import WindForm
from projects.models import Project




def wind_model(request,pk=3):


    project = Project.objects.get(pk=3)



    if request.method=='POST':


        form=WindForm(request.POST)

        if form.is_valid():

            WindSpeed=float(form.cleaned_data.get('WindSpeed'))

            Y = 0.00500401*(WindSpeed) + 0.00559301

            context={

                'value':Y,
                'project': project
            }

            return render(request,'wind/wind_result.html',context)
        else:
            return HttpResponse("<h1>Please enter the value within given range</h1>")
    else:
        form=WindForm()

        return render(request,'wind/wind_model.html',{'form':form,'project':project})




def wind_visualisation(request,pk=3):
    project = Project.objects.get(pk=3)

    context = {

        'project': project
    }

    return render(request, 'wind/wind_visualisation.html',context)


def wind_detail(request,pk=3):

    project = Project.objects.get(pk=3)

    context = {

        'project': project
    }

    return render(request, 'wind/wind_detail.html', context)

# Create your views here.
