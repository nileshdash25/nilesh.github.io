from django.shortcuts import render
from Testapp.models import StudentInfo
from Testapp.Form import StudentForm
# Create your views here.
def Temp(req):
   s=StudentInfo.objects.all()
   my_dict={'student':s}
   return render (req,'FetchDatabase.html',context=my_dict)
def LogiN(req):
   fm=StudentForm()
   if req.method=='POST':
      fm=StudentForm(req.POST) 
      if fm.is_valid():
        fm.save(commit=True)
        print('Insert Data in Database Successfully ') 
   return render (req,'Register.html',{'forms':fm})

