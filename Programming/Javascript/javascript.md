# Javascript

## Introduction

JavaScript needs to be embedded into HTML code. Like with pure HTML code, the pages you made will not be dynamic. With javascript you can make it dynamic.

JavaScript is made by Netscape and was called LiveScript at that time. Near 1995 Sun (the authors of Java) adopted it as open standard for the Internet and have call it JavaScript. Since Sun has adopted JavaScript, many other companies adopted JavaScript like for example America Online, Apple, Borland and Oracle ...

Microsoft made also his own implementation and called it JScript.

The JavaScript was made to be run client side. There is also a JavaScript implementation for server side.

When you write some JavaScript code, always test it with different browsers!

You should need to embed JavaScript code in HTML documents. In the first examples, we show some complete code examples with HTML code. But further we remove all the HTML code for some basic examples, to avoid that the examples will be are to long. But if we need to be are clear, we add the HTML tags too.

## The traditional 'Hello, world!' program

```html
<html>
<head>
  <title>Some test with JavaScript</title>
</head>
<body>
<h1>'Hello, world!' Test:</h1>
<p>This is the traditional 'Hello, world!' script.</p>

<script>
document.write("Hello, world!")
</script>

</body>
</html>
```

Little example to print the content of a variable:

```javascript
<script>
msg = "Hello, world!"
document.write(msg)
</script>
```

**Note: In the second example, we don\'t make use of quote in the write function. Like it is not a string constant but a reference to a variable.**

These 2 little examples will work very well with decent browsers. But a problem will raise if we use an older browsers. Like every browser that does not understand a tag, will ignore it. That means that the tag `<script>` and `</script>` will be removed and only the text line `document.write(msg)` will be showed. That's probably not what we want. To avoid it, we should add the following:

```javascript
<script>
<!-- This next one will be hidden for not compatible browsers
document.write("Hello, world!<br>")
// End hidden for non-compatible browsers -->
</script>
```

Like you see, there is a comment line that you probably recognize.

## Embed the JavaScript to your HTML code

Specifies JavaScript for Navigator 2.0.

```html
<script language="JavaScript" type="text/javascript">
```

Specifies JavaScript for Navigator 3.0

```html
<script language="JavaScript1.1" type="text/javascript">
```

## Save code in an external file and import it

```html
<head>
  <title>My Page</title>
  <script src="/virtual_hosts/joomla_dvanmosselbeen.be/common.js">
  ...
  </script>
</head>
<body>
...
```
    
## Display a message if a client does not support JavaScript

```html
<noscript>
<b>This page uses JavaScript, so you need to get Netscape Navigator 2.0
or later!</b>
<br>
<a href="http://home.netscape.com/comprod/mirror/index.html">
<img src="/virtual_hosts/joomla_dvanmosselbeen.be/NSNow.gif"></a>
If you are using Navigator 2.0 or later, and you see this message,
you should enable JavaScript by choosing Network Preferences from
the Options menu.
</noscript>
```

## Document your code with comments

You can add comments to your code to comment your code. It will be really useful to add the right comments on the right place. It will help you when you come back to your piece of code some time later. But also to give some comments to the person who read your code too.

A single line comment is as following:

```javascript
  // Print heading
  document.write("<h1>This is a heading</h1>");
```

A multi line comment is as following:

```javascript
/* Print a heading and
then print a paragraph
*/
document.write("<h1>This is a heading</h1>");
document.write("<p>This is a paragraph.</p>");
```

Another more useful example:

```javascript
/**
 * Print message
 * @param {String} a message
 */
function printMyMsg(myMsg) {
    document.write(myMsg)
}
```

## Reserved JavaScript keywords

When you make some variables, these maybe not be are called like one of the reserved JavaScript keyword.

```javascript
if
else
while
break
function
return
```

## Constants and variable types

We not need to declare a variable before we assign something to it. But we can still declare the variables if we like it too:

```javascript    
var firstName = 'Joe'
```

We had been could declare a variable without defining some stuff to it, we write it then like following:

    var firstName

We not need to specify the type of variable when we create it, it's not like Java. The type of variable can also be are changed in a loop for example. It is a dynamic type.

We can write the following code on one line, but then we need to add the`;` after each line:

```html
<script> msg = "Hello, world!" document.write(msg) </script>
```

The non recommended way:

```html
<script> msg = "Hello, world!"; document.write(msg); </script>
```

That make the code many lesser readable and should be avoided!

## Expressions

We can use constants and variables to make an expression.

If we use some string in a expression, the expression would be of the type string.

