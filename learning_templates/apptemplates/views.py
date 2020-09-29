from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'Hello world','number':100}
    return render(request,'apptemplates/index.html',context=context_dict)

def other(request):
    return render(request,'apptemplates/other.html')

def relative(request):
    return render(request,'apptemplates/relative_url_templates.html')