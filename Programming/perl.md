# Perl

created: 2012-12-15 00:00:00

This article talk about Perl programming.

# Playing with Perl in the interpreter

Open a shell and type `perl`. You are then in the `Perl` interpreter.

Type whatever you want and then `ctrl+d` to execute the statements.

# Let's Play with the interpreter

    $myVar = 'Hello world\n';
    print $myVar;
    $myVar = "Hello world\n";
    print $myVar;

That output:

    Hello world\nHello world

Some aritmetric stuff:

    $a = 7;
    $b = 3;
    print $a + $b . "\n";
    print $a - $b . "\n";
    print $a * $b . "\n";
    print $a / $b . "\n";
    print $a ** $b . "\n";
    print $a % $b . "\n";

That output:

    10
    4
    21
    2.33333333333333
    343
    1

# Creating a Perl script

A Perl script is the same code you have enter in the interpreter. Because of the interpreter lose the code you have entered each time you quit it, you want probably write down some code i a file and execute that file.

The classic Hello world program:

    #!/usr/bin/perl
    print "Hello, World!\n";

The first line is the shebang. The path of the `perl` interpreter on the `unix`like like box. You can know where your `perl` interpreter is located with the command 'whereis perl'.

Make the script executable for everyone:

    chmod +x myScript.pl

Then you can execute the script without specifying the program. Like we can execute it with 'perl myScript.pl'. We can also rename it so that the script have no more a extension.

# If

    $a = 7;
    $b = 3;
    if ($a > $b) {
        print "$a is greater than b\n";
    }

That output:

    7 is greater than 3
    $a = 7;
    $b = 3;
    if ($b > $a) {
        print "$b is greater than $a\n";
    } else {
        print "$b is not more than $a\n";
    }

Output :

    3 is not more than 7
    $a = 7;
    $b = 3;
    unless ($b > $a) {
        print "$b is not more than $a\n";
    }
    $a = 7;
    $b = 3;
    unless ($a > $b) {
        print "$a is not more than $b\n";
    } else {
        print "$a is more than $b\n";
    }

Output:

    7 is more than 3
    print "$a is greater than $b\n" if ($a > $b)";
    print "$b is not more thatn $a\n" unless ($b > $a);

output:

    7 is more than 3
    3 is not more than 7

# Arrays

    @array = (1, 2, 3, 4, 5);
    foreach $number (@array) {
        print "$number\n";
    }

Making an array with a little range trick:

    @array = (1 .. 5);
    foreach $number (@array) {
        print "$number\n";
    }
    @array = (1 .. 5, 7 .. 10 );
    foreach $number (@array) {
        print "$number\n";
    }

That output:

    1
    2
    3
    4
    5
    7
    8
    9

10

    foreach $number (1 .. 5) {
        next if ($number == 3);
        print "$number\n";
    }

That output:

    1
    2
    4
    5
    foreach $number (1 .. 10 ) {
        last if ($number == 7);
        print "$number\n";
    }

That output:

    1
    2
    3
    4
    5
    6

# Resources

*   Nice Perl movie introductions: [http://showmedo.com/videos/series?name=perlDevijverPerlIntroSeries](http://showmedo.com/videos/series?name=perlDevijverPerlIntroSeries)