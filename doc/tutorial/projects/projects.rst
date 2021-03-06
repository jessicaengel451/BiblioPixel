Projects
--------------

A BiblioPixel Project is a text file describing a lighting project in either
`YAML <https://yaml.org>`_ or `JSON <https://json.org>`_ format.

Projects have been designed to be as flexible and forgiving as possible.

You can reuse bits of projects inside other projects, and you can combine
partial projects from the command line, like this:

.. code-block:: bash

    bp living-room.yml + smooth-fades.yml

    # Or even inline
    bp smooth-fades.yml + '{shape: [30, 30], driver: my-driver.yml}'

You have many formats you can use for values - for example, you can represent
colors by a name like ``"red"`` or ``"DarkSlateBlue"``, a web color like
``#FF7F0F``, or a list of RGB components like ``[255, 127, 15]``.

There's every attempt to give good error messages, and to explain that, for
example, ``"sickly pink"`` is not a valid color name.

If you run into an error message using Projects that you do not understand,
please report it as an issue
`here <https://github.com/ManiacalLabs/BiblioPixel/issues>`_
or ask a question on the
`Maniacal Labs User Group <https://groups.google.com/d/forum/maniacal-labs-users>`_\ .

**Example 1**: a simple Project file written in YAML

.. bp-code-block:: example-1

   shape: 50
   animation: $bpa.strip.Wave

**Example 2**: a slightly larger Project file, written in JSON

.. bp-code-block:: example-2

   {
       "shape": [64, 32],

       "run": {
           "fps": 60
       },

       "animation": {
           "typename": "$bpa.matrix.MatrixRain",
           "colors": ["blue", "yellow", "coral"]
       }
   }

**Example 3**: the same Project file as in Example 2, but written in YAML

.. bp-code-block:: example-3

   shape: [64, 32]

   run:
     fps: 60

   animation:
     typename: $bpa.matrix.MatrixRain
     colors: [blue, yellow, coral]

.. bp-code-block:: footer

   shape: [64, 4]
   animation: $bpa.strip.SaberBlade
