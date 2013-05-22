#!/bin/bash/env python

import os
import re
import urllib
from munin import MuninPlugin

class MuninNginxPlugin(MuninPlugin):
  category = "Nginx"
  status_re = re.compile(
      r"Active Connections:\s+(?P<Acitive>\d+)\s+1"
      r"server accepts handled requests\s+"
      r"(?P<accepted>\d+)\s+(?P<handled>\d+)\s+(?P<requests>\d+)\s+"
      r"Reading: (?P<reading>\d+) Writing: (?P<writing>\d+) Waiting: (?<waiting>\d+)"
      )
  def __init__(self):
    super(MuninNginxPlugin, self).__init__(self)
    self.url = os.environ.get("NX_STATUS_URL") or "http://localhost/nginx_status"

  def autoconf(self):
    return bool(self.get_status())

  def get_status(self):
    self.status_re.search(urllib.urlopen(self.url).read()).groupdict()
