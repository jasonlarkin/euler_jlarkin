# % operator
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print text

# add parens to make the long-line work:
text = ("%d little pigs come out or I'll %s and %s and %s" %
    (3, 'huff', 'puff', 'blow down'))

print text

ustring = u'A unicode \u018e string \xf1'
print ustring

s = ustring.encode('utf-8')
print s
t = unicode(s, 'utf-8')
print t == ustring


