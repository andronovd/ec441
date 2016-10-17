import os
import time
t = os.stat( "web_server.py" )[ 8 ]
lastmod = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( t ) );
print( lastmod );
