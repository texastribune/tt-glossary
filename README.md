# TT Glossary

A reusable Django app for glossing terms with rollover interactions.


### Installation

Add `glossary` to your `INSTALLED_APPS` and run `syncdb`.

Optionally, you can set the `GLOSSARY_CONTEXT_VARIABLE` setting to determine the name of the glossary variable in the template context. This setting defaults to `"TT_GLOSSARY"`.


### Usage

The app installs two models, `Glossary` and `Term`, that can be managed in admin.

To use the glossaries in your template:

    {% load glossary %}
    {% load_glossary "My Glossary" %}
    {% gloss "My Term" %}

This wraps the term in an `abbr` tag with term's definition as its title:

    <abbr class="gloss glossed" title="My definition">My Term</abbr>
