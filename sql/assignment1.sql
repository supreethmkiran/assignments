create database supreeth;
use supreeth;
create table ODI
(
Team_ID integer primary key,
Ranks integer,
team varchar(50) Unique,
Matches integer ,
points integer default 0,
rating integer
check (rating>20) 
);
insert into ODI values(1,1,'England',43,5372,125);
insert into ODI values(2,2,'India',47,5669,121);
insert into ODI values(3,3,'South Africa',39,4488,115);
insert into ODI values(4,4,'New Zealand',33,3729,113);
insert into ODI values(5,5,'Australia',40,4342,109);
insert into ODI values(6,6,'Pakistan',	41,3846,94);
insert into ODI values(7,7,'Bangladesh',35,3155,90);
insert into ODI values(8,8,'West Indies',39,3022,77);
insert into ODI values(9,9,'Sri Lanka',43,3266,76);
insert into ODI values(10,10,'Afghanistan',31,1961,63);
insert into ODI values(11,11,'Zimbabwe',30,1609,54);
insert into ODI values(12,12,'Ireland',26,1176,45);
insert into ODI values(13,13,'Scotland',10,373,37);
insert into ODI values(14,14,'Nepal',8,152,19);
insert into ODI values(15,15,'United Arab Emirates',15,144,10);
insert into ODI values(16,16,'Papua New Guinea',9,50,6);



select * from ODI where rating > 100;
select * from ODI where rating<100 AND Matches<40;
select * from ODI where team like "S%";
select * from ODI where team not like "%a";
select * from ODI where Matches in (15,40,39);
select * from ODI order by Matches;
select * from ODI order by points;
create view Matches1 as select * from ODI where Matches>30;
delete from ODI where team="Papua New Guinea";
alter table points add column team_id integer 
references odi(team_id) on update cascade on delete cascade; 


create table points
(
Pos integer,
Played integer,
Won integer,
Lost integer,
T_NR integer default 0,
Points integer,
NRR decimal(3,2),
Team_ID integer primary key,
foreign key fk(Team_ID) references ODI(Team_ID)
);
insert into points values(1,4,3,0,1,7,2.16,4);
insert into points values(2,4,3,1,0,6,0.57,5);
insert into points values(3,3,2,0,1,5,0.53,2);
insert into points values(4,3,2,1,0,4,1.30,1);
insert into points values(5,4,1,1,2,4,-1.51,9);
insert into points values(6,3,1,1,1,3,2.05,8);
insert into points values(7,4,1,2,1,3,-0.71,7);
insert into points values(8,4,1,2,1,3,-1.79,6);
insert into points values(9,4,0,3,1,1,-0.95,3);
insert into points values(10,3,0,3,0,0,-1.49,10);



alter table points add column Team_Id integer 
references odi(team_id) on update cascade on delete cascade; 


# question 3 not done
UPDATE POINTS SET T_ID="4" where pos="1"; 
UPDATE POINTS SET T_ID="5" where pos="2"; 
UPDATE POINTS SET T_ID="2" where pos="3"; 
UPDATE POINTS SET T_ID="1" where pos="4"; 
UPDATE POINTS SET T_ID="9" where pos="5"; 
UPDATE POINTS SET T_ID="8" where pos="6"; 
UPDATE POINTS SET T_ID="7" where pos="7"; 
UPDATE POINTS SET T_ID="6" where pos="8"; 
UPDATE POINTS SET T_ID="3" where pos="9"; 
UPDATE POINTS SET T_ID="10" where pos="10";

select * from ODI,Points
where ODI.Team_ID= Points.Team_ID;

select * from odi 
where Ranks between 6 and 16

alter table ODI 
add column Tied integer default 0;

**alter table points add column team_id integer 
references odirank(team_id) on update cascade on delete cascade; 
**



ALTER TABLE POINTS
CHANGE T_NR NR integer;










******create table summary
(
Team_ID integer,
Winning_Team varchar(50),
Defeated_Team Varchar(50),
Location Varchar(50),
Dates Varchar(20),
Won_By varchar(20),
Additional_Info varchar(20)
foreign key fk(Team_ID) references ODI(Team_ID)
);

insert into summary values("England","South Africa","The Oval","May","104 Runs",Null);
insert into summary values("West Indies","Pakistan","Trident Bridge","May","7 Wickets",Null);
insert into summary values("New Zealand","Sri Lanka","Sophia","June 1","10 Wickets",Null);
insert into summary values("Australia","Afghanistan","Bristol","June 1","7 Wickets",Null);
insert into summary values("Bangladesh","South Africa","The Oval","June 2","21 Runs",Null);
insert into summary values("Pakistan","Sri Lanka","Bristol","June 7",Null,"Rained Off");
******







