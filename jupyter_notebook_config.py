import os
from IPython.lib import passwd

c.NotebookApp.ip='0.0.0.0'
#c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python'

# sets a password if PASSWORD is set in the environment
#if 'PASSWORD' in os.environ:
#  c.NotebookApp.password = passwd(os.environ['PASSWORD'])
#  del os.environ['PASSWORD']
c.NotebookApp.password = u'sha1:b806083743c3:ee82685ac965fab7850070104d4673e1d006f3a0'
c.NotebookApp.iopub_data_rate_limit=10000000
