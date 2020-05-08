#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

example_db = SqliteDatabase('example.db')

class ExampleModel(Model):
    class Meta:
        database = example_db

class User(ExampleModel):
    name = CharField()
    age = IntegerField()

    def __unicode__(self):
        return self.name


class Car(ExampleModel):
    model = CharField(null=True)
    plate = CharField(unique=True)
    user = ForeignKeyField(User, related_name="cars")

    def __unicode__(self):
        return "{}-{}".format(self.model, self.plate)


# Creamos las tablas si no existen
User.create_table(fail_silently=True)
Car.create_table(fail_silently=True)

u0 = User()
u0.name = "Ramona Flowers"
u0.age = 24
u0.save()
u1 = User(name="Stephen Stills", age=24)
u1.save()
u2 = User(name="Scott Pilgrim", age=23)
u2.save()

print("Todos los Usuarios")
for u in User.select():
    print(u.id, u.name, u.age)

print("Con ID=1")
print(User.get(User.id == 1))

print("Con nombre 'Stephen Stills'")
print(User.get(User.name == "Stephen Stills"))

print("Con edad <= 24")
for u in User.filter(User.age <= 24):
    print(u)

print("Con nombre que empieza con 'S'")
for u in User.filter(fn.Substr(User.name, 1, 1) == "S"):
        print(u)

# Metamos los autos en el juego
car0 = Car(model="2012", plate="jbc 2502", user=u0)
car0.save()

print("Autos de u0")
for c in Car.filter(Car.user == u0):
    print("{} -> {}".format(c, c.user))

print("Cantidad de autos de personas con 24 años")
print(Car.select().join(User).where(User.age == 24).count())

print("Autos con modelo 2012 de usuarios de 24 años")
for car in Car.select().join(User).where(User.age == 24, Car.model=="2012"):
    print(car)


print("Una actualizacion")
c = Car.get(plate="jbc 2502")
c.plate = "AAC 6666"
c.save()

print("un borrado")
print(u0.cars.count())
car0.delete_instance()
print(u0.cars.count())
