from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoin(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2023,sal__gt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Sales')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True,deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=2000,deptno=20)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename='Smith')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Accounting')
    
    
    # EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoin.html',d)