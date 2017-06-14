# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
import datetime
from django.test import TestCase
import os
from models import Post
import traceback


def save_md_files_into_database(f_dir):
    if os.path.exists(f_dir):
        t = Tag.objects.get(name="tag test")
        c = Category.objects.get(name="category test")
        u = User.objects.get(id=1)
        list_dir_and_files = os.walk(f_dir)
        post_list = Post.objects.all()
        title_list = [x.title for x in post_list]
        title_set = set(title_list)
        for root, dirs, files in list_dir_and_files:
            for item in files:
                if item.endswith(".md"):
                    title = item[:-3]
                    with open(os.path.join(f_dir, item)) as f:
                        content = f.read()
                    if title.decode("utf-8") not in title_set:
                        print title
                        p = Post(title=title,
                                 body=content,
                                 author=u,
                                 category=c,
                                 abstract=title,
                                 create_time=datetime.datetime.now(),
                                 modified_time=datetime.datetime.now())
                        p.save()
                        p.tags.add(t)
                        print "*" * 100
                    else:
                        if Post.objects.get(title=title).body.encode("utf-8") != content:
                            print "{0}.md modified!".format(title)
                            p_modified = Post.objects.get(title=title)
                            p_modified.body = content
                            p_modified.save()
    else:
        raise Exception("path \"{0}\" not exist".format(f_dir))

if __name__ == '__main__':
    pass
