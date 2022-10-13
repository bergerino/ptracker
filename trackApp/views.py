from datetime import date
from multiprocessing import context
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Daytotaluser, Issueperdayuser, Issuetotaluser, Userspentonprojects, Userspent, Projectspent
from .forms import UserDetailSelect, UserSpentOnProjectForm, UserSpentForm, ProjectSpentForm
import calendar
from collections import Counter

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
    for record in user_spent_on_project:
        spent_sum = spent_sum + float(record.spent.replace(",", "."))

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

    sql_query = """select
            u.id as user_id,
            u.name as name_id,
            SUM(ROUND(t.time_spent/3600.0, 1)) as all_spent,
            SUM((CASE WHEN 0<(select count(*) from label_links ll left join labels l on l.id=ll.label_id  where ll.target_type='Issue' and ll.target_id = i.id and l.title like 'Type::Request') THEN 1 ELSE 0 END)*ROUND(t.time_spent/3600.0, 1) )
             AS request,
            SUM((CASE WHEN 0<(select count(*) from label_links ll left join labels l on l.id=ll.label_id  where ll.target_type='Issue' and ll.target_id = i.id and l.title like 'Type::Bug') THEN 1 ELSE 0 END)*ROUND(t.time_spent/3600.0, 1) )
             AS bug,
            SUM((CASE WHEN 0<(select count(*) from label_links ll left join labels l on l.id=ll.label_id  where ll.target_type='Issue' and ll.target_id = i.id and l.title like 'Type::Operational') THEN 1 ELSE 0 END)*ROUND(t.time_spent/3600.0, 1) )
             AS operational,
            SUM((CASE WHEN 0<(select count(*) from label_links ll left join labels l on l.id=ll.label_id  where ll.target_type='Issue' and ll.target_id = i.id and l.title like 'Type::Meeting') THEN 1 ELSE 0 END)*ROUND(t.time_spent/3600.0, 1) )
             AS meeting,
            SUM((CASE WHEN 0<(select count(*) from label_links ll left join labels l on l.id=ll.label_id  where ll.target_type='Issue' and ll.target_id = i.id and l.title like 'Type::Absence') THEN 1 ELSE 0 END)*ROUND(t.time_spent/3600.0, 1) )
             AS absence

            from timelogs t
            left join users u on u.id = t.user_id
            left join issues i on t.issue_id = i.id
            left join projects p on p.id = i.project_id"""

    if (request.method == "GET"):
        form = UserSpentForm(request.GET)

        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            name = form.cleaned_data['name']

    user_spent = Userspent.objects.raw(sql_query +
        ''' where (t.spent_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' 
            group by 1, 2
            order by 2 desc''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1]]
        )
    if name is not "":
        name = '%' + name + '%'

        user_spent = Userspent.objects.raw( sql_query +
            ''' where (t.spent_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' and u.name LIKE %s
                group by 1, 2
                order by 2 desc''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], name]
        )

    form = UserSpentForm(initial={
        'year': year,
        'month': month,
        'name': name.strip("%")
    })

    columns_sum = (0, 0, 0, 0, 0, 0)
    spent_sum = 0
    request_sum = 0
    bug_sum = 0
    operational_sum = 0
    meeting_sum = 0
    absence_sum = 0
    for record in user_spent:
        spent_sum = spent_sum + float(record.all_spent)
        request_sum = request_sum + float(record.request)
        bug_sum = bug_sum + float(record.bug)
        operational_sum = operational_sum + float(record.operational)
        meeting_sum = meeting_sum + float(record.meeting)
        absence_sum = absence_sum + float(record.absence)
    columns_sum = (round(spent_sum, 2), round(request_sum, 2), round(bug_sum, 2), round(operational_sum, 2), round(meeting_sum, 2), round(absence_sum, 2))

    context = {
        'user_spent': user_spent,
        'form': form,
        'name': name.strip("%"),
        'month': month,
        'year': year,
        'columns_sum': columns_sum
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
        ''' where (t.spent_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59'
            group by 1,2,3,4
            order by 4 desc''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1]]
        )
    if name is not "":
        name = '%' + name + '%'

        project_spent = Projectspent.objects.raw(sql_query +
            ''' where (t.spent_at  + interval '2h') between '%s-%s-01' and '%s-%s-%s 23:59:59' and p.name LIKE %s
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
    sql_query_ipdu = """select p.name project,
            p.id projectid,
            i.title issue,
            i.id issueid,
            u.id userid,
            u.name,
            SUM(ROUND(t.time_spent/3600.0, 1)) as spent,
            TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy') date_spent
            from issues i
            left join projects p on p.id = i.project_id
            left join timelogs t on t.issue_id = i.id
            left join users u on u.id = t.user_id
            left join notes n on n.id = t.note_id"""
    sql_query_itu = """select i.title issue,
            i.id issueid,
            p.name project,
            p.id projectid,
            u.id userid,
            u.name,
            SUM(ROUND(t.time_spent/3600.0, 1)) as spent
            from issues i
            left join projects p on p.id = i.project_id
            left join timelogs t on t.issue_id = i.id
            left join users u on u.id = t.user_id
            left join notes n on n.id = t.note_id"""
    sql_query_dtu = """select u.name,
            u.id userid,
            SUM(ROUND(t.time_spent/3600.0, 1)) as spent,
            TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy') date_spent
            from issues i
            left join projects p on p.id = i.project_id
            left join timelogs t on t.issue_id = i.id
            left join users u on u.id = t.user_id
            left join notes n on n.id = t.note_id"""

    if (request.method == "GET"):
        form = UserDetailSelect(request.GET)

        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']

    issue_per_day_user = ""
    day_total_user = ""
    issue_total_user = ""
    if name is not "":
        name = '%' + name + '%'

        issue_per_day_user = Issueperdayuser.objects.raw(sql_query_ipdu +
            ''' where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-%s' and u.name LIKE %s
                group by 2, 4, 5, date_spent''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], name]
        )
        day_total_user = Daytotaluser.objects.raw(sql_query_dtu +
            ''' where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-%s' and u.name LIKE %s
                group by u.id, date_spent''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], name]
        )
        issue_total_user = Issuetotaluser.objects.raw(sql_query_itu +
            ''' where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-%s' and u.name LIKE %s
                group by i.id, u.id, p.id;''', [year, month, year, month, calendar.monthrange(year=year, month=month)[1], name]
        )
    
    form = UserDetailSelect(initial={
        'year': year,
        'month': month,
        'name': name.strip("%"),
    })

    unique_projects = []
    unique_issues = []
    project_tuples = []
    project_total = 0
    issue_total = 0
    month_total = 0
    
    for record in issue_per_day_user:
        
        if record.project not in unique_projects:
            unique_projects.append(record.project)
        
        if (record.issue, record.project, issue_total) not in unique_issues:
            for record0 in issue_total_user:
                if record.issue == record0.issue:
                    issue_total = record0.spent
            unique_issues.append((record.issue, record.project, issue_total))
    
    for record in unique_projects:
        for record0 in issue_total_user:
            if record == record0.project:
                project_total += record0.spent
        project_tuples.append((record, Counter(elem[1] for elem in unique_issues)[record]+1, project_total))
        project_total = 0

    for record in issue_total_user:
        month_total += record.spent


    context = {
        'month_total': month_total,
        'issue_total_user': issue_total_user,
        'day_total_user': day_total_user,
        'issue_per_day_user': issue_per_day_user,
        'form' : form,
        'name': name.strip("%"),
        'month': month,
        'year': year,
        'project_tuples': project_tuples,
        'unique_issues': unique_issues,
        'month_range': calendar.monthrange(year=year, month=month)[1]
    }

    response = render(request, 'trackApp/track4.html', context=context)
    response.set_cookie('year', year)
    response.set_cookie('month', month)
    response.set_cookie('name', name.strip("%"))
    
    return response

def fungujes(request):
    response = HttpResponse('Ano, funguju')
    return response