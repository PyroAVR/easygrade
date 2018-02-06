from student import student
from grade import grade
from gradeitem import gradeitem
from bootstrap import *
from student import *
import java_preprocess
import java #this sure does look funky

# build items
# preprocess
preprocess_files = java_preprocess.target()
preprocess_files.add_file('game/Box.java')
preprocess_files.add_file('game/Dot.java')
preprocess_files.add_file('game/Line.java')
preprocess_files.add_file('game/Lines.java')
preprocess_files.add_file('game/DotsAndBoxes.java')
preprocess_files.add_file('game/GameBoard.java')
preprocess_files.add_file('game/Player.java')
preprocess_files.set_clean_level('all')

# build individual
Box             = java.target('game/Box.java')
Dot             = java.target('game/Dot.java')
Line            = java.target('game/Line.java')
Lines           = java.target('game/Lines.java')
DotsAndBoxes    = java.target('game/DotsAndBoxes.java')
GameBoard       = java.target('game/GameBoard.java')
Player          = java.target('game/Player.java')

# tests


# grade items

# ps = gradeitem('Problem Solving')
# ps.add_subitem('PS', 15)
# 
# inlab = gradeitem('In-Lab Activity')
# inlab.add_subitem('In-lab', 10)
# 
# design = gradeitem('Design')
# design.add_subitem('object-oriented approach', 5)
# design.add_subitem('all classes and methods present', 5)
# 
# impl = gradeitem('Implementation')
# impl.add_subitem('Dot', 5)
# impl.add_subitem('Line', 5)
# impl.add_subitem('Lines', 10)
# impl.add_subitem('Box', 10)
# impl.add_subitem('LinesAndBoxes', 5)
# impl.add_subitem('2x3 board', 10)
# impl.add_subitem('2x2 board', 5)
# impl.add_subitem('error handling', 5)
# 
# style = gradeitem('Style and Documentation')
# style.add_subitem('headers', 4)
# style.add_subitem('docstrings', 4)
# style.add_subitem('explanations', 2)
# 
# lab_session = grade()
# lab_session.add_grade_item(ps)
# lab_session.add_grade_item(inlab)
# lab_session.add_grade_item(design)
# lab_session.add_grade_item(impl)
# lab_session.add_grade_item(style)

# should be able to do something like gradeitem.generate_report()
# to make each student's report, and then fill with report.run_tests()

# bootstrap from unpacked mycourses zip
submissions = enumerate_submissions('.')
rename_map = build_name_map(submissions)
unpack_and_rename(rename_map)
clean_zip(submissions)

#generate students
def find_student_folders(path):
    student_names = list()
    for entry in os.scandir(path):
        if entry.is_file(): continue
        if not ',' in entry.name:  # super hacky but it's whatever
            print('ignoring folder in', path,':', entry.name)
        else:
            print('found submission', entry.name)
            student_names.append(entry)
    return student_names

students = list()
for entry in find_student_folders('.'):
    students.append(student(*name_from_dir(entry)))
for student in students:
    print('processing submission for: ' + student.name)
    #student.register_grade(lab_session)
    student.add_build_step(preprocess_files)
    student.add_build_step(Box)
    student.add_build_step(Dot)
    student.add_build_step(Line)
    student.add_build_step(Lines)
    student.add_build_step(DotsAndBoxes)
    student.add_build_step(GameBoard)
    student.add_build_step(Player)
    student.build()
