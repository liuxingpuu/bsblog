# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from ..blog import create_app

import os
web_config = os.environ.get('WEBCONFIG', 'ucloud')
app = create_app(web_config)
