#!/usr/bin/python
# from __future__ import print_function
# from __future__ import unicode_literals
# from __future__ import division
# from __future__ import absolute_import

# from builtins import range

from uuid import uuid4
from datetime import datetime
from traildb import TrailDBConstructor, TrailDB
cons = TrailDBConstructor('txiny', ['username', 'action'])

print("h")

# for i in range(3):
#     uuid = uuid4().hex
#     username = 'user%d' % i
#     for day, action in enumerate(['open', 'save', 'close']):
#         cons.add(uuid, datetime(2016, i + 1, day + 1), (username, action))

# cons.finalize()

# for uuid, trail in TrailDB('tiny').trails():
#     print(uuid, list(trail))
