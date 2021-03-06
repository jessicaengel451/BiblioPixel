The ``drivers`` Section
-----------------------------

``drivers`` is a list of Class Sections and is used when there are multiple
hardware or virtual Drivers controlled by one Project.

A very common case is an installation with many instances of more or less the
same driver - as in a long strip or a large matrix with many parts.

If there is both a ``driver`` and ``drivers`` section, then the ``driver`` Class
Section is used as a default for each entry in the ``drivers`` section.  This
often removes a huge amount of duplicated typing:

**Example 1**: A ``drivers`` Section for three serial devices

.. code-block:: yaml

   # I have three LED strips attached to three AllPixels:
   # device 1, 80 LEDs; device 3, 100 LEDs, device 0, 80 LEDs

   drivers:
     - c_order: BRG
       num: 80
       gamma: [1.1, 0.5, 0]
       ledtype: LPD8806
       typename: serial
       device_id: 1

     - c_order: BRG  # Didn't I just see this?
       num: 100
       gamma: [1.1, 0.5, 0]
       ledtype: LPD8806
       typename: serial
       device_id: 3

     - c_order: BRG  # Not again??
       num: 80
       gamma: [1.1, 0.5, 0]
       ledtype: LPD8806
       typename: serial
       device_id: 0

**Example 2**: Same as before, with ``driver`` and ``drivers`` Sections

.. code-block:: yaml

   driver:
     c_order: BRG
     gamma: [1.1, 0.5, 0]
     ledtype: LPD8806
     typename: serial
     num: 80

   drivers:
    - device_id: 1
    - {device_id: 3, num: 100}
    - device_id: 0

**Example 3**: Using drivers to address multiple SPI ports

.. code-block:: yaml

  driver:
    typename: .SPI.WS2801
    num: 64

  drivers:
    - dev: /dev/spidev0.0
    - dev: /dev/spidev0.1

.. bp-code-block:: footer

   shape: [64, 16]
   animation:
     typename: $bpa.strip.FireFlies
     colors: ['light grey', 'slate grey 1', 'slate grey 4']
