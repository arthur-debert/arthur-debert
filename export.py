from coltrane.models import *
from works.models import *
template = """---
layout: post
title: "%s"
permalink: "%s"
tags: [%s]
categories: [%s]
id: %s
date: "%s -0300"
---
%s"""
for entry in Entry.objects.filter():
        date_str = entry.pub_date.strftime("%Y-%m-%d")
        fd = open('data/posts/%s-%s.markdown' % (date_str, entry.slug), 'w')
        url = entry.get_absolute_url()
        post = template % (entry.title, url, entry.tag_list, "posts",  entry.id, date_str, entry.body)
        fd.write(post.encode('utf-8'))
for entry in Work.objects.all():
        date_str = entry.pub_date.strftime("%Y-%m-%d")
        fd = open('data/works/%s-%s.markdown' % (date_str, entry.slug), 'w')
        url = entry.get_absolute_url()
        post = template % (entry.title, url, "", "works", entry.id, date_str, entry.body)
        fd.write(post.encode('utf-8'))


import simplejson
from simplecomments.models import Comment
comments = []
for comment in Comment.objects.filter(content_type__id=16, is_public=True):
        comments.append({
            'post_url':comment.get_content_object().get_absolute_url(),
            'post_id':comment.get_content_object().id,
            'author': comment.name,
            'email': comment.email,
            'date': comment.date.strftime("%Y-%m-%d %H:%M:%S"),
            'body': comment.body
            })
for comment in Comment.objects.filter(content_type__name__icontains='work', is_public=True):
        comments.append({
            'work_url':comment.get_content_object().get_absolute_url(),
            'work_id':comment.get_content_object().id,
            'author': comment.name,
            'email': comment.email,
            'date': comment.date.strftime("%Y-%m-%d %H:%M:%S"),
            'body': comment.body
            })                                                                                                                 
open("data/comments.json", 'w').write(simplejson.dumps(comments))
