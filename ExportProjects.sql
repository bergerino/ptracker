select
 p.name, 
 p.description, 
 u.email creator, 
 ROUND(SUM(t.time_spent)/3600.0, 1) as spent,
 replace(ROUND(SUM(t.time_spent)/3600.0, 1)::text, '.', ',') as spent_txt
from issues i 
left join projects p on p.id = i.project_id 
left join users u on u.id = p.creator_id  
left join timelogs t on t.issue_id = i.id  
where (t.created_at  + interval '2h') between '2022-06-01' and '2022-06-30 23:59:59'
group by 1,2,3
order by 4 desc