create table results
(Team1 int,
Team2 int,
Marginruns int,
Marginwickets int,
Month varchar(15),
Day int,
Place varchar(30),
foreign key (Team1) references ODI(Team_ID),
foreign key (Team2) references ODI(Team_ID)
);

insert into results values(1,3,104,null,'May',30,'The Oval');
insert into results values(8,6,null,7,'May',31,'Trent Bridge');
insert into results values(4,9,null,10,'June',1,'Sophia Gardens');
insert into results values(5,10,null,7,'June',1,'Bristol');
insert into results values(7,3,21,null,'June',2,'The Oval');
insert into results values(6,1,14,null,'June',3,'Trent Bridge');
insert into results values(9,10,34,null,'June',4,'Sophia Gardens');
insert into results values(2,3,null,6,'June',5,'Rose Bowl');
insert into results values(4,7,null,2,'June',5,'The Oval');
insert into results values(5,8,15,null,'June',6,'Trent Bridge');
insert into results values(6,9,null,null,'June',7,'Bristol');
insert into results values(1,7,106,null,'June',8,'Sophia Gardens');
insert into results values(4,10,null,7,'June',8,'Taunton');
insert into results values(2,5,36,null,'June',9,'The Oval');
insert into results values(3,8,null,null,'June',10,'Rose Bowl');
insert into results values(7,9,null,null,'June',11,'Bristol');
insert into results values(5,6,41,null,'June',12,'Taunton');
insert into results values(2,4,null,null,'June',13,'Trent Bridge');
insert into results values(1,8,null,8,'June',14,'Rose Bowl');
insert into results values(5,9,87,null,'June',15,'The Oval');
insert into results values(3,10,null,9,'June',15,'Sophia Gardens');
insert into results values(2,6,89,null,'June',16,'Old Trafford');
insert into results values(8,7,null,null,'June',17,'Taunton');
insert into results values(1,10,null,null,'June',18,'Old Trafford');
insert into results values(4,3,null,null,'June',19,'Edgbaston');
insert into results values(5,7,null,null,'June',20,'Trent Bridge');
insert into results values(1,9,null,null,'June',21,'Headingley');
insert into results values(2,10,null,null,'June',22,'Rose Bowl');
insert into results values(8,4,null,null,'June',22,'Old Trafford');
insert into results values(6,3,null,null,'June',23,"Lord's");
insert into results values(7,10,null,null,'June',24,'Rose Bowl');
insert into results values(1,5,null,null,'June',25,"Lord's");




select distinct place from results;



select count(Place) from results
where Place="Lord's";



select place,count(Place) from results
group by place;#Question 6



select team1,Team2 from results
where Marginwickets is null
and Marginruns is null;


select avg(Marginruns) from results
where Marginruns is not null; 





select o.team, max(r.marginwickets)from results r,odi o 
where marginwickets=(select max(Marginwickets) from results)
and o.team_id=r.team1;


select r.team1,o.team,r.marginwickets from results r,ODI o where marginwickets = (select max(Marginwickets) from results) 
and r.Team1=o.Team_ID ;



select o.team,r.team1,r.Team2,r.place from results r,ODI o 
where r.team1=o.Team_ID
order by team1,team2,place; #q9;


select r.* from results r,ODI o where place in ("Lord's","Oval","Trent Bridge","Old Trafford")
and r.team1=o.Team_ID;



select distinct(o.points) ,o.team,r.team1 from results r ,ODI o where o.points not like 0
and r.team1=o.Team_ID;


select o.team ,o.Matches ,count(r.Marginruns) as Matches_Won,
count(r.team2) as Matches_Lost from results r,odi o
where Place not like "Lord's"
and r.Team1=o.Team_ID
group by team1 ;



select o.team ,o.Matches ,count(r.Marginruns) as Matches_Won,
count(r.team2) as Matches_Lost from results r,odi o
where Place not in ("Lord's","Trent","Oval")
and r.Team1=o.Team_ID
and count(r.Marginruns)>=count(r.Team2)
group by team;




select t.team1,win (select team1,count(team1) win from results 
where Place not like "Lord%" group by team1 
union all
select team2,count(team2) loss from results
where Place not like "Lord%" group by team2) t ;




8) select max(runs),Team1 from results,Fixture 
where Fixture.Match_No=Details.Match_No 
and runs>=50 group by Team1;

14 not done
