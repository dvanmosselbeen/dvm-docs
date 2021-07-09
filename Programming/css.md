-----
title: CSS
description: This page talk about css.
created: 16-01-2008 00:00:00
modified: 16-01-2008 00:00:00
keywords: css, webdev, html, development, programing, website
lang: en
-----

# CSS

CSS stands for Cascading Style Sheet. It's meant to be used for the styling of 
web pages.

## How to use CSS

There's 3 different ways to specify css style.

* inline ex: `<h1 style="background-color: red;">`
* internal ex: Whatever is included into a `<style>` tag in the `<head>` section.
* external: is in it's own external css file and we then import it with: `<link 
  rel="stylesheet" href="css/styles.css">` in the `<head>` section.

## Difference between an id and class

When specifying an id, it's meant to be unique. With defining a class, it's 
mean to be reusable.

A little css file example:

```
#header_sep {
    background: #eee;
    border: 0px;
}
.maintablecol {
    background: white;
    border: 0px;
}
```

The first one is used for the id tag, the second for a class.

```
<div id=header_sep>
...
</div>
```

This is the second:

```
<td class="header_sep">
...
</td>
```

# Resources

* https://developer.mozilla.org/en-US/docs/Web/CSS/Reference