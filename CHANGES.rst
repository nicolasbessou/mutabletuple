Change log
==========

0.1 2015-03-04 Nicolas Bessou
----------------------------

* Initial release.

* Based off my recordtype project, but uses ast generation instead of
  building up a string and exec-ing it. This has a number of advantages:

  - Supporting both python2 and python3 is easier. exec has the
    anti-feature of having different syntax in the two languages.

  - Adding additional features is easier, because I can write in real
    Python instead of having to write the string version, and deal
    with all of the escaping and syntax errors.

* Added FACTORY, to allow namedlist to work even with mutable defaults.
