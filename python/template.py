import dominate
import os
from dominate.tags import *

def makeHtml(fileName):
    doc = dominate.document(title='Dominate your HTML')

    with doc.head:
        link(rel='stylesheet', href='style.css')
        script(type='text/javascript', src='script.js')
        with meta():
            attr(author="bhlee")
            
    with doc:
        with div(id='header').add(ol()):
            for i in ['home', 'about', 'contact']:
                li(a(i.title(), href='/%s.html' % i))

        with div():
            attr(cls='body')
            p('Lorem ipsum..')
    # http://stackoverflow.com/questions/273192/how-to-check-if-a-directory-exists-and-create-it-if-necessary
    # os.makedirs(path, exist_ok=True)
    if not os.path.exists("C:/js/bhlee"):
        os.makedirs("C:/js/bhlee")

    f = open("C:/js/bhlee/"+fileName, 'w')
    f.write(str(doc))
    f.close()

makeHtml("index.html")