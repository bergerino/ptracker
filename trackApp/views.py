from datetime import date
from django.shortcuts import render
from .models import Userspentonprojects, Userspent, Projectspent
from .forms import UserSpentOnProjectForm, UserSpentForm, ProjectSpentForm

def index(request):
    return render(request, 'trackApp/index.html')

def track1(request):
    year = date.today().year
    month = date.today().month - 1
    name = ""
    project = ""

    if(request.method=="GET"):
        form = UserSpentOnProjectForm(request.GET)

        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            name = form.cleaned_data['name']
            project = form.cleaned_data['project']


    user_spent_on_project = Userspentonprojects.objects.raw(
        '''select 1 as id,
            p.name project,
            i.title issue, 
            u.name, 
            replace(ROUND(t.time_spent/3600.0, 1)::text, '.', ',') as spent,
            TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy HH24:MI:SS') date_spent, substring(n.note for 300) note
            from issues i
            left join projects p on p.id = i.project_id
            left join timelogs t on t.issue_id = i.id
            left join users u on u.id = t.user_id
            left join notes n on n.id = t.note_id
            where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59'
            order by 5, 1, 2''', [year, month, year, month]
    )
    if name is not "" and project is "":
        name = '%' + name + '%'

        user_spent_on_project = Userspentonprojects.objects.raw(
            '''select 1 as id,
                p.name project,
                i.title issue, 
                u.name, 
                replace(ROUND(t.time_spent/3600.0, 1)::text, '.', ',') as spent,
                TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy HH24:MI:SS') date_spent, substring(n.note for 300) note
                from issues i
                left join projects p on p.id = i.project_id
                left join timelogs t on t.issue_id = i.id
                left join users u on u.id = t.user_id
                left join notes n on n.id = t.note_id
                where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59' and u.name LIKE %s
                order by 5, 1, 2''', [year, month, year, month, name]
        )
    if project is not "" and name is "":
        project = '%' + project + '%'
        user_spent_on_project = Userspentonprojects.objects.raw(
            '''select 1 as id,
                p.name project,
                i.title issue, 
                u.name, 
                replace(ROUND(t.time_spent/3600.0, 1)::text, '.', ',') as spent,
                TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy HH24:MI:SS') date_spent, substring(n.note for 300) note
                from issues i
                left join projects p on p.id = i.project_id
                left join timelogs t on t.issue_id = i.id
                left join users u on u.id = t.user_id
                left join notes n on n.id = t.note_id
                where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59' and p.name LIKE %s
                order by 5, 1, 2''', [year, month, year, month, project]
        )
    if project and name is not "":
        project = '%' + project + '%'
        name = '%' + name + '%'
        user_spent_on_project = Userspentonprojects.objects.raw(
            '''select 1 as id,
                p.name project,
                i.title issue, 
                u.name, 
                replace(ROUND(t.time_spent/3600.0, 1)::text, '.', ',') as spent,
                TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy HH24:MI:SS') date_spent, substring(n.note for 300) note
                from issues i
                left join projects p on p.id = i.project_id
                left join timelogs t on t.issue_id = i.id
                left join users u on u.id = t.user_id
                left join notes n on n.id = t.note_id
                where (t.spent_at + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59' and p.name LIKE %s and u.name LIKE %s
                order by 5, 1, 2''', [year, month, year, month, project, name]
        )

    form = UserSpentOnProjectForm(initial={
        'year': year,
        'month': month
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
        'name': name,
        'project': project,
        'month': month,
        'year': year,
        'spent_sum' : spent_sum
    }

    return render(request, 'trackApp/track1.html', context=context)

def track2(request):
    year = date.today().year
    month = date.today().month - 1
    name = ""

    if (request.method == "GET"):
        form = UserSpentForm(request.GET)

        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            name = form.cleaned_data['name']

    user_spent = Userspent.objects.raw(
        '''select 1 as id,
            u.name, 
            ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
            replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
            from issues i 
            left join projects p on p.id = i.project_id  
            left join timelogs t on t.issue_id = i.id    
            left join users u on u.id = t.user_id 
            where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59' 
            group by 2
            order by 3 desc''', [year, month, year, month]
        )
    if name is not "":
        name = '%' + name + '%'

        user_spent = Userspent.objects.raw(
            '''select 1 as id,
                u.name, 
                ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
                replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
                from issues i 
                left join projects p on p.id = i.project_id  
                left join timelogs t on t.issue_id = i.id    
                left join users u on u.id = t.user_id 
                where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59' and u.name LIKE %s
                group by 2
                order by 3 desc''', [year, month, year, month, name]
        )

    form = UserSpentForm(initial={
        'year': year,
        'month': month
    })

    spent_sum = 0
    for record in user_spent:
        spent_sum = spent_sum + float(record.spent)

    context = {
        'user_spent': user_spent,
        'form': form,
        'name': name,
        'month': month,
        'year': year,
        'spent_sum': spent_sum
    }

    return render(request, 'trackApp/track2.html', context=context)

def track3(request):
    year = date.today().year
    month = date.today().month - 1
    name = ""

    if (request.method == "GET"):
        form = UserSpentForm(request.GET)

        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            name = form.cleaned_data['name']

    project_spent = Projectspent.objects.raw(
        '''select 1 as id,
            p.name, 
            p.description, 
            u.email creator, 
            ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
            replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
            from issues i 
            left join projects p on p.id = i.project_id 
            left join users u on u.id = p.creator_id  
            left join timelogs t on t.issue_id = i.id  
            where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59'
            group by 2,3,4
            order by 5 desc''', [year, month, year, month]
        )
    if name is not "":
        name = '%' + name + '%'

        project_spent = Projectspent.objects.raw(
            '''select 1 as id,
                p.name, 
                p.description, 
                u.email creator, 
                ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
                replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
                from issues i 
                left join projects p on p.id = i.project_id 
                left join users u on u.id = p.creator_id  
                left join timelogs t on t.issue_id = i.id  
                where (t.created_at  + interval '2h') between '%s-%s-01' and '%s-%s-30 23:59:59' and p.name LIKE %s
                group by 2,3,4
                order by 5 desc''', [year, month, year, month, name]
        )

    form = ProjectSpentForm(initial={
        'year': year,
        'month': month
    })

    spent_sum = 0
    for record in project_spent:
        spent_sum = spent_sum + float(record.spent)

    context = {
        'project_spent': project_spent,
        'form': form,
        'name': name,
        'year': year,
        'month': month,
        'spent_sum': spent_sum
    }

    return render(request, 'trackApp/track3.html', context=context)