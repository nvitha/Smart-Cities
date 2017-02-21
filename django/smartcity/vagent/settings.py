# These topic will be watched.  The messages will be written to
# standard out.
topics_prefixes_to_watch = (
	'heartbeat',
	'heartbeat/ListenerAgent/'
	#'datalogger'
)

heartbeat_period = 10

# The parameters dictionary is used to populate the agent's 
# remote vip address.
_params = {
	# The root of the address.
	'vip_address': 'tcp://147.222.165.15',
	'port': 22916,
	
	# public and secret key for the standalonelistener agent.
	# These can be created from the volttron-ctl keypair command.
	'agent_public': 'XAa3R9hrbNVFLiOCtlKP9KuH8BZblRRYMj8jETWlaW8',
	'agent_secret': 'JzDs3PkhDkSKAtWE-TkrevrmulCogfLwvkneMSKeacI',
	
	# Public server key from the remote platform.  This can be
	# obtained from the starting of the platform volttron -v.
	# The output will include public key: ....
	'server_key': 'D88v1zyKyjUnIXTDPUSGrjf2V29-sddJYEIrsTO_nGQ'
}

def remote_url():
	return "{vip_address}:{port}?serverkey={server_key}" \
		"&publickey={agent_public}&" \
		"secretkey={agent_secret}".format(**_params)
