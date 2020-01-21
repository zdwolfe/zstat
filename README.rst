zstat
========================


A bone-simple stats tool for displaying percentiles from stdin to stdout.
Example:

:: 

  $ cat nums.txt
  456
  366
  695
  773
  617
  826
  56
  78
  338
  326


:: 

  $ cat nums.txt | zstat
  p0      =       56
  p50     =       366
  p90     =       773
  p95     =       773
  p99     =       826
  p99.9   =       826
  p100    =       826

Installation
=========================================================
``pip install zstat-cli``


Local Installation
=========================================================

Clone this repository locally, then:

``pip3 install -e .``

Building
=========================================================


``make``


Testing
=========================================================

``make test``


Deploy New Version
=========================================================

``make deploy``