```javascript
foo = 'Hello,'
bar = ' world!'
baz = foo + bar
document.write(baz)
```

Another example:

```javascript
foo = 'Hello,'
bar = ' world!'
document.write(foo + bar)
```

If we mix up string with integers, the result would be not like expected. In the next example we make a string containing 1:

```javascript
foo = '1'
document.write(foo + 1)
```

That output:

    11

But if it's really a integer as variable, we not get the trouble:

```javascript
foo = 'Hello,'
bar = 2
baz = ' you'
buu = foo + bar + baz
document.write(buu)
```

That output:

    Hello,2 you

Another example:

```javascript
foo = 'Hello,'
bar = 2
baz = ' you'
document.write(foo + bar + baz)
```

Output:

    Hello,2 you

btw we had been could write:

```javascript
foo = 'Hello,'
bar = 2
baz = ' you'
document.write(foo, bar, baz)
```

## Loops

There are 2 kinds of loops in JavaScript, the `for` and `while` loop. Each of these 2 have their own usage which you will understand better once you start using them.

### The for loop

The `for` loop have 3 important elements. We first initialize a variable that will be used for the counter. Then we have the condition in question. And as least, the incrementer. And finally, in the block of code we have the action that should be repeated. Let's have an example:

```javascript
for (i = 1; i <= 10; i++) 
{
    document.write("<p>Get some looooping ...</p>")
}
```

Let's say it with other words: We first assign the value 1 to the variable `i`, while the value of `i` is lesser as 10; we increment the content of the variable `i` with one more value. (It's similar as `i = i + 1`). And then we execute the block of code that follow the for loop. We have done one iteration. nbr have now the value 2, so it still pass the condition and will be again incremented. The block of code is again executed. nbr have now value ... While the variable `i` is lesser (`<`) or equal (`=`) to 10 (while the condition is true), the block of code is executed. Once nbr have the value 11, the for loop is no more used and the script continue his job with following the next line of code below the for loop.

You should also pay attention to not make an infinite loop. It's so easy to make a mistake and make a loop that never will end. Look at the follow piece of code. This will crash your web browser! Try it out :-)

```javascript
for (i = 1; i >= 1; i++)
{
    document.write("<p>Get some looooping ...</p>")
}
```

With the Firefox web, if a script want to crash the browser, Firefox detect it and show a dialog that permit you to stop the script without crashing Gecko based web browsers.

In the previous example we only have one block of code that should be executed several times depending of the for condition. We had been could use multiples action to execute in the for loop, but then we need
to use the brackets `{ }` to delimit multiples line of code in the same block:

```javascript
for (i = 1; i <= 10; i++) {
    document.write("<p>" + i + " - Get some looooping ...</p>");
    document.write("<hr>");
}
```

It is not required to indent the code in the block. We had been could indent it with 4 spaces to make the stuff more readable. See the same example but indented with 4 spaces:

```javascript
for (i = 1; i <= 10; i++) {
    document.write("<p>" + i + " - Get some looooping ...</p>");
    document.write("<hr>");
}
```

We had also could write it on one line to make the code so weird as possible:

```javascript
for (i = 1; i <= 10; i++) {
    document.write("<p>" + i + " - Get some looooping ...</p>"); document.write("<hr>");
}
```

**Pay attention to the line wrap!**

My personal taste is to indent the block of code with 4 spaces. To make the stuff as many as possible readable. But take your choice! If it does not matter for you, make in sort that it is so readable as possible!

In these previous for loop examples, we wish that we wanted to iterate an amount of times. If we not know how mush time we should need to iterate, you need then to make use of the while loop.

### while loop

When we not know how many times we should need to iterate.

