---
layout: post
title: "A Visual Inspector for BulkLoader"
permalink: "/trane/2009/aug/09/bulkloader-inspector/"
tags: [actionscript bulk-loader opensource flex]
categories: [trane]
legacy_id: 28
date: "2009-08-09 -0300"
---
A couple of weeks ago I exchanged a few emails with [Chris O'Byrne](http://www.acleveraddress.com/). He was writing a loading lib for actionscritp and was taking some ideas and code from BulkLoader. The result is [MultiLoader](http://code.google.com/p/as3-multiloader/). I haven't look much into it, but one thing struck me.  He created a visual inspector, a GUI that let's helps to understand what is being loaded. I thought this would be a nice addition to BulkLoader, mainly to help others debug and understand what BulkLoader is doing. As they say, good artists copy, great artists steal ;).

It ocurred to me that anything but the simplest interface would require a GUI toolkit. It made sense to do it in Flex.

It turns out that the inspector is very useful, and helped to visualize a few issues with BulkLoader my self. Here is what it looks like:

![The inspector running](/assets/images/blog-posts/bulkloader-inspector-01.jpg) 

Since it uses Flex, you need to use it differently, depending on what your project is.
If you are coding a Flex application, then just instanciate the BulkLoaderInspectorPanel, and you should be all set.
If you are working on a regular (non-flex) project, you should load a compiled swf. But since flex apps have a very specific lifecycle, there are some steps you need to take. The easiest path is to just create a Bootstrapper (trunk/inspector/Bootstrapper.as). Just setup the path to the swf, and it should just work.

There a few visual adjustments to be made, but it's **very** useful as is. If you're into flex and would like to improve on it, patches are very welcome.

Note however, that since it compiles the entire flex framework, hence it has a big file size, it should only be used while debugging. 
