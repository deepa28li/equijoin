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
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__startswith='j')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Accounting')
    # EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoin.html',d)


def selfjoin(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=2000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='Smith')
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True,deptno=10)
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__year=2023,sal__gt=2000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__job='Analyst')
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='Ford',mgr__sal__gt=1000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(job='Persident',mgr__job__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='Blark',mgr__hiredate__year=2024)
    empmgrobjects=Emp.objects.select_related('mgr').all()[1:4:]
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__day=8,deptno=20)
    empmgrobjects=Emp.objects.select_related('mgr').filter(job='Salesman',mgr__comm__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True,deptno=10)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='j')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lte=1500)

    # empmgrobjects=Emp.objects.select_related('mgr').all()

    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoin.html',d)