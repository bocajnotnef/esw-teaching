#! /usr/bin/env python3

#
# Hey! You're reading my python program! Cool!
# This stuff with #'s at the front, these are called 'comments'
# Comments aren't 'seen' by the interpreter, so they don't
# affect how your program runs, but they're useful to leave
# notes in the code about how something runs.
#


# 'import' gets code that's useful for other things, but that
# you might not always need, and adds it to your program.
# I'll explain them more later, just ignore them for now
import time

# here, I'm assigning a gigantic string to the variable 'intro'
intro = """
Hello!

Welcome to Jake's Really Probably Terrible Intro to Python!

I'm going to attempt to roll the tutorials into actual
python files like this one so that you can both run
the code and interact with things.

Much of how I learned programming (and even still do) is by
looking at how programs behave by running them and then
looking at the code and messing with it.

Plus, this way I can give you examples and then you can see
how they work right in the interpreter.

>>> Press enter to continue. <<<
"""

# now I'm outputting 'intro'
print(intro)

# this doesn't really do anything, it just stops the program
# until you hit enter.
x = input()

lesson_0_1 = """
So in programming one of the first things you have to learn is
the concept of a 'variable.' A variable is basically a box with a
name that we put stuff in. You make a variable (in python) like this:

    some_name = 12

Now the variable "some_name" is a box that contains the number 12.
If we do something like this:

    some_string = "100"

The variable "some_string" contains the string "100". A string is a bunch
of letters. There is a big difference between "100" and 100--one is the
'letters' for one, zero, zero, and one is the value one hundred.

>>> Press enter to continue. <<<
"""

print(lesson_0_1)

# Goes Nowhere, Does Nothing
x = input()

lesson_0_2 = """
That may seem tricky right now, but you'll get the hang of it down the line.
An easy way to test it is to do something like:

    num = 700
    num = num + 5

Python will give you an error:

    TypeError: cannot concatenate 'str' and 'int' objects

What this means is that it tried to "+" a string and a number, which doesn't
make sense.

Get used to seeing errors---they happen a lot in programming.

>>> Press enter to continue. <<<
"""

print(lesson_0_2)
x = input()


lesson_0_3 = """
Well that's quite enough of me talking for now, I think.

I'm going to give you a set of prompts that'll ask you for some input,
and then try to do an action on it.

Feel free to try to break it--heck, that's what it's for.

>>> Press enter to continue <<<
"""

print(lesson_0_3)


# now things get a little more complicated
"""
Hey look! A string that isn't being assigned to anything!

You can totally do this if you have a really long comment and you
don't feel like writing #'s at the start of your lines every time.

So, what's below is called a 'while loop.'
While loops are a control structure. Control structures are super important.

Control structures let your code make decisions--to do a certian thing, or
not, depending on some condition.

Here's the super basic syntax of a while loop:

    while(this condition is true):
        do this stuff

    afterwards, do this stuff

Here, the condition of the while is that the variable 'counter' is less than
three.
"""

counter = 0

while(counter < 3):
    print("Iteration {} out of 3".format(counter))

    print("Please give me a number: ", end="")
    x = input()
    print("You gave me {}".format(x))
    print("I will now add 7 to {}".format(x))

    # predeclare this box so we can get to it later
    plus7 = None

    """
    The following structure is called a try-except block.

    Try-excepts are used when you think your code may have an error
    and you don't want it to crash.

    They're fairly complex, so let's just ignore them for now.
    """
    try:
        plus7 = 7 + int(x)
        print("Good! Result: {}".format(plus7), end="\n\n")
        time.sleep(3)
    except Exception as err:
        print("You broke it!")
        print("The error follows:")
        print(err, end="\n\n")
        time.sleep(3)

    # this line is super important!
    # remember how our while loop is waiting for counter
    # to get bigger than three, before it stops running?
    # if we never add anything to counter, it will never get bigger
    # and then our program will never stop.
    # very bad!
    counter += 1


lesson_0_4 = """
Wasn't that fun?

You may have seen a slightly different error, one that looks like:

    invalid literal for int() with base 10:

That happened because of how I processed your input. See, what I did was:

    x = input()

Which basically says "Get some input from the user, then put it in the
box labled x". Then I did:

    int(x)

Which says "Go and get the box labled x and convert whatever is inside of it
to an integer."

(Side note: an integer is just a whole number, like -2, -1, 0, 1, 2, etc).

If x contains something like 'w', then "convert w to an integer" doesn't
make any sense. That error is just python complaining at you.

>>> Press enter to continue <<<
"""

print(lesson_0_4)

# GNDN
x = input()

lesson_0_5 = """
Good stuff. Now, I'm gonna leave you there so you can ponder the usefulness
of variables.

I highly recommend you open the interpreter ("python3" on the command line,
remember?) and just fiddle about with them for a bit.

Also, crack open this file and take a look at what's inside. You can
get a feel for how things work by looking at how these tutorials are built.

You can also mess about with what's here to try and get a feel for how things
work. Just open this file up in IDLE or something.

Remember, most of learning programming is breaking stuff and trying to put
it back together in a different way.

I expect you to do a lot of learning by fiddling around with your own stuff
and by cracking open these files to take a look at how they work.

Cheers!
"""
