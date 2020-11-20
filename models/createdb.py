import sqlite3

conn = sqlite3.connect('../database.sqlite3')
 
c = conn.cursor()

c.execute('''create table if not exists students(
    number integer primary key not null,
    name varchar(255) not null
    )'''
)
c.execute('''INSERT INTO students (number, name) VALUES(20181234, '電波太郎')''')

c.execute('''create table if not exists lessons(
    id integer primary key AUTOINCREMENT,
    date DATE not null,
    koma integer not null,
    name varchar(255)
    )'''
)

c.execute('''create table if not exists attendances(
    lesson_id integer not null,
    student_number integer not null,
    is_attended boolean not null default true,
    primary key(lesson_id, student_number),
    foreign key (lesson_id) references lessons(id),
    foreign key (student_number) references student(number)
    )'''
)

conn.commit()

c.execute("SELECT * FROM students")

result = c.fetchall()
 
print(result)

conn.close()