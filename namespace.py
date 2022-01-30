import string
import yaml
f = open('data.yaml')
cfg = yaml.safe_load(f)['global']
f.close
for ns in cfg['namespaces']:
	ns_key=list(ns.keys())[-1]
	ns_value=ns[ns_key]
	print(ns_value)
	for secret in ns_value['secrets']:
		print(f"Processing secret {secret} in {ns_key} namespace")
