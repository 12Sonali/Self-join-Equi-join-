from django.shortcuts import render
from app.models import *
from django.db.models import Q
# Create your views here.
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2023)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=1500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__lt=1500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=20)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='CHICAGO')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)  


def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lte=2000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=2850)
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__year=2024)
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(job='PRESIDENT')
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='SCOTT')
    empmgrobjects=Emp.objects.select_related('mgr').filter(empno=7902)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr=7566)
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__year=2024,sal__gt=1500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm=0)
    empmgrobjects=Emp.objects.select_related('mgr').filter (mgr__isnull=False)
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno=30)

    d={'EMPLOYEEMANAGEROBJECT':empmgrobjects}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SCOTT')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='MILLER')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='OPERATIONS') | Q(deptno__dlocation='DALLAS'))
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr=7698)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=10)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2023,sal__gt=2300)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__ename='WARD') | Q(deptno__dname='RESEARCH'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__deptno__in=(10,20))  |  Q(deptno__in=(10,20)))
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='K')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno__in=(10,20))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='W')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(job='CLERK')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__lte=1600)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation__startswith='C')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename__endswith='t')   |  Q(deptno__dname='ACCOUNTING'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno__dlocation__contains='A')
    emd=Emp.objects.select_related('deptno','mgr').filter(job='PRESIDENT')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__ename='SCOTT') | Q(deptno__dname='RESEARCH'))
    emd=Emp.objects.select_related('deptno','mgr').filter(comm=300)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm=0)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal=2850)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='E')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename__endswith='E')   |  Q(deptno__dname='SALES'))
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lt=2000)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__contains='A')
    emd=Emp.objects.select_related('deptno','mgr').filter(job__startswith='C')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='S')   | Q(ename__endswith='K'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='M')   | Q(ename__endswith='S'))
    
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)

def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=SalGrade.objects.all()
    # Retrieving the data of employess who belongs to grade 4
    #SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]

    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    # Retrieving the data of employess who belongs to grade 3,4
    SO=SalGrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))


    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)



                                                  