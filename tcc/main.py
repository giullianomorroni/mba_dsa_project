# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # encoding=utf8
import json

cdbs = open('../data_original/cdb/produtos.json')

cdbs = json.load(cdbs)
print(cdbs)
