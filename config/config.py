config = {
    
    'irc': {
        'server': 'irc.twitch.tv',
        'port': 6667
    },

    # Place your twitch account username and the OAuth token for your channel
		# here. If you don't know your OAuth token, you can find or generate it
		# here: http://twitchapps.com/tmi/. NOTE: Be sure to secure this token!
		# Anyone who has this can stream on your channel.

    'account': {
        'username': '<PLACE YOUR USERNAME HERE>',
        'password': '<PLACE YOUR OAuth TOKEN HERE>'
    },

    # Twitch already has spam fighting in their console now, but in case you
		# would like further granularity, enter the keyword you would like to time
		# out here, and an integer representing the number of seconds to timeout.

    'throttled_buttons': {
        'turkey': 10
    },
	
  # Dictionary of commands used for the Hold Key function. This is for actions
	# in a game that need longer key presses, e.g. moving the character. The
	# number of seconds can be set or changed in game.py 'hold_button'. 

	'held_buttons': {
		'holdup',
		'holdu',
		'holddown',
		'holdd',
		'holdright',
		'holdr',
		'holdleft',
		'holdl'
	},
	
  # Dictionary of commands used for the Step Key function. This is for actions
	# in a game that need very short key presses, e.g. menu navigation. The number
	# of seconds can be set or changed in game.py 'step_button'.

	'step_buttons': {
		'stepleft',
		'stepright',
		'stepup',
		'stepdown',
		'stepl',
		'stepr',
		'stepu',
		'stepd'
	},

    # Not currently used, planned on future development.

    'spam_buttons': {
        'spama'
    },

    # Display height of showing chat commands in Command Prompt/Terminal.

    'misc': {
        'chat_height': 13
    }

}