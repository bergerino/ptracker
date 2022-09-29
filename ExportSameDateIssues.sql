create view ExportSameDateIssues as
select p.name project,
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
    left join notes n on n.id = t.note_id
    where (t.spent_at + interval '2h') between '2022-07-01' and '2022-07-31'
    group by 2, 4, 5, date_spent