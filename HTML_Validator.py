#!/bin/python3


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are
    not meant to be used directly by the user are prefixed with an underscore.
    This function returns a list of all the html tags contained
    in the input string,stripping out all text not contained within
    angle brackets.
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    htmltag = html.replace("<", "*<")
    htmltag = htmltag.replace(">", ">*")
    x = htmltag.split("*")
    tags = []
    cleantags = []
    for i in x:
        if i.startswith("<") and i.endswith(">"):
            tags.append(i)
    for tag in tags:
        sep = " "
        tag = tag.split(sep, 1)[0]
        if tag[-1] != ">":
            cleantags.append(tag + ">")
        else:
            cleantags.append(tag)
    return cleantags


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html
    # tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to
    # keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    stack = []

    htmltags = _extract_tags(html)
    if html == '':
        return True
    if htmltags == []:
        return False
    else:
        for symbol in htmltags:
            if '>' not in symbol:
                return False
            if '/' not in symbol:
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                if (stack[-1][0] == '<' and symbol[1] == '/'):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
