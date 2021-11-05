Test1
-----

.. flat-table:: table title
   :widths: 2 1 1 3
   :class: table-test
   :name: table-name
   :stub-columns: 1

   * - head col 1
     - head col 2
     - head col 3
     - head col 4

   * - column 1
     - field 1.1
     - field 1.2 with autospan

   * - column 2
     - field 2.1
     - :rspan:`1` :cspan:`1` field 2.2 - 3.3

   * .. _`last row`:

     - column 3
