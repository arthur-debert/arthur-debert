---
layout: post
title: "As2 Class Paths are global variables"
permalink: "/trane/2007/feb/04/as2-class-paths-are-global-variables/"
tags: [as2 actionscript]
categories: [trane]
legacy_id: 7
date: "2007-02-04 -0300"
---
Globals are evil, anyone will tell you that.

In AS2 there are no real classpaths, but a chain of objects bound to the `_global` space. In fact, before Flash MX came out this was the canonical way to make sure your "semi-global" objects were safe kept: creating nested objects that would look like a class path, and put your data there. For example:

    // checks to make sure we don't overwrite anybody else's objects
    if (!_global.com) _global.com = {};
    if(!_global.com.stimuli)_global.com.stimuli = {};
    _global.com.stimuli.myFavoriteColor = 0xFF0000;

This code hides a variable "myFavoriteColor" inside a global object com.stimuli, that looks like a classpath. This works well. So well that, in fact, it's how classpaths are usually created in Javascript. If you are careful to make sure you don't delete anybody else's "com" or "org" objects you should be fine. Since in AS2 and Javascript there are no real private variables(except for values hidden inside closures) that's pretty much how far  classpaths go. 

But recently, I've been bitten by a nasty side effect of this: a global object is no substitute for a real class loader. In [Gringo's website](http://www.gringo.nu/) the shell swf loads each job in our portfolio as an external swf. The website has been online for almost six months, and must load swf made with very different needs. The trouble is: sometimes, the same libraries are used in different swfs. And worse, each one is a different version. For example, we use [Zeh's](http://www.zeh.com.br/) excellent [Tweener](http://code.google.com/p/tweener/) for scripted animations, and have been doing so for sometime. What if a new swf must use a newer version of Tweener, than the one the 'shell' was compiled with. The flash player will keep the class definition compiled at the first swf that it runs into. So if the "main.swf" has revision 38 compiled and the player runs that first, a second swf, that was compiled later, with revision 173 will end up using the first class definition: revision 38. Now you are hosed.

Even worse, if demo "A" uses revision 56 and demo "B" uses revision 98, the cached version will depend on which version the player runs into first. That means that how the class will behave depends on runtime execution order, if demo "A" is viewed first, then when demo "B" is loaded it will work differently then if their viewing order was reversed. This make bug tracking extremely hard. Testing quickly becomes unmanageable: with 20 demos there will be millions permutations. 

While in most use cases the fact that classpaths are just global object is pretty harmless, in situations where many different swfs may refer to the same class names (but different versions) shatters the illusion that both should be treated the same way. The flash player(the old AVM) is at least predictable on how it behaves, but that can still harvest some pretty nasty bugs.

There are a few partials solutions to this, but all a bit hackish. One obvious choice is to instruct programmers to put all of their classes into dedicated classpaths, so they're run as separate classes. Besides being a lot of work to move classpaths around like that it quite error prone. Another hack is to keep track of all classes (looping recursively though the global object and looking for variables that are of type Functions). Then, every time you load a new swf, you diff that class map, and check if all new classes are inside an expected class path, tracing a warning message if they're not. As the number of classes increase this can affect performance. Not good.

I understand that's this is an edge case, and should be pretty rare if you consider the scope of most actionscript projects. Still, it' worth noting that abstractions are only good until they break.

p.s.: AS3 acknowledges this problem and has a well defined (if a source of confusion) to deal with it: the ApplicationDomain. When loading external swfs, you can choose to "separate" it's code, it will run as if in a new classpath, avoiding all this mess.