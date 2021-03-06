# Copyblock

Copyblock came out of a desire of mine to separate the copy for a site I'm working on from the site templates. Things like welcome messages, intro copy for forms, etc. This is copy I'd like to be able to tweak easily over time without having to redeploy the entire site to make it happen. What I wanted was a system kindof like gettext, but without .po files, the weird syntax, and a separete app to generate the right files.

[![Markdown  Supported](http://static.monkinetic.com/django-copyblock/md.png)](http://dcurt.is/the-markdown-mark)

What I wanted was really simple: a directory of text files, optionally in [Markdown](http://daringfireball.net/projects/markdown) , that could be inserted into my app templates with a template tag. That's what Copyblock does.

## Installation

From Pypi:

    % pip install django-copyblock

From [Github](http://github.comsivy/django-copyblock):

    % pip install -e git://github.com/sivy/django-copyblock.git#egg=copyblock

## Usage

Create a root directory for your copyblock files:

    %  mkdir copy/dir

Add this path to your settings file:

    COPYBLOCK_ROOT='path/to/your/copy/dir'

In your templates:

    {% copyblock filename %}

This will do the following:

* Look for copy/dir/filename.markdown
* Run the file filename.markdown through markdown
* Cache the output for future lookups
* Insert the output in the rendered template

 Right now, copyblock only does markdown. If your copy is not in markdown (plain text), you can pass in the `nomarkdown` parameter to the template tag:

    {% copyblock filename nomarkdown %}

 Also, if you don't want to use the in-memory cache (load copy from file every time, good for copy editing), pass in the `nocache` parameter:

    {% copyblock filename nocache %}

When working on site copy, it can be helpful to turn off the Copyblock cache completely with (in `settings.py`):

    COPYBLOCK_CACHE=False

To use Python Markdown extensions, add extensions in the settings file:

    COPYBLOCK_MARKDOWN_EXT=['fenced_code']

## Serving Copyblock Files

Copyblock provides a simple app that will serve Markdown files in your COPYBLOCK_ROOT on the url endpoint of your choosing:

In `settings.py`, set the template name (in your main application) to render markdown files through:

    COPYBLOCK_TEMPLATE='template.html'

This template should contain an `output` template variable, like so:

    {{ output|safe }}

In `urls.py`, add:

    urlpatterns += patterns('',
        url(r'^site/(?P<path>.+)',   include('copyblock.urls',  namespace="copyblock",  app_name='copyblock')),
    )

The path can be whatever you choose.

Now, accessing http://mysite.example.com/site/name-of-markdown-file in your browser will load the content of the

## @TODO

* Add support for other text formats, or even HTML (suggestions, request? <steve@wallrazer.com>)
* A view that will render any file in `settings.COPYBLOCK_ROOT` through the site's base template (`base.html`) under a path determined by `urls.py`. IE, `/path/to/copy/dir/foo.markdown` would be viewable at `yoursite.com/somepath/foo`. Or, something like that. [DONE]
