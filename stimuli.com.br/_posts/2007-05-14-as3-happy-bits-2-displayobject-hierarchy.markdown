---
layout: post
title: "AS3 Happy bits #2: The DisplayObject Hierarchy "
permalink: "/trane/2007/may/14/as3-happy-bits-2-displayobject-hierarchy/"
tags: [as2 actionscript as3]
categories: [posts]
id: 12
date: "2007-05-14 -0300"
---
Flash, like most interesting programs has developed organically, out living by far the sort of "low file size gif replacement" it began it's life as. Also, like many successful platforms (windows more than anything else) it takes backwards compatibility very seriously. I find it really incredible that to this day I can use flash 9 to export Flash 1 version swfs. More incredible still, the flash 9 plugin can read those files flawlessly. This means that content produced in 1996 is still readable as is. 

The downside to it, is that in the struggle to make backwards compatibility feasible, many short sighted decisions have lingered on, from version to the next. The flash API, up to flash 8 is some sort of fransktein. We use to joke at work that some core members of the API have been implemented by trainees, without any access to the current API. It's just awful. At the heart of the API is the **MovieClip** class. Since flash is a visual and interactive platform the **MovieClip**, complex objects that can hold graphics, sounds and code the class flash developers work the most with. Yet, it's interface makes no sense:
<code  class="actionscript">
// creating a movie clip:
var mc : MovieClip = createEmptyMovieClip("ball", 1);
// do we really need "create" here, do we say things such as
var obj = createEmptyObject();
// ?
// we are just creating it, it should be empty!
  
// now attaching from the library
var mc2 : MovieClip = attachMovie("id", name, depth);
// why do we sometimes have to say MovieClip and sometimes just Movie will do?
  
// removing a movie clip:
mc2.removeMovieClip();
// wouldn't just 'remove' suffice?

</code>
Besides the inconsistency with method names, how about not making use of a powerful AS feature: variable length of parameters? Why not having the createEmpty**MovieClip**() accept only a name, and in that case using the next highest depth available. How about assigning some place holder name in case the first parameter is null? This seems a bit wacky, but that's exactly what the IDE does with clips on the timeline. 

There are lots of nonsense points to the API, no point in beating a dead horse. So when flash 9 (flex actually) announced a new version of AS, with a completely new virtual machine and API, it gave macromedia team the chance to drop the historical artifacts of the API and begin a fresh one. 

So AS3 finally gave us a sane display list. The class hierarchy makes sense, with each subclass extending the one above it, with a clear use case and extra features. The display list can be manipulated consistently with the node related methods such as addChild, addChildAt and so forth. Value ranges have been changed to be one based (1-> 100% scale, alpha), making it more intuitive to apply ratios and general calculations. The underscore prefixed to items' properties has been removed (why were they made to "look" like private: _alpha, _xscale, etc). Long standing issues such as getting the list of available frame labels on a **MovieClip** are now possible (I have no idea why this one wasn't implemented before: the runtime had to know the labels available). 

My favorite feature though, is that the display list is a real node tree, and now you can move objects between nodes. This used be a big headache in earlier versions. You had to be very careful with the way you build the **MovieClip** hierarchy, because once it was setup you couldn't move things around. Preloading images and swfs had be done with the hierarchy in place, and that also made up a lot of grunt work. 

Not being able to remove a **MovieClip** off the stage without "killing" the **MovieClip** included a few hacks as well: setting things off stage, alpha set to 0 and _visible to false. 

Now not only you can set masks, but you can also check if a clip is masked, and by whom (what could be the reason behind having a write only property?). Better yet, mask don't have to share the same parents, a "feature" that made a masking a lot more complicated: when "cleaning up" some clips you'd have to remove **MovieClip** higher on the tree and keep track of that yourself, since it was a write-only property.

The stage is finally well represented by a singleton class, instead of a holder of static properties. 

Drawing on **MovieClip**s is decuppled from the DisplayObject itself, into a Graphics object, and has a reasonable API. Most notably the convinience methods of drawRect and friends.

Loading information has been moved to an aproppriate object, the LoaderInfo, so now the place to check urls, bytes size and so forth are in a different place than drawing code, for example.

When one looks at the new the DisplayObejct hiererchy, it becomes clear how much the old API sucked. There were no separation of responsibilities, at a quick glance, what was the **MovieClip** class now is spread out through at least 6 other classes:

- *LoaderInfo*: information regarding loading , urls, events and so forth,
- *Loader*: used to load new DisplayObjects
- *FrameLabel*
- *InteractiveObject*: holding events and properties such as contextMenu, tabIndex.
- *Graphics*: used for drawing.
- *Stage*: a singleton that holds "global" properties for the display list.

The display package is a very welcome change. It fixed a lot of bad design decisions that flash took over those 10 years and created a logical and powerful way to manipulate visual objects which is, afterall, the whole point in using flash. I for one won't be looking back.