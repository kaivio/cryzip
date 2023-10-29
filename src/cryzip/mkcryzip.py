#!/usr/bin/env python

from cryzip import param

param.dirs = ['.']
param.output = '../archive_%(date)s.7z'
param.readme = ''' # %%(output)s

*No description*

## Comment

%%(comment)s

'''


#param.fiter = lambda entry: True

from cryzip import start
