from ipalib.plugins import user
from ipalib.parameters import Str
from ipalib import _
user.user.takes_params = user.user.takes_params + (
		Str('mailmessagestore?',
			cli_name='messagestore',
			label=_('[sub]directory for store maildir'),
		   ),
		)
user.user.default_attributes.append('mailmessagestore')
