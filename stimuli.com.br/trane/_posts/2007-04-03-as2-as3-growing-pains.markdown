---
layout: post
title: "AS3 Happy bits #1: Runtime errors"
permalink: "/trane/2007/apr/03/as2-as3-growing-pains/"
tags: []
categories: [trane]
legacy_id: 8
date: "2007-04-03 -0300"
---
Sure, the much improved performance AVM is great. A sane display hierarchy helps (or rather doesn't get a lot in the way) too, but my favorite AS3 feature is runtime errors.

Actionscript was my first programming language. After doing it for a while I decided I need to lear a *real* language and decided to learn Java (it was 2001 after all...). After wrestling with the compiler for a while I remember being shock running into my first [NullPointerException](http://java.sun.com/j2se/1.4.2/docs/api/java/lang/NullPointerException.html). What do you mean my program just "quits"? After getting used it to it became clear: actionscript was a freak language: no matter what happens (or should but doesn't), your program will keep on running. No warnings, no traces, it will keeping haply humming along. Even worse, being a dynamic loosely typed language there was very little error checking at all in AS2. Even if you did use "static" typing it was mostly useless: the bread an butter of the API, the MovieClip object was dynamic: mistyped properties on it wouldn't be caught by the compiler: no dice.

What looks at first as a nice way to make beginning programmers less intimidated with programming soon enough becomes debugging hell. Anything. Reading from an existing location (local files or http streaming) will not throw any errors. Telling a MovieClip that doesn't exist to do something. Linking from a library asset that isn't loaded yet. Nothing. Whatever goes wrong, you must find out on your own. It's kind of ironic, since you - the programmer - are asked to do something that the computer has already done (it has hidden it from you). 

An ugly side effect of this is that because code can fail anywhere and you must find about it on your own, to produce solid code, you end up putting error checking all over the place. Great. Now your code looks like C. 

In flash 8, Macromedia introduced Error. But like a lot of flash things (in the old days, I hope) it was a half-baked solution: almost nothing would throw an error (only NetStream.close() as far as I can remember). The feature was there but wasn't of any use throughout the API. You could however, create and throw your own errors, but most developers didn't do it, it wasn't a common idiom in the AS world. If it is useful, how come the API doesn't use it?

So I was happy to learn that AS3 and the new AVM make a better use of errors and better still, that the runtime will let you know (even the player, as a plugin or stand alone), on the spot that some assumption isn't holding. They implemented it in a nice, unobtrusive way: normal users wouldn't see anythings (the stack will stop execution though) but developers (a reasonable assumption for people with the debug player installed) will see the error.

As an added bonus: Error.getStackTrace() so you can print and check code execution path.

Dealing effectively with errors takes sometime to get used to. Even though they're very useful I certainly don't want to go down the checked exceptions with empty nested try-catch blocks all over the place. That's why I am glad AS didn't go the Java route, making code that may throw exception required to say so in advanced, and client code to deal with it. In theory it looks like you're making code more solid, but it [doesn't work in practice](http://www.mindview.net/Etc/Discussions/CheckedExceptions).