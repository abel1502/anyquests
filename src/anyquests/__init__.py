import sys
import textwrap

try:
    import niquests
    sys.modules["anyquests"] = niquests
except ImportError:
    try:
        import requests
        sys.modules["anyquests"] = requests
    except ImportError:
        raise ImportError(textwrap.dedent(
            """
            
            Neither niquests nor requests are installed. Please install one of these package and try again.
            
            Use:
                pip install niquests
            or:
                pip install requests
            
            For more information see: https://github.com/niquests/anyquests#i-am-an-end-user-which-one-to-choose
            """
        )) from None
