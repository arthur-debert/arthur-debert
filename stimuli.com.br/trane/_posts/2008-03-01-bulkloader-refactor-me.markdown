---
layout: post
title: "BulkLoader :: Refactor me"
permalink: "/trane/2008/mar/01/bulkloader-refactor-me/"
tags: [actionscript design bulk-loader]
categories: [trane]
legacy_id: 24
date: "2008-03-01 -0300"
---
After BulkLoader was made public in November 2007, it really took of. From about 3 downloads a week, to around 30 daily, since November, totaling over 3 thousand downloads in about three months.

For me this came out as a big surprise. I'd expect coworkers at [Gringo](http://www.gringo.nu/) to use it, and maybe a few others, but I've never thought it would be that many.

Usage numbers are much harder to guess though, since most hackers would rather checkout from svn, and of course, the majority of people will download it, take a 20 seconds look and leave it at that.

Still, from the mailing list, email exchange and blog posts, I can see that there's a few programmers using it. This is a great reward. 

Turns out, releasing BulkLoader was much, much more work than I'd figure. Documenting, replying to comments, wiki and general maintenance are many times more time consuming than coding actually. It's been a great exercise in learning how to communicate, write docs, and making sure that BulkLoader will help users getting work done.

When users started to write about it, I realized that there were far more use cases than I had planned for, and it showed. Many thoughtful feature requests came, bug reports. Also more than one person struggle with the same issue made it clear that the docs were either lacking, or that feature behave in a hard to grok manner. 

As I started to push more and more updates, and many times, hacking features that were not in my regular usage pattern, sometimes I'd push broken updates, or sometimes break something that used to work. 

##  The types mess
Somewhere in January, I realized that there were  problems with the way BulkLoader was programmed. One was that, for various reasons, it was necessary to specify the type of an item being added (images, videos, text files, etc), because that would map to internal details regarding how to load them (NetStreams, Sound objects, Loader object and so forth). But I made a deep mess, confusing file extension, mime types and the classes used in BulkLoader to load them. The end result was a big mess of the "types" system, where it was very complex to change, or and understand that part of the code. This also impacted users heavily since types were used from the outside as well.

## The anti OO, conditionals spread all over the place
The other issue, is that I always intend to not expose the LoadingItem instances, to keep them internal. It turns out, that it wasn't possible to do that, not without restricting some very fair needs. So with time, people would use more and more of LoadingItem objects directly. But LoadingItem was crafted hack after hack, the antithesis of Object Orientation, full of conditionals for each loading type. [This thread](http://groups.google.com/group/bulkloader-users/browse_frm/thread/d9a5872c790b3ad3#) laid the plan.

## Change but don't break
I wanted to get a major refactor done: properly create a class structure for LoadingItems and also clean up the whole types-are-extensions-and-classes mess. But there were so many people using it, and I didn't want to break things too much. I needed to go into that large refactor, with some assurance that most stuff would simply work: a needed a test suite. I started a new svn branch, the li-refactor branch, and have been hacking on it when time allows for the last month.

## Testing is hard: let's go shopping!
I've used some Unit Testing in the past, but very little. Either toy examples for studding, or reading it like documentation. BulkLoader is hard to test. Most features are asynchronous, and very little of the code is reentrant. Also, because it is a singleton of sorts (not really, but all instances are kept in memory) it made it testing hell.

I chose to go with [ASUnit](http://www.asunit.org/), mostly because it looked less tied up to flex libraries and Flex Builder. BulkLoader is now proud to have over 170 test. I am pretty sure that there are more to come, but it is a great start. I've decided to keep test out of the main zip download, since most people will never need to touch those, but they are in the svn rep. I've kept a copy of ASUnit as well, since I had to patch it a bit to make testing for BulkLoader easier, mostly making sure that tests would run in a serial fashion, and not in parallel (because if it keeping all instances in memory, it made a mess). 

Tests got many, many bugs that were lurking around. It's really impressive how useful they are. There is so much to gain in understanding, how things work, and what in the design promotes bad coupling. This is first real test suite I wrote, and I am sure I've made a lot of mistakes in it. But never the less, it has taught me a lot, on testing, BulkLoader design in general, and more importantly, gave me the confidence for a large, much needed refactor.

## Breaking backwards compatibility
As much as I wished I didn't have too, some backwards compatibility was broken. Fixing the issues above implied in changing a few details, and since BulkLoader is such a young project, I am glad I have done so. 

## Avoiding bloat
One of the hardest issues with a public project is saying no to feature requests. Most are very sensible, and it is a natural impulse to just go ahead and implement them. But BulkLoader has become very large, borderline bloated for a project of it's scope. So unless something incredibly useful comes out, I am freezing new features and calling this merge a release candidate. I'll do a couple more of bug fixes releases and then called it a 1.0 day.

## And many thanks
To all users who provided bug reports, feature requests and just general feedback. Those contributions are invaluable, and it is very rewarding seeing users begin more productive, doing less grunt work. 

For a full list of changes:
[mailing list thread](http://groups.google.com/group/bulkloader-users/browse_frm/thread/9320421e58b7bd17) for the whole shebang.