import os
import dominate
from dominate.tags import attr, script, link, meta, div, li, p, a, ol, title


def makeHtml(path, fileName, sitename, authorname, usecss, usejs):
    doc = dominate.document(title=sitename)

    with doc.head:
        if (usecss.lower() == "y"):
            link(rel='stylesheet', href='style.css')
        if (usejs.lower() == "y"):
            script(type='text/javascript', src='script.js')
        with meta():
            attr(author=authorname)

    with doc:
        with div(id='header').add(ol()):
            for i in ['home', 'about', 'contact']:
                li(a(i.title(), href='/%s.html' % i))

        with div():
            attr(cls='body')
            p('Lorem ipsum..')
    # http://stackoverflow.com/questions/273192/how-to-check-if-a-directory-exists-and-create-it-if-necessary
    # os.makedirs(path, exist_ok=True)
    if not os.path.exists("./" + path):
        os.makedirs("./" + path)

    f = open("./" + path + "/" + fileName, 'w+')
    f.write(str(doc))
    f.close()

    if (usejs.lower() == "y"):
        if not os.path.exists("./" + sitename + "/js"):
            os.makedirs("./" + sitename + "/js")
    if (usecss.lower() == "y"):
        if not os.path.exists("./" + sitename + "/css"):
            os.makedirs("./" + sitename + "/css")

sitename = str(input("Site name :"))
author = str(input("Author : "))
usejs = str(input("Do you want a folder for JavaScript?")).lower()
usecss = str(input("Do you want a folder for CSS?")).lower()

makeHtml(sitename, "index.html", sitename, author, usecss, usejs)

