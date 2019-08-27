# Patching

created: 2012-12-15 00:00:00

Modify some file and create a file containing only the difference.

# Introduction

Some time you want to modify a file and redistribute the modifications that you have applied. Without sending the complete modified file. You can make a patch of what you have modified and only send the differences of the original file, so that others can apply the same changes.

# Let's play

Create a text file and add some fake data. Say, we go to call it `original.txt`and add the following to the file:

    This is some fake text. Just here to play with it. No matters
    what it contain, maybe preferably human readable text. Not
    that we can not apply it to binary files, just better to
    avoid it for now. We make this little text longer as 5 lines,
    so that we been see what's happened. With an shorter text, it
    may look maybe not ideal as example.

Make a copy of the 'original.txt' file and call it 'modified.txt' and change the content of it:

    cp original.txt modified.txt
    This is some fake text. Just here to play with it. No matters
    what it contain, maybe preferably human readable text. Not
    that we can not apply it to binary files, just better to
    avoid it for now. We make this little text longer as 5 lines,
    so that we been see what's happened. With an shorter text, it
    may look maybe not ideal as example. It's many more easy when
    it's basic while we learn the stuff.

We now look with `diff` to see the changes between the both files we have made:

    diff -u original.txt modified.txt

That output the following:

    --- original.txt        2006-12-28 07:41:02.000000000 +0100
    +++ modified.txt        2006-12-28 07:41:28.000000000 +0100
    @@ -3,4 +3,5 @@
    that we can not apply it to binary files, just better to
    avoid it for now. We make this little text longer as 5 lines,
    so that we been see what's happened. With an shorter text, it
    -may look maybe not ideal as example.
    +may look maybe not ideal as example. It's many more easy when
    +it's basic while we learn the stuff.

Okay, we got the difference printed on screen, we now want to save the diff to an file that we call 'patch.diff':

    diff -u original.txt modified.txt > patch.diff

We go now to try to patch a file. We create an third file, a copy of the 'original.txt' file and then apply the patch on it. We make here an third file so that we keep all us files we have made, it's just to keep the things clear:

    cp original.txt patched.txt
    patch patched.txt patch.diff

And that output:

    patching file patched.txt

Good, were been done, you an now work on some stuff and distribute your patch file.

# Additional tips

In `vim`, you can set `:set patchmode=.orig`
