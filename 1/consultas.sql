-- Top 10 países con más títulos en Netflix:
select country ,count(*) as cantidad, CONCAT(ROUND(( count(*) / ( SELECT count(*) FROM films ) * 100 ),2 ), '%') as porcentaje from films f join filmsforcountry fc on (f.show_id = fc.show_id) join country c on (fc.idcountry = c.idcountry) group by country order by cantidad desc limit 10;
-- Géneros más populares:
select gender ,count(*) as cantidad from films f join filmsforgender fg on (f.show_id = fg.show_id) join gender g on (fg.idgender = g.idgender) group by gender order by cantidad desc;
--Cantidad de títulos lanzados por año:
SELECT substring(date_added,-4,4) as year, count(*) as cantidad FROM netflix.films group by year order by year desc;
