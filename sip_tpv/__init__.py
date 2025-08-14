from .sip_to_pv import sip_to_pv
from .pv_to_sip import pv_to_sip
#import pkg_resources
from importlib.metadata import version

#__version__ = pkg_resources.get_distribution("sip_tpv").version
__version__ = version("sip_tpv")
