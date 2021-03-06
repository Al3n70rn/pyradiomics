import sys

if sys.version_info < (2, 6, 0):
  raise ImportError("pyradiomics > 0.9.7 requires python 2.6 or later")
in_py3 = sys.version_info[0] > 2

import logging


def debug(debug_on=True):
  """
  Set up logging system for the whole package.
  By default, module hierarchy is reflected in log, as child loggers are created by module
  This is achieved by the following line in base.py: ``self.logger = logging.getLogger(self.__module__)``
  To use same instance in each module, set ``self.logger=logging.getLogger('radiomics')``.

  At command line, turn on debugging for all pyradiomics functions with:

  ``import radiomics``\n
  ``radiomics.debug()``

  Turn off debugging with:

  ``radiomics.debug(False)``
  """
  global logger, debugging
  if debug_on:
    logger.setLevel(logging.DEBUG)
    debugging = True
  else:
    logger.setLevel(logging.WARNING)
    debugging = False


debugging = True
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
# formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M")
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
debug(False)  # force level=WARNING, in case logging default is set differently (issue 102)

# For convenience, import the most used packages into the "pyradiomics" namespace
import collections, numpy

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions
