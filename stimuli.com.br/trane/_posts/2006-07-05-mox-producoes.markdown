---
layout: post
title: "Mox Produções"
permalink: "/works/mox-producoes"
tags: []
categories: [works]
id: 10
date: "2006-07-05 -0300"
---
Portfolio website for video production company, Mox Produções.

The idea was to present a really simple navigation showcasing the company's main areas like stripes that will open up to reveal themselves. With a blocky, staccato look and feel design by [Lucia Dossin](http://www.fiveblackcats.com) the website achieves an almost retro look.

The navigation between jobs is thoughtful and fun. Extensive use of masking and an infinite scroll suggest a long line of films passing by the viewer. Some tricks had to be applied in order to allow for the same image to be visible in more that one frame as if they were stitched together while they aren't. While it looks like you're seeing the same film strip simply sliding, each frame contains a full strip, and they are carefully animated so the look as one.This piece taught me a few rough corners with BitmapData's in actionscript. As the number of pieces grow, the filmstrips have to be broken upon a few movie clips, since flash can't handle Bitmaps larger than 2880 pixels in any dimension.

The site is fully editable by the administration application, built with django. Since reads are way more common that writes, the back-end outputs xml files that feed the front end, therfore avoiding many unnecessary db queries. 