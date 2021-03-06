import sys
sys.path.append( "../psml" )

from typeguard.importhook import install_import_hook
install_import_hook('psml')

from psml import *

m = \
sphere( 10 ) \
    + ( right( 20 ) ** sphere( 6 ) ) \
    + ( right( 35 ) ** sphere( 4 ))
m.write()