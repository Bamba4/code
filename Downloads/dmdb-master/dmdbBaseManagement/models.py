from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, UUIDField, EmailField
)


class User(Document):
    meta = {'collection': 'user'}
    first_name = StringField(required=True)
    last_name = StringField(required=True)


# audit model
class Audit(Document):
    meta = {'collection': 'audit'}
    created_by = StringField()
    created_at = DateTimeField(default=None, Null=True)
    updated_by = StringField()


# Create your models here.
class Employee(Document):
    meta = {'collection': 'employee'}
    id = UUIDField(unique=True, primary_key=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    address = StringField()
    date_of_birth = DateTimeField(default=None, Null=True)
    role = StringField(required=True)
    phone_number = StringField()
    email = StringField(required=True)
    avatar = StringField(required=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class GodParent(Document):
    meta = {'collection': 'god-parent'}
    id = UUIDField(unique=True, primary_key=True)
    first_name = StringField()
    last_name = StringField()
    address = StringField()
    email = EmailField()
    date_of_birth = DateTimeField(default=None, Null=True)
    avatar = StringField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Tutor(Document):
    meta = {'collection': 'tutor'}
    id = UUIDField(unique=True, primary_key=True)
    first_name = StringField()
    last_name = StringField()
    address = StringField()
    date_of_birth = DateTimeField(default=None, Null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Student(Document):
    meta = {'collection': 'student'}
    id = UUIDField(unique=True, primary_key=True)
    first_name = StringField()
    last_name = StringField()
    address = StringField()
    date_of_birth = DateTimeField(default=None, Null=True)
    surate = StringField()
    joined_at = DateTimeField(default=None, Null=True)
    avatar = StringField()
    god_parent = ReferenceField(GodParent)
    tutor = ReferenceField(Tutor)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
