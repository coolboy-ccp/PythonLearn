# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

def aDict():
    return {'name':'Bob', 'age':20, 'score':'80'}


import pickle
#------------对象数列化和反序列化
def testSerial():
    f = open('PythonPickle.txt', 'wb')
    pickle.dump(aDict(), f)
    f.close()

def testLoad():
    f = open('PythonPickle.txt', 'rb')
    d = pickle.load(f)
    f.close()
    print(d)

#--json转换
import json

def aJson():
    return '{"name": "lili", "age": 20, "score": 99}'

def obcToJson():
    jsonStr = json.dumps(aDict())
    print(jsonStr)
    return jsonStr

def jsonToObc():
    print(json.loads(aJson()))

#---class to json
class JsonModel:
    def __init__(self, name, age, score):
        self._name = name
        self._age = age
        self._score = score

    def __str__(self):
        return 'JsonModel: name = %s, age = %s, score = %s' % (self._name, self._age, self._score)

def m2j(obj):
        return {
            'name' : obj._name,
            'age' : obj._age,
            'score' : obj._score
        }

def j2m(json):
    return JsonModel(json['name'], json['age'], json['score'])

def aJsonModel():
    return JsonModel(name='lili', age=20, score=99)

def classToJson(obj):
        print(json.dumps(obj, default=m2j))

def testClassToJson():
    classToJson(aJsonModel())

def testClassToJsonUse__dict__():
    print(json.dumps(aJsonModel(), default=lambda obj: obj.__dict__))

def testJsonToClass():
    print(json.loads(aJson(), object_hook=j2m))

if __name__ == '__main__':
    #testSerial()
    #testLoad()
    #obcToJson()
    #jsonToObc()
    testClassToJson()
    testClassToJsonUse__dict__()
    testJsonToClass()
    pass