---
layout: post
title: "Preloading Video in AS2"
permalink: "/trane/2006/dec/10/preloading-video-as2/"
tags: [actionscript as2 video flv]
categories: [trane]
legacy_id: 9
date: "2006-12-10 -0300"
---
Sometimes you need to preload a whole video before displaying it. Maybe you will use it as a transition, maybe it's integrated into the user interface(it's part of a menu, for example). Because videos must be attached to Video instances, you need to have you movie clip hierarchy in place so you can attach the NetStream and load it. This imposes too many restraints on how you must have your clips setup (and instantiated) before loading.

It's pretty obvious, but it took me a while to figure this one out: you don't need a Video instance to preload videos. For example, suppose you have a menu with three items and a video to play for each. No need to keep different videos on stage. You can preload the stream directly. It's so simple in fact that there's barely code to show.

  main_conn = new NetConnection();
  main_conn.connect(null);

  main_stream = new NetStream(main_conn);
  main_stream.play(url);

From there you can control loading easely through main_stream.bytesTotal and main_stream.bytesLoaded. When you need to play that video, just attch the NetStream to it:`video.attachVideo(main_stream);`

As an added bonus, after playing your video, you can get rid of your Video instance (remove from the stage) and change the movie clip hierarchy as you see fit. Later on, just attach another Video instance and call `video.attachVideo(main_stream);` on it, and voilá, you can safely keep you preloaded stream, with two caveats:

* You'll be keeping the whole stream in memory, so this will work better for smaller videos (You don't want to waste your user's memory preloading large videos)
* You don't call <span class="code">close()</span> on the NeStream, if you do, it will be gone from memory.

The same trick works for AS3 too. Even though with the `URLLoader` you could always use the raw data as cast it to a NetStream, it's pretty handy.