# Write your MySQL query statement below
with student_and_subjects as (
select st.student_id , st.student_name , su.subject_name from students as st cross join subjects su)

select s.student_id , s.student_name , s.subject_name , count(e.student_id) as attended_exams from student_and_subjects as s left join examinations as e on s.student_id = e.student_id and s.subject_name = e.subject_name group by s.student_id , s.student_name , s.subject_name order by s.student_id, s.subject_name;


-- students_and_subjects = students.join(subjects , how="cross")
-- result = (students_and_subjects.join(examinations , (students_and_subjects["student_id"] == examinations["student_id"]) &
-- (students_and_subjects["subject_name"] == examinations["subject_name"]) , how = "left")
--                 .groupBy(students_and_subjects["student_id"] , students_and_subjects["subject_name"])
--                 .agg(
--                     count(examinations["student_id"]).alias("attended_exams")
--                 )
--                 .select(
--                     students_and_subjects["student_id"],
--                     students_and_subjects["student_name"],
--                     students_and_subjects["subject_name"],
--                     col("attended_exams")
--                 )
-- )