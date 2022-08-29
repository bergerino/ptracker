select p.name project,
  i.title issue, 
  u.name, 
  replace(ROUND(t.time_spent/3600.0, 1)::text, '.', ',') as spent,
  TO_CHAR(t.spent_at + interval '2h', 'dd.mm.yyyy HH24:MI:SS') date_spent, substring(n.note for 300) note
from issues i
left join projects p on p.id = i.project_id
left join timelogs t on t.issue_id = i.id
left join users u on u.id = t.user_id
left join notes n on n.id = t.note_id
where (t.spent_at + interval '2h') between '2022-06-01' and '2022-06-30 23:59:59'
order by 5, 1, 2