Take for example that we have some application that get some input of the user, put the input result in the `i` variable. Look to this minimalistic piece of code (it's really not yet the ideal example):

```javascript
    i = 1
    while (i <= 10) { 
        document.write("i is still lower as 10! ");
        i++;
    }
```

The `while` function have only one element in his parentheses, while the for loop, had 3 elements. Here we only have the condition in the while parentheses. While the condition is true, the block of code is executed. We should always add an incrementer in the block of code. The for loop have it included in his for parentheses.

We can make use of the break in combination with a condition to break a loop.

## if, elif, else

In the previous examples we have see how it work with logical tests in the loop examples. There was each time a logical test; `<=`.

We can also use logical test in some block code or where as needed.

```javascript
    i = 1;
    if (i < 2) {
        document.write("Lower!");
    }
```

Let's have an example with a combination of the while and the if and break:

```javascript
    i = 1
    while (i <= 100) {
        document.write(i, " Just some tests... ");
        if (i == 50) {
            document.write("Because we spawn to many output, we stop! ");
            break;
        }
    i++;
    }
    document.write("We are done with us test! ");
```

While `i` is lower or equal to 100, run the chunk of code in while loop; Output the message `i`, " Just some tests... " each time (the content of the variable `i` and the message). If `i` is equal to 50 (i == 50), we output the message "Because we spawn to many output, we stop! " and break the while loop. The next code following the while loop is executed; the message "We are done with us test! " is outputted.

The break will only break (stop) the execution of the block of code where the break statement is placed. Take for example the next piece of code that will break the whole script!:

```javascript
document.write("Is outputed on screen!")
break
document.write("Is never seen!")
```

An if with an else example:

```javascript
if (age < 12) {
    entryPrize = 5
    needAdultPresent = true
}
else {
    entryPrize = 10
    needAdultPresent = false
}
```

In the previous example, only one block of code is executed, depending what the content of the variable `age` is; if it's lower as 12 or not.

## Functions

It is common that some pieces of JavaScript code need to be executed on different parts of your HTML page or on a different page. In this case, it's best to split the code in functions so that you do not need to write always the whole repeated chunk of code. You only refer to some function. That will help to get your code more compacter. Also if you want to change a bit the code of the repeated chunk of code, you need to modify it on all the different places where you have write it down. With making use of functions, you modify your function content and it will reflect where needed.

```javascript
function hello_world()
{
    document.write("Hello, world")
}
```

We used the reserved word function following a function name we have choice. When we create a self made function we need to make use of the `{}` brackets, also if there is only one statement line in the block of code in the function.

We can now call us self made function where as we want in the same HTML page:

```javascript
    hello_world()
```

That just output `Hello, world`. It's just a minimalistic piece of code to make a function.

We can create a function that require an argument, so that there will be done something with the argument when we call the function with an argument:

```javascript
    function hello_world(fname)
    {
        document.write("Hello, world and ", fname)
    }
```

We now call us self made function with an argument `hello_world('foo')`:

```javascript
    hello_world('foo')
```

We now call us self made function with an argument `hello_world('bar')`:

```javascript
    hello_world('bar')
```

You can make so personalized messages too.

We define now a default value for a function argument, in case we not give a argument when we call the function.

**NOTE: Then next example have an error in his syntax!**

```javascript
    function hello_world(fname='baz')
    {
        document.write("Hello, world and ", fname);
    }
```

We now call us self made function without an argument `hello_world()` a default value will be used:

```javascript
    hello_world()
```

The previous function examples we showed are really simply and not return some values. It print it out on screen. A such function in other language is called a procedure. A function return some values back so that you can assign it to another variable.

So we need to rewrite the function so that he return some values, so that we could assign it to a variable:

```javascript
function hello_world(fname)
{
    return "Hello, world and ", fname
}
```

A real function should be called as following:

```javascript
foo = hello_world('buu')
/* 
Then we do whatever we want with foo, we only 
output it on screen here
*/
document.write(foo)
```

If we not need to make use of a variable and want to print on screen the stuff returned be a function:

```javascript
document.write(hello_world('xuu'))
{ var tmp = 1 for (i=1;i<=n;i++) tmp = tmp * i return tmp }

function facult(n)
{
    var tmp = 1
    for (i=1; i<=n; i++)
    tmp = tmp * i
    return tmp
}
```
We now call it:

```javascript
    ff = facult(4)
    document.write(ff)
```

And that output:

    24

## Recursion

A function can call another function, but it can also call itself. That's called recursion.

```javascript
function facult(n)
{
    if (n == 1)
    return 1
    else
    return facult(n-1) * n
}
```

Note, we make use of the previous created `facult()` function.

## Build-in functions

JavaScript has some build-in functions that we can use. That avoid that we should need to create these on his own.

Here's a little list of some functions:

* `parseInt()` - 
* `parseFloat()` - 
* `escape()` - Convert non alphanumeric to ascii code (useful for data
    sending between web pages)
* `unescape()` - Inversed of the escape function
* `eval()` - Same thing like in Python
* `history.back()` - To go back, like the back button of the browser.
* `chr.charCodeAt()` - Show the ascii code of a character.

### parseInt()

We give as argument something and get a number or `NaN` Not a Number.

```javascript
document.write(parseInt(3), 
    parseInt("3"), 
    parseInt("3Q"), 
    parseInt("4You"))
```

### eval()

```javascript
foo = 'Hello '
bar = 'world!'
baz = eval("foo+bar")
document.write(baz)
```

Output:

    Hello world!

...

## Operators

There are different operators, you have already make use of it several times before unconscious if you have followed this manual.

-   Assigning operator (Toekenningsoperators) (=)
-   Logical operator (logische operators) (`<`, `<=`, `>`, `>=`, `==`)
-   Calculation operator (berekeningsoperators) (`+`, `-`, `/`, `++`, `...`)
-   Bitwize operator (bitsgewijze operators)
-   ...

### Assigning operator

The `=` sign is the assigning operator.

```javascript
x = 3 + 4
y = x + 3 * 2
x += y     // is like x = x + y
x -= 2     // is like x = x - 2
x *= y     // is like  = x * 2
...
```

### Logical operator

Logical operator output true or false.

```javascript
4 != 3     // output true
NOT false   // true
NOT true   // false
x > y      // x is greater than y
x <= y     // x is lower or egual to y
x >= y     // x is greater or egual to y
x == y     // is like
x != y     // is not like
x && y     // x and y
x || y     // x or y
// The next one is a shortcut way for the if else
// if x == y is true; return EgUaL; else LiKe
x == y ? 'EgUaL' : 'LiKe'
...
```

### Calculation operator

`+`, `-`, `*`, `/` and `%`

```javascript
2 + 1 // 3 
6 - 2 // 4 2 * 3 // 6
6 / 2 // 3 
5 % 2 // 1   # % is the modulo operator 
y = 1 x = ++ y // 2 y = -- Y // x++
```

### Bitwize operators

`<<`, `>>>`, `>>>`, `&` (AND), `^` (XOR) ...

### Special operators

delete - With the delete operator we can delete an element of an array or object.

## typeof()

Useful if you want to know which type a variable of something is.

```javascript
document.write(typeof('hello'))
```

Output one of the follow type:

    'number', 'string', 'boolean', 'object', 'function', and 'undefined'

## Priority rules

```
1. ++, --, - (make negative), ~, !, typeof, void, delete
2. *, /, %
3. +, - (substraction), + (concatenation strings)
4. <<, >>, >>>
5. <, <=, >, >=
6. ==, !=
7. &
8. ^
9. | 
10. &&
12. ||
13. ?:
14. =, OP= (operator combined with `=`, example `+=`)
```

## Strings

We can use single or double quotes to encapsulate a string.

We can escape a single or double quote also if needed. Like `\'Hello, Dave\'s computer\'`.

We make use of n to make a new line in a string. Useful for in alert messages. See for example with the follow code:

```javascript
alert('hello\n world')
```

A tab stop `\t`

Double backslash to escape a `\`. Example `c:\\tmp\\`

### Some methods and properties available on strings

See also `match`, `replace`, `split`, `test` and `exec`

A method on a string:

```javascript
x = "Hello, world"
// return 12 NOTE length is a property, not a method!
document.write(x.length)
document.write(x.toUpperCase())
document.write(x.toLowerCase())
document.write("Test".toLowerCase())
document.write("Test".bold())
```

See also : `big()`, `blink()`, `fontcolor()`, `fontsize()` and `sup()`.

```javascript
    document.write(x.charAt(0)) document.write(x.charAt(0))
```

`X.charAt(Y)`, waarbij geldt: `Y = X.length - 1`. (N.B.: bij `length` gebruiken we geen haakjes aan het eind, omdat het een property is en geen method!) Hiermee kunnen we bijvoorbeeld controleren wat we hiervoor hebben beweerd over de werking van bold. Als we schrijven: `document.write("Test".bold().charAt(1))`, dan wordt het tweede teken van de string getoond; omdat `bold()` `<B>` en `</B>` rondom de string heeft gezet, krijgen we een `B` te zien en dus niet de `e` van Test!

### Slicing a chunk of a string

We can use the `substring()` method on strings to slice the content of the variable.

Let's have an example:

```javascript
x = "Hello, world!"
write.document(x.substring(7))
write.document(x.substring(7, 10))
```

### Searching in a string

We can do it with the methods `indexOf()` and `lastIndexOf()`. `lastIndexOf()` search from backwards occurrence.

Let's have an example:

```javascript
x = "Hello foo and bar.";
x.indexOf("foo");
x.indexOf("foo",2);     // We can start to search from a position
```

## Arrays

You have different ways to initialise an array.

We need to make a constructor.

```javascript
foo = new Array();
foo[0] = "Bart"; foo[1] = "Lisa"; foo[2] = "Magie";

bar = new Array("Homer", "Marge");
baz = new Array("foo", 3.1415, true);

var xuu = ["Me", "You"];
xuu.push("Both of us"); // Add up an item.

document.write(foo, bar, baz, xuu);
```

Printing element `1` (second element, we start to count from `0`)

```javascript
document.write(foo[1]);
```

The array type have also the property length, to get the length of the array.

```javascript
for (item = 0; item <= foo.length-1; item++)
{
    document.write(foo[item], ", ");
}
```

We can assign an array into an array, so that we can make multidimensional array.

### Methods on arrays

#### reverse()

The `reverse` method, reverse the positions.

#### sort()

With `sort`, we can sort the array

```javascript
x = new Array("xuu", "buu", "bar");
document.write(x.sort())
```

#### join()

We join each element of the array to a string:

```javascript
xuu = X.join(" ")  // we want to join it with a space between each item
document.write(xuu)
```

## Objects

This next piece of code not work like expected with Firefox?? It output `1178001555000` while it should be `Fri May 1 00:00:00 UTC+0200 1998` (MS Internet Explorer) or `Fri May 01 00:00:00 GMT+0200 (Romance Daylight Time) 1998` (Netscape Communicator)

```javascript
//birthday = new Date("May 1, 1900")
// or
// Stand for year, month, day
//birthday = new Date(0,4,1);
//birthday = new Date("May 1, 1998 8:39:15");
birthday = new Date(1998, 4, 1, 8, 39, 15);
today = new Date();
birthday = birthday.setYear(2007);
document.write(birthday);
```

### Creating his own objects

```javascript
function auto(bd,tp, yr)
{
    this.brand = bd;
    this.type = tp;
    this.year = yr;
} 
```

The word `this` in the `object`, mean that it is related to this object. This is comparable to `self` used in the Python programming language.

If we want to make use of the custom object, we need to make a new instance of the object. We create an instance with the `new`:

```javascript
littlecar = new auto("Fiat", "Panda", 1996)
write.document(littlecar)
```

Another example may be:

```javascript
personObj=new Object();
personObj.firstname="John";
personObj.lastname="Doe";
personObj.age=50;
personObj.eyecolor="blue";
document.write(personObj.firstname + " is " + personObj.age + " years old.");
```

## Storing scripts in external files

When writing JavaScript code, you will quickly discover that it take much space. With this i mean that there may be many lines. So probably you want to split the stuff and put the JavaScript code in a external file. We give the extension `.js` to the external JavaScript file.

```html
<script src="/static/common.js" type="text/javascript"></script>
```

And then somewhere in the code you call your function:

```html    
<a href="#" onClick="hiddenWikiInfo()">bla</a>
```

Or load it when the page load:

```html    
<body onLoad="hiddenWikiInfo()">
```

## Forms

...

## Events

...

## Frames and navigation

...

## Cookies

...

## Other things

### Viewing what object something has

When developing code, you want time by time check what object some
object has:

```javascript
for(var prop in document){
    document.write(prop + "<br>");
}
```

### Make use of the console for debugging

While creating Javascript code, you need to debug it while writing it, and sometimes you want to show some data so that you know what it holds.

```javascript
var myArray = new Array(); //
    
// Just add a bunch of data to the newly created array
myArray[0] = "Foo"; myArray[1] = "Bar"; myArray[2] = "Baz";
    
// Display stuff to the console. 
// For this use Google Chrome, right click on the page and select Inspect, then click on the "console" tab.
console.log(myArray);
console.log("This is my stuff.");
console.log("5+3");
console.log(5+3);
```

### Snippets of code

```html
<body onLoad="alert('Welcome on my page!')">
<body onUnload="alert('See you back soon!')">
<a href="/virtual_hosts/joomla_dvanmosselbeen.be/quit.html" onClick="return confirm('Really quit?')">quit</a>
```

## Some resources

- <http://www.w3schools.com/js/> The tutorial to follow!
- <http://diveintomark.org/archives/2003/05/05/why_we_wont_help_you>
- <http://developer.mozilla.org/en/docs/Category>:JavaScript:References
- [www.mozilla.org/docs/dom/domref/](http://dvm.zapto.org:8080/pyguicms-dev/articles/view/www.mozilla.org/docs/dom/domref/)
- <http://wp.netscape.com/eng/mozilla/3.0/handbook/javascript/> (is very complete)
- <http://www.dannyg.com/>
- <http://www.voorbeginners.info/javascript/> - It's in dutch
- <http://javascript.startpagina.nl/>
- <http://www.crockford.com/javascript/javascript.html>

