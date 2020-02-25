use pyqt_erp;

-- title;
insert into title values
(1, '사장'),
(2, '부장'),
(3, '과장'),
(4, '대리'),
(5, '사원');

-- department;
insert into department values
(1, '영업', 8),
(2, '기획', 10),
(3, '개발', 9),
(4, '총무', 7);

-- employee
insert into employee(emp_no, emp_name, title, manager, salary, dept, pass, hire_date, gender) values
(4377, '이성래', 1, null, 5000000, 2, password('1234567'), '2000-01-1', TRUE),
(3426, '박영권', 3, 4377, 3000000, 1, password('1234567'), '2000-02-11', TRUE),
(1003, '조민희', 3, 4377, 3000000, 2, password('1234567'), '2005-03-12', FALSE),
(3011, '이수민', 2, 4377, 4000000, 3, password('1234567'), '2010-04-13', FALSE),
(2106, '김창섭', 4, 1003, 2500000, 2, password('1234567'), '2016-05-14', TRUE),
(3427, '최종철', 5, 3011, 1500000, 3, password('1234567'), '2017-06-15', TRUE);

select emp_no, emp_name, title, manager, salary, dept, pass, hire_date, gender, if (pic is not null, 1, 0)
 from employee;

select if (pic is null, 0, 1) from employee;

select * from title;
delete from title where title_no=1;

/* 우분투 MySQL Timezone 설정방법
select @@global.time_zone, @@session.time_zone;

select b.name,a.time_zone_id
from mysql.time_zone a, mysql.time_zone_name b
where a.time_zone_id = b.time_zone_id
and b.name like '%Seoul';
select count(*) from mysql.time_zone;

select @@system_time_zone;


set GLOBAL time_zone='Asia/Seoul';
set time_zone = 'Asia/Seoul';

select @@system_time_zone;
만약 MySQL이 설치되는 OS가 Windows 계열 또는 HP/UX 등이라면 MySQL 사에서 제공하는
MyISAM 파일들을 http://dev.mysql.com/downloads/timezones.html 에서 다운 받은 다음
MySQL 데이터베이스를 중단시키고 'mysql' 서브디렉토리에 직접 복사해 넣어야 한다.
https://dev.mysql.com/doc/refman/5.7/en/time-zone-support.html#time-zone-installation 참조
*/

select * from employee;
