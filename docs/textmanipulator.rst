.. _textmanipulator:

===============
TextManipulator 
===============

This is the cog guide for the textmanipulator cog. You will
find detailed docs about usage and commands.

Throughout this documentation, ``[p]`` is considered as your prefix.

------------
Installation
------------

Let's firstly add my repository if you haven't already:

* :code:`[p]repo add kreusada https://github.com/kreusada/kreusadacogs`

Next, let's download the cog from the repo:

* :code:`[p]cog install kreusada textmanipulator`

Finally, you can see my end user data statements, cog requirements, and other cog information by using:

* :code:`[p]cog info kreusada textmanipulator`

-----
Usage
-----

Manipulate text with tools.

.. _textmanipulator-commands:

--------
Commands
--------

Here's a list of all commands available for this cog.

.. _textmanipulator-command-convert:

^^^^^^^
convert
^^^^^^^

**Syntax**

.. code-block:: ini

    [p]convert

**Description**

Convert text to different casetypes or change their UI.

.. _textmanipulator-command-convert-alt:

"""""""""""
convert alt
"""""""""""

**Syntax**

.. code-block:: ini

    [p]convert alt <characters>

**Description**

Convert text to AlTeRnAtInG cAsE.

**Arguments**

* ``<characters>``: The text to convert.

.. _textmanipulator-command-convert-lower:

"""""""""""""
convert lower
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]convert lower <characters>

**Description**

Convert text to lower case.

**Arguments**

* ``<characters>``: The text to convert.

.. _textmanipulator-command-convert-snake:

"""""""""""""
convert snake
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]convert snake <characters>

**Description**

Convert text to have_snake_spaces.

**Arguments**

* ``<characters>``: The text to convert.

.. _textmanipulator-command-convert-title:

"""""""""""""
convert title
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]convert title <characters>

**Description**

Convert text to Title Case.

**Arguments**

* ``<characters>``: The text to convert.

.. _textmanipulator-command-convert-upper:

"""""""""""""
convert upper
"""""""""""""

**Syntax**

.. code-block:: ini

    [p]convert upper <characters>

**Description**

Convert text to UPPER CASE.

**Arguments**

* ``<characters>``: The text to convert.

.. _textmanipulator-command-count:

^^^^^
count
^^^^^

**Syntax**

.. code-block:: ini

    [p]count

**Description**

Count the number of characters/words in text.

.. _textmanipulator-command-count-characters:

""""""""""""""""
count characters
""""""""""""""""

**Syntax**

.. code-block:: ini

    [p]count characters <characters>

**Description**

Count the number of characters in the text.

**Arguments**

* ``<characters>``: The text to count against.

.. _textmanipulator-command-count-characters:

"""""""""""
count words
"""""""""""

**Syntax**

.. code-block:: ini

    [p]count words <words>

**Description**

Count the number of words in the text.

**Arguments**

* ``<words>``: The text to count against.

.. _textmanipulator-command-escape:

^^^^^^
escape
^^^^^^

**Syntax**

.. code-block:: ini

    [p]cscape <words>

**Description**

Escape Discord markdown in the text.

**Arguments**

* ``<words>``: The text to escape.

.. _textmanipulator-command-remove:

^^^^^^
remove
^^^^^^

**Syntax**

.. code-block:: ini

    [p]remove <char_to_remove> <words>

**Description**

Remove a specific character from the text.

**Arguments**

* ``<char_to_remove>``: The character to remove.
* ``<words>``: The text to remove this character from.

----------------------
Additional Information
----------------------

This cog has been vetted by the Red-DiscordBot QA team as approved.
For inquiries, see to the contact options below.

---------------
Receive Support
---------------

Feel free to ping me at the `Red Cog Support Server <https://discord.gg/GET4DVk>`_ in :code:`#support_othercogs`,
or you can head over to `my support server <https://discord.gg/JmCFyq7>`_ and ask your questions in :code:`#support-kreusadacogs`.