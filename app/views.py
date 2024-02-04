from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q


# -----------------equi join----------------
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
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoin.html',d)

# -------------------self join -------------------
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


# -------------------------3 table joins--------------------------
def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Blark')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='Jones')
    emd=Emp.objects.select_related('deptno','mgr').filter( Q(deptno__dname='Research') | Q(mgr__ename='Allen'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Ford',deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='Sales') | Q(mgr__ename__startswith='K'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='Sales') | Q(mgr__sal__gt=1000))
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='Persident',mgr__job__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=10,mgr__job__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__job__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='Blark',mgr__hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=20,deptno__dlocation='Dallas')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024) | Q(deptno__dname='Accounting'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gte=3000)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='k')
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__day=8,deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024) | Q(deptno__dname='Dallas'))
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__day=8,deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='Salesman',mgr__comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='Jones',deptno__dlocation='Dallas')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__job__isnull=True,deptno=10)
    emd=Emp.objects.select_related('deptno','mgr').all()[1:4:]
    emd=Emp.objects.select_related('deptno','mgr').order_by('ename')
    emd=Emp.objects.select_related('deptno','mgr').order_by('-ename') 
    emd=Emp.objects.select_related('deptno','mgr').order_by('-mgr__ename')
    emd=Emp.objects.select_related('deptno','mgr').all()[:4:]
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2023) | Q(sal__gt=2000))
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=3000)
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__day=17,deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='Ford',mgr__hiredate__year=2023)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=30,deptno__dlocation='Chicago')
    emd=Emp.objects.select_related('deptno','mgr').order_by('deptno__dlocation') 



    



    # emd=Emp.objects.select_related('deptno','mgr').all()
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)