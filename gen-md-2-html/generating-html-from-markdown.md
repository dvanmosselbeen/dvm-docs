# Generating HTML from Markdown

To convert the `Markdown` files to `HTML`, the application `pandoc` can be used to do so. `pandoc` is able to convert to and from a variety of formats. pandoc can be easily installed with `apt-get install pandoc`.

There is no script here yet to automate the translation from `Markdown` to `HTML`.

The following will make use of a custom `css` file and `Google fonts`. On top of this, it will also create a `Table of Contents`:

```commandline
pandoc --metadata title="Debian" -s --toc --css=mystyle.css --css="https://fonts.googleapis.com/css?family=Roboto|Oswald" debian.md -o debian.html
```

## Make use of SASS

Quick start here: <https://www.w3schools.com/sass/sass_intro.php> even if I have the basics. Just a not so that I will look into this to make css for these markdown files.

## Remarks

- As some Markdown files have some handmade TOC, in that case, there will be a double TOC. Need to clean up the Markdown files and remove the TOC.
- The TOC made by `pandoc` doesn't have a header entry.

## Remarks to make a script

- The first line in the markdown file should be stripped of, like we use a title command with pandoc, there will be twice a reference to the title of the document, one in header 1 and the other in header 2.

## Resources

- <https://pandoc.org/demos.html>
