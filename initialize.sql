create table if not exists students(
    number integer primary key not null,
    name varchar(255) not null
);

create table if not exists lessons(
    id integer primary key AUTOINCREMENT,
    date DATE not null,
    koma integer not null,
    name varchar(255)
);

create table if not exists attendances(
    lesson_id integer not null,
    student_number integer not null,
    is_attended boolean not null default true,
    primary key(lesson_id, student_number),
    foreign key (lesson_id) references lessons(id),
    foreign key (student_number) references student(number)
);