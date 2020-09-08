# David Van Mosselbeen Notes

This is just a bunch of personal notes i made for my specific needs. These are all in Markdown format and shouldn't be 
shared as is as some files could have some private information. (Needs to be checked !)

**Before releasing / sharing any data, each file should be checked and sensitive information should be removed!**

## Notes about the organisation of these files

The content of a file always start with a heading 1 followed by a blank line and then followed by the metadata. Then 
the rest of the file start with a heading 2 and more. 

For headings i will now use the hashtag (#) instead of underlining a word or phrase.

### Meta data of the files

As the content of these files are in simple Markdown format and for future usage, a good manual way would be to add 
meta data to these files. Later on a tool could be used or created to parse these meta data. This is essentially to 
make things easier in the future and to have the ability to import these.

For the moment, the metadata should be on the beginning of the file and should contain the following:

    -----
    title: <The title of the file>
    description: <A description of the file>
    created: <Year-Month-Day hh:mm:ss> (ex: 28-11-2007 13:36:29)
    modified: <Year-Month-Day hh:mm:ss> (ex: 28-11-2007 13:36:29)
    keywords: <Foo>, <Bar>, <Baz>
    lang: en
    -----

**Many of the files should be adjusted to match my current standard.** 

### Creation date

Many files have the same creation time. This is due the fact that some files are very old and have been reconverted 
several times in the past. Mind the different websites i have got.

* created: 2012-12-15 00:00:00: Means files created before this date. This dates back at some migration point.

## TODO

* Add Meta data to each md file.
* Create a script that check each md file to ensure it respect the meta data.
