.. _contribute:

=======================
Contribute to this site
=======================

In order to be an effective guide for others, **this site needs to include the advice, experiences, perspectives and insights of African professionals in the software industry**.

The site is an open-source project, and all contributions will be credited (unless you prefer to be anonymous). If you have an idea for something to be included but you aren't sure whether it's the right kind of thing, or how to write it, get in touch to ask.

**Suggestions and requests** (for example if you have a question related to software careers) are also welcomed - use GitHub issues or email to send them in.


How to contribute
=================

There are multiple options.

* **Submit a pull request**: See `the project readme file <https://github.com/evildmp/fanaka/blob/main/readme.rst>`_ for details of how to build the site locally.

* **Edit the page in your browser**: At the top of every page is a an edit icon, that will take you to the file for that page on GitHub (you'll need to be signed in for this). You will need to create a fork of the repository, if you haven't done so already. Make your changes, and hit **Commit changes...**. GitHub will take you through the process of making a pull request to incorporate the changes you have made.

* **Send your contribution or suggestion as a GitHub issue** (`create a new issue <https://github.com/evildmp/fanaka/issues/new>`_)

* **Send your contribution or suggestion by email** (address on the `GitHub repository page  <https://github.com/evildmp/fanaka/>`_). The other methods described above will mean that your contribution will be associated with you, so do this if you would prefer that it isn't.


Contribute to translations
===========================

You can contribute to translation of Fanaka either by using the Transifex web interface or by editing the project's translation files in the Git repository.


Using Transifex
---------------

Transifex is a service that provides a convenient web-based interface for collaborating on translation.

Join the `Fanaka translation team on Transifex <https://explore.transifex.com/danieleprocida/fanaka/>`_.

Transifex guides:

* `Getting started as a translator <https://help.transifex.com/en/articles/6248698-getting-started-as-a-translator>`_
* `Translating with the web editor <https://help.transifex.com/en/articles/6318216-translating-with-the-web-editor>`_

The web editor for Fanaka on Transifex: https://app.transifex.com/danieleprocida/fanaka/translate/.


Editing translation files
-------------------------

Strings for transalation are referred to as "messages" - this is based on the origin of the translation system's focus on application and system messages.

Translations for each page are added or edited in the corresponding ``.po`` (Portable Object) file, which can be found in ``locales/<lang>/LC_MESSAGES/``. For example to translate :ref:`studies` (``studies.fr``) to French:

* the original page: ``studies.rst``
* the  ``.po`` file to edit: ``locales/fr/LC_MESSAGES/``

The ``.po`` file contains pairs of strings, the original ``msgid`` ("message ID") and the translation ("message string"). For example::

    msgid "Professional experience"
    msgstr ""

In this case the ``msgstr`` is empty - no translation exists yet, so the translator needs to add *Expérience professionnelle* to the ``msgstr``.

The final step is to make a pull request containing the new translations that have been added.


Contributors
============

* `Daniele Procida <https://vurt.org>`_
* `Stephen Mwangi <https://www.stephenmwangi.com>`_
* `Sharon Koech <https://www.linkedin.com/in/skoech/>`_
* `Charles Odada <https://www.linkedin.com/in/charlesodada/>`_


----------

Fanaka © 2025 by Daniele Procida and other contributors is licensed under CC BY-SA 4.0
