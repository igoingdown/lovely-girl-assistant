# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import datetime
from test_python_call_shell import foo
from qiniu import *
from qiniu_util import upload_to_cloud

# Create your views here.

def index(request):
    tag_lists = Post.objects.all()
    print tag_lists
    return render(request, 'blogApp/index.html', context={'title': '我的博客首页',
                                                          'welcome': '欢迎来到我的博客首页',
                                                          'items': tag_lists,
                                                          })
    pass


def submit(request):
    return render(request, 'blogApp/form.html',
                  context={'welcome': '欢迎'})
    pass


@csrf_exempt
def investigate(request):
    if request.method == 'POST':
        print 'Raw Data: "%s"' % request.body
        params = {'key': '34a937c951c84cb3aaa855e54fda653e',
                  'info': '你好'}
        forward = HistoryMessage(create_time=datetime.datetime.now(),
                                 modified_time=datetime.datetime.now(),
                                 body="你好", talk_direction=0)
        forward.save()
        r = requests.post("http://www.tuling123.com/openapi/api", data=params)
        if r.status_code == 200:
            data = json.loads(r.text)
            data['time'] = datetime.datetime.now()
            with open("./blogApp/demo/bin/source.txt", "w") as f:
                f.write(data['text'])
            foo()
            ret, info = upload_to_cloud("star", "ans.wav", "./blogApp/ans.wav")
            backward = HistoryMessage(create_time=datetime.datetime.now(),
                                     modified_time=datetime.datetime.now(),
                                     body=params['info'], talk_direction=1,
                                     type=data['code'])
            backward.save()
    return JsonResponse(data)


@csrf_exempt
def stores(request):
    if request.method == 'POST':
        print 'Raw Data: "%s"' % request.body
        params = {'key': '34a937c951c84cb3aaa855e54fda653e',
                  'info': '北京到哈尔滨的火车'}
        forward = HistoryMessage(create_time=datetime.datetime.now(),
                                 modified_time=datetime.datetime.now(),
                                 talk_direction=0,
                                 body="北京到哈尔滨的火车")
        forward.save()
        r = requests.post("http://www.tuling123.com/openapi/api", data=params)
        if r.status_code == 200:
            d = json.loads(r.text)
            d['time'] = datetime.datetime.now()
            backward = HistoryMessage(create_time=datetime.datetime.now(),
                                      modified_time=datetime.datetime.now(),
                                      talk_direction=1,
                                      body=params['info'],
                                      url_body=d['url'],
                                      type=d['code'])
            backward.save()
            with open("./blogApp/demo/bin/source.txt", "w") as f:
                f.write(d['text'])
            foo()
            upload_to_cloud('star', 'ans.wav', './blogApp/ans.wav')
    return JsonResponse(d)


@csrf_exempt
def flight(request):
    if request.method == 'POST':
        print 'Raw Data: "%s"' % request.body
        params = {'key': '34a937c951c84cb3aaa855e54fda653e',
                  'info': '明天北京到拉萨的飞机'}
        forward = HistoryMessage(create_time=datetime.datetime.now(),
                                 modified_time=datetime.datetime.now(),
                                 talk_direction=0,
                                 body=params['info'])
        forward.save()
        r = requests.post("http://www.tuling123.com/openapi/api", data=params)
        if r.status_code == 200:
            d = json.loads(r.text)
            d['time'] = datetime.datetime.now()
            print d['text']
            with open('./blogApp/demo/bin/source.txt', 'w') as f:
                f.write("am")
            foo()
            upload_to_cloud('star', 'ans.wav', './blogApp/ans.wav')
            backward = HistoryMessage(create_time=datetime.datetime.now(),
                                      modified_time=datetime.datetime.now(),
                                      talk_direction=1,
                                      body='明天北京到拉萨的飞机',
                                      url_body=d['url'],
                                      type=d['code'])
            backward.save()

    return JsonResponse(d)



