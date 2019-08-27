# Programming on gnu linux

created: 2012-12-15 00:00:00

This page talk about some general programming on a `GNU/Linux box`. Setting up a working development environment. Talking about the required toys to play. Take also a look to the other programming related pages.

The content of this page is mainly based on the old book `Linux Programming Unleased` and this page content should be modified before releasing.

# Introduction

There may many reason to program on a `GNU/Linux` box as that many to program on a `Microsoft Windows` box.

# GNU cc

`GNU cc` is know as `gcc`.

Take also a look to the `gcc-doc` package.

A little example:

    /*
     * Listing 3.1
     * hell.c - Canonical "Hello, world!" program 4    4 */
    #include <stdio.h>
    int main(void)
    {
        fprintf(stdout, "Hello, Linux programming world!\n");
        return 0;
    }

And compile it with:

    gcc hello.c -o hello

Now run us custom application:

    ./hello

and that will output:

    Hello, Linux programming world!

# Make

    make clean
    make
    make -n install     # See what it would do first
    make install
