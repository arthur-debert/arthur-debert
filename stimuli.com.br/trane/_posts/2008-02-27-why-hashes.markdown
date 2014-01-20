---
layout: post
title: "Why Hashes?"
permalink: "/trane/2008/feb/27/why-hashes/"
tags: [actionscript design]
categories: [trane]
legacy_id: 23
date: "2008-02-27 -0300"
---
Every now and then I have to defend the use of hashes in parameters. Usually it is a side issue to something else, and I try to explain my position in 6 words or less, and it ends up sounding like insult or non sense. So today I am writing this so I can provide a link between parenthesis and carry on with the subject in hand. 

Using hashes to collect parameters to functions gives the impression that I think they are great, but in fact, I don't: it's a poor solution to a very specific problem. It's a work around a language deficiency, mostly because Actionscript's lack of a proper abstraction for this particular situation.

##What problem does it solve?
Sometimes you have a method or a function that is very parametrized, you want to control it's behavior with a many parameters, and many have a default, sensible value, your don't need to specify them most of the time. Also, you might want to add features to your method in the near future, you want it to remain flexible. 

The core issue here, is flexibility. Actionscript has a few features that take you 80% of the way, but sometimes it leaves you 20% off.

## Default parameters:
Let's say you have a method that plays sounds on the library, by some id which is string. Then, you always have to specify the id.

    public function playSound(soundID : String){
     	//...
    };

All is well, but you want to be able to control the volume each sound is playing. Maybe all sounds are not properly equalized, or the user has a volume knob he can set at run time. Most of the time, a volume of 1 is appropriate, but a few sounds are way to loud, and you need to tone it down a bit. But still, usually the volume of 1 will do it, and also you don't want to break backwards compatibility with all the working code you've written. Default parameters solve both issues:

    public function playSound(soundID : String, volume : Number = 1){
     	//...
    };

All working code will keep working. Since you usually want the volume to be 1, this won't make you type more on most calls, but for that few sounds that were recorded to loud, you can just say:

    playSound("rollover", 0,5);

In the end you get flexibility, both in terms of code you've already written and code you will write. There is no overhead of breaking things, creating a new function or having to educate users. Flexibility is one of the touchstones of well written software.

## Variable number of parameters:
In AS3 you can signal that you are expecting an unknown number of parameters with a "...". Say you've got a function that adds to numbers:

    function addNumbers(a : Number, b:Number) : Number{
       return a + b
    }

Now you need a function that can add 3 numbers. What do you do, create another function that can add 3 numbers?

    function addThreeNumbers(a : Number, b : Number, c: Number) : Number{
    	return a + b + c;
    }

That's ugly, and not very flexible, what if next week you run into the need of adding 5 numbers? Will you create a method call addFiveNumbers ?
The solution for this, is to create a function that works with any amount of parameters:

    function addNumbers(numbers...) : Void{
    	var result : Number = 0;
    	for(var i : int = 0; i < numbers.length; i++){
    		result += numbers[i]
    	}
    	return result;
    }
    
Now you can deal with any number of parameters. Your function is very flexible. Old code will still work unmodified, new cases can be dealt with. Flexibility is good.

But having functions with an unknown number of parameters work well when all possible arguments are of the same type and will usually be processed in a loop, such as the example above.

But suppose you'd try that on the playSound above, but now defining if the sound will loop, something like:

    function playSound(args...) : void{
       var soundId : String = args[0];
       var volume : Number = args[1] || 1;
       var loops : Boolean = args[2] || false;
    }

This is still flexible, but it is not very maintainable. Lot's of extra typing, and worse, now the arguments are tied to the order of the args parameter. Unless the order of items has any meaning, or doesn't mean anything at all (such as when adding numbers), the functionality will depend on an opaque, hidden and unrelated information. So if you want a sound to loop with the default value, you have to say:

    playSound("rollover", null, true);

But if you then add other features (such as panning, or callbacks) you might simply end up with some case where you need to specify the 6th parameter but not the ones in the middle, now it is just horrible:

    playSound("rollover", null, false, null, null, onDone )

It's too easy to err and forget. Sometimes you would pass null, others false... it's a lot of typing. All in one a very bad solution.

The core problem here, is that parameter passing, both with named parameters and also collapsing parameters into an args... array will make the logic depend on the order, and doesn't let you mark things as optional. You only want to define the first and 7th option, not anything else. You shouldn't have to remember long list of parameters and their correct order. 

## Standard Java solution: create an object for holding an specific set of properties.
This is how you'd do it in Java, create a SoundPlayProperties object that does nothing. Then you can say:

    var soundProperties : SoundPlayProperties = new SoundPlayProperties("rollover");
    soundProperties.loops = true;
    playSound(soundProperties);

I'll get my self covered saying this is just a matter of taste. Some people like that better. But this is the standard excuse for not sticking to an opinion. I don't like the above solution. It is not elegant, it is verbose, it imposes a higher learning curve. Main issues with it:

* Complexity: the minimum number of tokens for this is 3, one for function call, another for the id, and other for the looping. The above code has 11 That's way, way too many.
* Overhead: now, you added another class, just to define options to a method. Users will no longer be able to find out how the method works by just reading the method signature, or the documentation to that method. Users will (I least I do) check out the modules for a library I am using. If a very simple library takes 30 classes, it really scares me. 
* Performance overhead: now, besides the method call you are creating an object.
* Moral high ground: without trying to go overboard on over stretching the implications of a simple choice, or turning into a flamewar of Java doesn't know what object orientation is. But an object is useful mostly for defining state and behavior, not just as a property list that doesn't do anything.
* Users expect to change the SoundPlayProperties objects later on, and have that change reflect on the playSound method.

Its a long rambling just to say it rubs me the wrong way, no I don't like it.

## Hashes:
Passing those options as hash keys, like this:
    playSound("rollover", {loops:true});
Provide a few advantages:

* Order doesn't matter any more
* Very readable, you can see exactly what that call means, with very few superfluous tokens (just the "{}").
* You can choose to specify as many, or as few options as you like.
* If in he future you decide to add another option, you are not breaking anyones code or habit.
* Makes it very clear that those options will be used in the playSound method, and not later.

A few disadvantages remain though: 

* An extra object creation ( performance overhead).
* No static typing, if you make a type it won't let you know, and while you can document the options on one place (the method doc).
* Tt's not very discoverable.

In the end, it's just a hack, a work around, but right now, it feels to be the make fewer compromises. Most of the time, you either wish to create objects really, or have a small number of parameters, but sometimes you don't.

## The ideal solution
Is to have a language with the right feature, like python has, which is to have optional named parameters, that won't depend on evocation order, so in this case, you can say:

    function playSound(soundID : String /* obligatory */, volume: Number=1, rightPanning: Number=1, leftPanning: Number=1, loops : Boolean=true, onCompleteCallBack : Function = null) : void{

    }

This will give you a lot of flexibility, creates no overhead, is very readable, and doesn't force the user to learn another class. You can specify as many options as you need, in any order you need, and keep it readable. You could say:

    playSound("rollover", loops=true);
    // or
    playSound("rollover", onCompleteCallBack=doSomething);
    // or many otions:
    playSound("rollover", loops=true, onCompleteCallBack=doSomething, volume=0.5);


This post was a bit longer than I expected, but I was tired of trying to squeeze all this info inside a one liner in a forum thread.