# StackSearch
------------------

A simple script which uses the stackexchange api to help you search for answers to stackoverflow questions for the comfort of your console.

A work in Progress (LOADING....35%.........)


# USAGE
----------------
Set defaults in config.txt - see config.sample

Start script with 2 arguments the search query and tags for the search query

```
$ answer.py search_query seach_tags
```
![alt text](https://github.com/mikeyny/StackSearch/blob/master/stacksearch2.png)

# Features

* User can set defaults in config files (Stackexchange site , number of results ,search preference).
* Results are display in a nicely formatted table .
* Displays top answer to all question results.


# To- Do
----------

* Make a search class ,so that each search is an instance of the class
* Allow for scrolling through answers incase the first one doesn't make the cut
* Better exception handling
