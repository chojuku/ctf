# -*- coding: utf-8 -*-
import sys
import re

for line in sys.stdin:
    print re.sub(r"[A-Z]", "1", re.sub(r"[a-z]", "0", line))
