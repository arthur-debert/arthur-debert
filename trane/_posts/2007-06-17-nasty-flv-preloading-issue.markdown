---
layout: post
title: "Nasty FLV preloading issue"
permalink: "/trane/2007/jun/17/nasty-flv-preloading-issue/"
tags: [actionscript flv annoyances]
categories: [trane]
legacy_id: 14
date: "2007-06-17 -0300"
---
Flash is, by far, the best way to deliver video on the web. The wide availability of the plugin makes it a no brainer.

I always used progressive download video, meaning video that's read from a vanilla http connection, no special streaming server on the backend. I'd love to hear the stats, but my guess is that the majority of flash video is delivered this way. The huge video sites, [youtube](http://youtube.com), [google video](http://video.google.com/) and [yahoo videos](http://video.yahoo.com/) all use flash with progressive download. But the API for showing video content is highly skewed towards using Flash Media Server. Sure Adobe(then macromedia) expects to make a buck on that, but still it's pretty odd that the most common use case is so cumbersome to code.


With the great [architectural changes](http://www.stimuli.com.br/trane/2007/may/14/as3-happy-bits-2-displayobject-hierarchy/) I was really chocked to learn the the NetStream remained mostly unchanged. It's awkward to use. It's full of small confusing details and the documentation could be so much better. I sure am not the only one to feel this way. [Traces from the youtube player](http://blog.emmettshear.com/post/2007/03/06/Oh-the-things-that-youll-see), from the [nytimes player](http://www.nytimes.com) make that clear.


So we hacked a sane VideoStream class for AS2 and I wanted to port it to AS3. The idea was to have a class that could do something like:

    var vs : VideoStream = new VideoStream(url, buffertime);
    // video loops once the end of the stream is reached
    vs.loops = true ; 
    // listen to complete loading events
    vs.addEventListener(Event.COMPLETE, onVideoLoaded); 
    // listen to loading progres events
    vs.addEventListener(Event.PROGRESS, onLoadingProgress);
    vs.addEventListener("playComplete", onPlayFinished);
  
    // and then later:
    // the video duration:
    trace(vs.duration)
    // and so on
    </code>
    In order to start a NetStream, you must instantiate it with a NetConnection object. it's ugly. You have to say:
    <code  class="actionscript">
    nc = new NetConnection();
    nc.connect(null);
    stream = new NetStream(nc);


Why on earth you can't say simply stream = new NetStream(); and, with no parameters for the NetConnection,  it would do it for you?
Since the NetConnection object doesn't do anything, I coded this class differently. Instead of keeping the NetConnection as a class property, I simply created a local variable and used that to instantiate the NetStream. But then something funny would happen. For a while the NetStream.bytesLoaded and NetStream.bytesTotal would behave as expected, at first it would be zero, until the the response would return the content length and then it would show the right bytes total and bytes loaded for a few executions, and THEN it would read 0 for both. That's right, after a few milliseconds the bytesTotal would go from 28428 to 0. That combined with a miss configured apache omitting the content length, and it took us hours to chase this bug. Worse it wasn't very predictable: sometimes loading information would read correctly all the way trough. 


Googling around, I came across [this thread](http://www.actionscript.org/forums/showthread.php3?t=101635). The post is 3 years old, for flash MX , but it's the same issue. They found the workaround but didn't understand why. Here's what I think happens. When you create a new NetConnection and the NetStream object everything is fine. But if the NetConnection is a local variable inside a function it will be marked for garbage collection by the VM. At some point the gc kicks in and clears the NetConnection object, since it is a local variable. When that happens, the NetStream goes cuckoo and reads dummy values for bytesLoaded. Because you don't know when the gc will do it's thing, it is unpredictable, intermittent. If the gc is idle until you finished your preloading code, it works. The strangest part is that even if the gc clears the NetConnection object and the loading information goes berseck, you can still use the NetStream. It's there. It's readable and all, but the loading information becomes useless. The fix is easy. Just make sure you keep a reference to the NetConnection object, as a class property, anywhere the gc won't clean it up.