import re


def shorten(s, N=80):
    """
    Return short representation of string s.
    """
    if len(s) <= N:
        return s[:]
    else:
        l = (N - 5)/2
        return '{} ... {}'.format(s[:l], s[-l:])


def newlineindex(mlstring, start=0):
    """
    Return two indices, for the end of the 1-st line and start of the next one.
    """
    r = re.compile('[\r\n]+')
    m = r.search(mlstring, start)
    return m.start(), m.end()


def nol(txt, start=None, end=None):
    """
    Return number of lines in the multi-line string txt.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(txt)
    if '\r' in txt:
        return txt.count('\r', start, end) + 1
    else:
        return txt.count('\n', start, end) + 1


def zip_columns(c1, c2, valign='t'):
    """
    Concatenate lines from tuples c1 and c2 together and return a tuple of
    obtained lines. The length of the returned tuple is max(len(c1), len(c2)).
    """

    # Make c1 and c2 the same length
    c1 = tuple(c1)
    c2 = tuple(c2)
    if len(c1) != len(c2):
        l1 = len(c1)
        l2 = len(c2)
        dl = abs(l1 - l2)
        if valign == 't':
            dt1 = ()
            dt2 = ('', ) * dl
        elif valign == 'b':
            dt1 = ('', ) * dl
            dt2 = ()
        elif valign == 'c':
            dl1 = dl / 2
            dl2 = dl - dl1
            dt1 = ('', ) * dl1
            dt2 = ('', ) * dl2
        else:
            raise NotImplementedError('Unknown vertical alignment', valign)
        if l1 > l2:
            c2 = dt1 + c2 + dt2
        else:
            c1 = dt1 + c1 + dt2

    w1 = max(len(l) for l in c1)
    w2 = max(len(l) for l in c2)
    f = '{{:<{}s}}{{:<{}s}}'.format(w1, w2)
    return (f.format(*s) for s in zip(c1, c2))
