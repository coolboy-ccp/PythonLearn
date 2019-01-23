# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

#使用metaclass创建一个简单的ORM

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField,self).__init__(name, 'varchar(100)')

class IntergerField(Field):
    def __init__(self, name):
        super(IntergerField, self).__init__(name, 'gigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)

        attrs['__mapping__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)


    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s'% sql)
        print('ARGES: %s' % str(args))

class User(Model):
    id = IntergerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


def testUser():
    u = User(id=12, name='michael', email='123.com', password='my-password')
    u.save()

if __name__ == '__main__':
    testUser()