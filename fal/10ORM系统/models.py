

#选课系统

from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description='学生姓名')
    pwd = fields.CharField(max_length=50, description='学生密码')
    sno = fields.IntField(description='学号')
    #一对多的关系
    clas = fields.ForeignKeyField('models.Clas', related_name='students', description='所属班级')
    #多对多的关系
    courses = fields.ManyToManyField('models.Course', related_name='students', description='选修课程')
    

class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description='课程名称')
    teacher = fields.ForeignKeyField('models.Teacher', related_name='courses', description='授课教师')
    
    
    
class Clas(Model):
    name = fields.CharField(max_length=50, description='班级名称')
    
class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description='教师姓名')
    pwd = fields.CharField(max_length=50, description='教师密码')
    tno = fields.IntField(description='教师编号')