#!/usr/bin/env python

import os

cwd = os.getcwd()

overlays = ['report', 'setup', 'tools']
# mount overlayfs
for overlay in overlays:
  os.system("mkdir overlay/work-%s 2>/dev/null" % overlay)
  cmd = "sudo mount -t overlay -olowerdir=/home/analysis/%s,upperdir=%s/overlay/analysis/%s,workdir=%s/overlay/work-%s none /home/analysis/%s" % \
  (overlay, cwd, overlay, cwd, overlay, overlay)
  os.system(cmd)

# inject init script
os.system("cp overlay/analysis/init.py ~")
# inject server script
os.system("sudo cp overlay/server/complex.php /var/www/html/server/")

# reset iptables
os.system("sudo ~/tools/network/reset")

# run init
os.system("cd ~;./init.py")
