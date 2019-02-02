# Copyright (c) 2019 Monolix
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from dmotd.daemon import DMOTD

d = DMOTD()

d.run(port=8000)
