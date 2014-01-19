---
layout: post
title: "Email validation in Actionscript 3"
permalink: "/trane/2007/sep/13/email-validation-actionscript-3/"
tags: [actionscript as3 email flex]
categories: [posts]
id: 18
date: "2007-09-13 -0300"
---
I've been playing with flex lately and I though the best way to get the hang of it was to use it in small pieces. One of the most obvious places for using the flex framework seemed form validation. Since it is **enterprise** ready, validation must be top notch. And then I stumbled upon the monstrous 500+ lines of code mx.validators.EmailValidator class. Sure, it's doing a lot more than checking if a String is a valid email address. It will tell you if there is too litle at signs, too many at signs, and many other possible combination of invalid email addresses. 

Wow! This is such a case of over engineering! If someone is typing a email addresses on a form, they probably know what it looks like. I've never seen such detailed error messages, and honestly, that's a good thing. Using the EmailValidator from flex will weight 6kb of sources. If it's that complex it sure will do a great job at validating emails, you'd think. But shockingly, the email validation is a great hack: no regex just a bunch of string searches such as:
<code>
var ampPos:int = emailStr.indexOf("@");
if (ampPos == -1)
</code>
And so forth. Ouch! Regexes can be daunting and intimidating, but sometimes avoiding a regex will cause a lot more trouble that it will save you. This is an invalid email address, according to the flex validator: "arthur+latenight@somedomain.com". Not only plus signs are legal at the address part, but they're very useful. If your mail server is configured correctly (and unfortunately many aren't) and you have an email account such as "arthur@somedomain.com", then you can use many variations of "arthur+a.web.store@somedomain.com" and still get those delivered to you. This is great for checking if a company has passed your personal information to others, or generating automated rules for filtering or forwarding. Gmail allows that, and I use it all the time.

Getting email validation right is tough. Zeh couldn't get his email to be [accepted in so many places he had to change](http://labs.zeh.com.br/blog/?p=70) it. The [spec](http://tools.ietf.org/html/rfc2822#section-3.4.1) allows many variations such as: arthur'@'debert@somedomain.com and other bizarre cases. You don't have to allow them all, but you should definitely allow for the most common ones. Flex, being a framework for client side programming, should really do a better job at validating emails. 

In the end you have a heavy, tightly coupled framework that deals with really edge cases (such as warning a user that his email has too many at signs!) but not taking enough care to validate emails correctly.

I've hacked an EmailValidator class that is much more light weight and hopefully gets most emails right. You can [download it here](http://media.stimuli.com.br:8080/media/misc/downloads/email-validation.zip). Sample usage below:

<code>
/* http://www.stimuli.com.br/, Arthur Debert
*/
package br.com.stimuli.mona.validators{
    /*// usage
    * import br.com.stimuli.mona.validators.EmailValidator;
    * 
    * // will return a boolean
    * EmailValidator.isValidEmail("someone@someplace.com");
    * 
    * // if you'd rather validate an catch an error you can use:
    * EmailValidator.validate("someone@someplace.com");
    * 
    * // You can also specify which class you;d rather throw an error in case the email isn't valid:
    * EmailValidator.validate("bad@email@someplace.com", MyErrorClass);
    * 
    * // You can also specify the message to be passed to the error class
    * EmailValidator.validate("bad@email@someplace.com", Error, "Bad email!");
    * 
    * // If you have an input where people can type a few email addresses you can validate a whole list
    * // This will separate and trim each word of text:
    * EmailValidator.isValidEmailList("someone@someplace.com, afriend@otherplace.com");
    * 
    * // If you specify an arbitrary separator to test. This will return true:
    * EmailValidator.isValidEmailList("someone@someplace.com; afriend@otherplace.com ", ";");
    * // But using the default (",") separator, this will return false:
    * EmailValidator.isValidEmailList("someone@someplace.com; afriend@otherplace.com ",);
    */
    public class EmailValidator{

        public function EmailValidator() {
            throw new Error("The EmailValidator class is not intended to be instantiated.");
        }
        
        // permissive, will allow quite a few non matching email addresses
        public static const EMAIL_REGEX : RegExp = /^[A-Z0-9._%+-]+@(?:[A-Z0-9-]+\.)+[A-Z]{2,4}$/i;

        /** Checks if the given string is a valid email address.
        *  @param email The email address as a String
        *  @return True if the given string is a valid email address, false otherwise.
        */
        public static function isValidEmail(email : String) : Boolean{
            return Boolean(email.match(EMAIL_REGEX));
        }
        
        /* Splits a string with the separator character, strips white characters and checks if all of them are valid
        */
        public static function isValidEmailList(emailList : String, separator : String = ",") : Boolean{
            var addresses : Array = emailList.split(separator);
            for each (var email : String in addresses){
                if (!isValidEmail(email.replace(/\s/, "")))return false;
            }
            return true;
        }
        
        public static function validate(email : String, errorClass : Class = null, errorMessage : String = "Invalid e-mail address.") : void{
            if (isValidEmail(email) )return;
            errorClass = errorClass || Error;
            throw new errorClass(errorMessage)
        }
    }
}</code>

If you catch valid emails that this regex is complaining about, please let me know.
you can also get the full scoop on the nitty gritty of email validation [here](http://www.regular-expressions.info/email.html).