---
layout: post
title: "A Munin plugin to track http response times."
permalink: "/trane/2009/aug/02/munin-plugin-track-http-response-times/"
tags: [munin linux http monitoring slicehost]
categories: [posts]
id: 27
date: "2009-08-02 -0300"
---
After two years of abandonment, I've finally managed to give some love to the server running this site.
After all the trouble, I wanted to have a good monitoring setup, so I can evaluate the changes and how they're performing.

[Munin](http://munin.projects.linpro.no/) has been running for while, but I had never tweaked it. Now, after running nginx and memcahed, I wanted to monitor those as well.

Turns out that Munin's plugin system is easy to extend. But it takes a while to understand how it all comes together: the various jobs, rdd integration, updates, permissions. Specially the autocongif and wildcards plugins, while a neat idea do make things more magical and harder to track.

I wanted to monitor is the total performance of the application. Not how apache, nginx or mysql are doing. Nor only disk or the bandwidth but the final response times, to measure how the entire stack is doing. 

External tools, such as [Pingdom](http://pingdom.com/) and [Monitor.us](http://mon.itor.us/) can handle it, but then you're also dealing with the internet connection, network conditions interfere with the measurements.

So I've hacked a quick plugin for Munin, that will measure response times for the urls you wish to monitor.
This is a how it looks: ![The Http Response munin plugin graph](http://media.stimuli.com.br/blog-posts/http-response.png).

In this particular case, I am monitoring the home url and the same one with a query string. That way, I can keep tabs on how the site is performing with memcached on and off.

Munin plugins are ran through the shell: they can be anything a perl script, c, python, anything else really. This plugin is written in python.  It does require [httplib2](http://code.oogle.com/p/httplib2/) though. I've tested this in python 2.5 and 2.4 (thanks for the patch [Hermann Kase](http://github.com/hermzz) ) on linux, but it should really run on other setups without issues.

I am putting this up on [github](http://github.com/arthur-debert/munin-httpresponse-plugin/tree/master), as future updates will be easier to track. Installing is pretty easy, just copy the httpresonsetime file to where plugins are located (/etc/munin/plugins on ubuntu), chmod it appropriately and add the urls you need to monitor on the config file:


    [httpresponsetime]
        env.urls http://www.example.com,http://www.othersite.com/somewhere


Restart the munin-node daemon, and you're all set.

Of course, just as I finished writing this, I found a similar plugin at the [munin exchange](http://muninexchange.projects.linpro.no/?search=&cid=10&os%5B4%5D=on&os%5B7%5D=on&os%5B3%5D=on&os%5B2%5D=on&os%5B5%5D=on&os%5B8%5D=on&os%5B1%5D=on&os%5B6%5D=on&pid=158).It takes a different approach though, as it allows for one url only to be monitored, and that url is set on the plugin file itself. The solution above seems cleaner.

If anyone else finds this useful, I'll put it up on munin exchange.

