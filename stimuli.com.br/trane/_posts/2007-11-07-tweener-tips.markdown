---
layout: post
title: "Tweener Tips"
permalink: "/trane/2007/nov/07/tweener-tips/"
tags: [tweener actionscript]
categories: [posts]
id: 20
date: "2007-11-07 -0300"
---
I've been using [Tweener](http://code.google.com/p/tweener/) for almost an year now, and I thought I'd share a few quick and useful tips.

## Delayed Function call, or a Poor man's timer
AS3 has the Timer class which is handy, but sometimes you just need a quick "call this function in x seconds". No need to instantiate an object, keep its reference, add event listeners, a function and clear up the timer. This is so simple (and great):

    Tweener.addTween(this, {time:0.3, onComplete: myFunction});

Or, using an anonymous function:

    Tweener.addTween(this, {time:0.3, onComplete: function():void{
    	// do something here!
    	trace("hello");
    });

Note that you don't have to tween any property at all for this to work. Just specify any object as the target, the time in seconds you wish to wait until the function is called and which function to call.

## Using "base" as a template for Tweens
Some animations / visual effects are used many times over in the same project. Using the base property you can create a "template" of a tween and specialize it later (like adding an onComplete callback for some runs of the effect). Suppose  you have a recurring tween that scale items and does a fade. You can say:

    // creates a "template" to be used more than once:
    var scaleFadeIn : Object = {
    	alpha:1,
    	_scale:1,
    	time:0.5,
    	transition: "linear"
    }
    // later in you code you can say:
    Tweener.addTween(myMovieClip, {base:scaleFadeIn});
    // or you can "enhance it", for example with an onComplete callback:
    Tweener.addTween(myMovieClip, {base:scaleFadeIn, onComplete: callHome});

The great thing about this is easier maintenance. If you later on decide that you want to try another transition or time, you only change the template, the "base" for those Tweens.

Note that base is very flexible, as they can be nested:

    var scaleAndColorFadeIn : Object = {
    	base: scaleFadeIn,
    	_color: 0xFF0000
    }

In this case, you "add" all settings from the scaleFadeIn and the scaleAndColorFadeIn. More on the [base property documentation page](http://hosted.zeh.com.br/tweener/docs/en-us/).

## Using setTimeScale to speed up testing
This is a real life saver. Tweener uses a sort of internal clock, a value by which all time operations are measured, called timeScale. Sometimes you are coding some section of the website, but to get there you have to see the loading animations, menu transitions and so on. Because you are seeing this over and over again, those precious seconds until you get to the part that really interests you is very boring, so you can "fast forward" them.
At the beginning of your website you can just say:

    // this will run everything 3 times as fast
    Tweener.timeScale(3);

Once you've reached the section / part of the website that you are actually working on, you can just set the speed back to normal:

    // this will set the speed back to normal
    Tweener.setTimeScale( 1);

Another use for this is when you want to see your animations in "slow motion". Setting time scale will allow the rhythm to be the same, you're just slowing down the tempo, maybe you are interested in looking how a blur really looks or if some items are overlapping.
