from datetime import date
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Userspentonprojects, Userspent, Projectspent
from .forms import UserDetailSelect, UserSpentOnProjectForm, UserSpentForm, ProjectSpentForm
import calendar

def index(request):
    return render(request, 'trackApp/index.html')

def track1(request):
    year = int(request.COOKIES.get('year', str(date.today().year)))
    month = int(request.COOKIES.get('month', str(date.today().month - 1)))
    name = request.COOKIES.get('name', '')
    project = request.COOKIES.get('project', '')
    if month == 0:
        month = 12

    sql_query = """select p.name project,
            p.id projectid,
            i.title issue,
            i.id issueid,
            u.id userid,
            u.name, 
            replace(ROUND(t.time_spent/3600.0, 1)::text, '.', ',') as spent,
            TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy HH24:MI:SS') date_spent, substring(n.note for 300) note
            from issues i
            left join projects p on p.id = i.project_id
            left join timelogs t on t.issue_id = i.id
            left join users u on u.id = t.user_id
            left join notes n on n.id = t.note_id"""

    if(request.method=="GET"):
        form = UserSpentOnProjectForm(request.GET)

        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            name = form.cleaned_data['name']
            project = form.cleaned_data['project']


    user_spent_on_project = Userspentonprojects.objects.raw(sql_query +
        ''' where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59'
            order by 8''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1]]
    )
    if name is not "" and project is "":
        name = '%' + name + '%'

        user_spent_on_project = Userspentonprojects.objects.raw(sql_query +
            ''' where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' and u.name LIKE %s
                order by 7, 1, 3''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], name]
        )
    if project is not "" and name is "":
        project = '%' + project + '%'
        user_spent_on_project = Userspentonprojects.objects.raw(sql_query +
            ''' where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' and p.name LIKE %s
                order by 7, 1, 3''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], project]
        )
    if project and name is not "":
        project = '%' + project + '%'
        name = '%' + name + '%'
        user_spent_on_project = Userspentonprojects.objects.raw(sql_query +
            ''' where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' and p.name LIKE %s and u.name LIKE %s
                order by 7, 1, 3''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], project, name]
        )

    form = UserSpentOnProjectForm(initial={
        'year': year,
        'month': month,
        'name': name.strip("%"),
        'project': project.strip("%")
    })

    spent_sum = 0
    records_sum = 0
    for record in user_spent_on_project:
        records_sum = records_sum + 1
        spent_sum = spent_sum + float(record.spent.replace(",", "."))
    print(records_sum)

    context = {
        'user_spent_on_project' : user_spent_on_project,
        'form' : form,
        'name': name.strip("%"),
        'project': project.strip("%"),
        'month': month,
        'year': year,
        'spent_sum' : round(spent_sum, 2)
    }

    response = render(request, 'trackApp/track1.html', context=context)
    response.set_cookie('year', year)
    response.set_cookie('month', month)
    response.set_cookie('project', project.strip("%"))
    response.set_cookie('name', name.strip("%"))
    return response

def track2(request):
    year = int(request.COOKIES.get('year', str(date.today().year)))
    month = int(request.COOKIES.get('month', str(date.today().month - 1)))
    name = request.COOKIES.get('name', '')
    if month == 0:
        month = 12

    sql_query = """select u.name,
            u.id userid,
            ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
            replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
            from issues i 
            left join projects p on p.id = i.project_id  
            left join timelogs t on t.issue_id = i.id    
            left join users u on u.id = t.user_id"""

    if (request.method == "GET"):
        form = UserSpentForm(request.GET)

        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            name = form.cleaned_data['name']

    user_spent = Userspent.objects.raw(sql_query +
        ''' where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' 
            group by 1, 2
            order by 3 desc''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1]]
        )
    if name is not "":
        name = '%' + name + '%'

        user_spent = Userspent.objects.raw( sql_query +
            ''' where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' and u.name LIKE %s
                group by 1, 2
                order by 3 desc''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], name]
        )

    form = UserSpentForm(initial={
        'year': year,
        'month': month,
        'name': name.strip("%")
    })

    spent_sum = 0
    for record in user_spent:
        spent_sum = spent_sum + float(record.spent)

    context = {
        'user_spent': user_spent,
        'form': form,
        'name': name.strip("%"),
        'month': month,
        'year': year,
        'spent_sum': round(spent_sum, 2)
    }

    response = render(request, 'trackApp/track2.html', context=context)
    response.set_cookie('year', year)
    response.set_cookie('month', month)
    response.set_cookie('name', name.strip("%"))
    return response

def track3(request):
    year = int(request.COOKIES.get('year', str(date.today().year)))
    month = int(request.COOKIES.get('month', str(date.today().month - 1)))
    name = request.COOKIES.get('project', '')
    if month == 0:
        month = 12

    sql_query = """select p.name,
            p.id projectid,
            p.description, 
            u.email creator, 
            ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
            replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
            from issues i 
            left join projects p on p.id = i.project_id 
            left join users u on u.id = p.creator_id  
            left join timelogs t on t.issue_id = i.id"""

    if (request.method == "GET"):
        form = UserSpentForm(request.GET)

        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            name = form.cleaned_data['name']

    project_spent = Projectspent.objects.raw(sql_query +
        ''' where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59'
            group by 1,2,3,4
            order by 4 desc''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1]]
        )
    if name is not "":
        name = '%' + name + '%'

        project_spent = Projectspent.objects.raw(sql_query +
            ''' where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' and p.name LIKE %s
                group by 1,2,3,4
                order by 4 desc''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], name]
        )

    form = ProjectSpentForm(initial={
        'year': year,
        'month': month,
        'name': name.strip("%")
    })

    spent_sum = 0
    for record in project_spent:
        spent_sum = spent_sum + float(record.spent)

    context = {
        'project_spent': project_spent,
        'form': form,
        'name': name.strip("%"),
        'year': year,
        'month': month,
        'spent_sum': round(spent_sum, 2)
    }

    response = render(request, 'trackApp/track3.html', context=context)
    response.set_cookie('year', year)
    response.set_cookie('month', month)
    response.set_cookie('project', name.strip("%"))
    return response
    

def track4(request):
    year = int(request.COOKIES.get('year', str(date.today().year)))
    month = int(request.COOKIES.get('month', str(date.today().month - 1)))
    name = request.COOKIES.get('name', '')
    if month == 0:
        month = 12
    sql_query = """select u.name,
        u.id userid,
        ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
        replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
        from issues i 
        left join projects p on p.id = i.project_id  
        left join timelogs t on t.issue_id = i.id    
        left join users u on u.id = t.user_id"""

    if (request.method == "GET"):
        form = UserDetailSelect(request.GET)

        if form.is_valid():
            name = form.cleaned_data['name']
    
    form = UserDetailSelect(initial={
        'name': name.strip("%")
    })

    context = {
        'name': name.strip("%"),
        'form': form
    }
    
    response = render(request, 'trackApp/track4.html', context=context)
    return response