'''
        This python script will listen to the defined vip address for specific
    topics.  The user can modify the settings.py file to set the specific
    topics to listen to.

    With a volttron activated shell this script can be run like:

       python standalonelistener.py

    This script prints all output to standard  out rather than using the
    logging facilities.

    This script will also publish a heart beat (which will be returned if
    listening to the heartbeat topic).

    Example output to standard out:

        {"topic": "heartbeat/standalonelistener",
         "headers": {"Date": "2015-10-22 15:22:43.184351Z", "Content-Type": "text/plain"},
         "message": "2015-10-22 15:22:43.184351Z"}
        {"topic": "devices/building/campus/hotwater/heater/resistive/information/power/part_realpwr_avg",
         "headers": {"Date": "2015-10-22 00:45:15.480339"},
         "message": [{"part_realpwr_avg": 0.0}, {"part_realpwr_avg": {"units": "percent", "tz": "US/Pacific", "type": "float"}}]}

    The heartbeat message is a simple plain text message with just a date stamp
    
    A "data" message contains an array of 2 elements.  The first element 
    contains a dictionary of (point name: value) pairs.  The second element
    contains context around the point data and the "Date" header.
'''
from datetime import datetime
import os
import sys

import json
import gevent
import logging
from gevent.core import callback

from volttron.platform import get_home, set_home
from volttron.platform.messaging import headers as headers_mod
from volttron.platform.vip.agent import Agent, PubSub, Core
from volttron.platform.agent import utils

# These are the options that can be set from the settings module.
from django.smartcity.vagent.settings import remote_url, topics_prefixes_to_watch, heartbeat_period

utils.setup_logging()
_log = logging.getLogger(__name__)

set_home()

class StandAloneListener(Agent):
    ''' A standalone version of the ListenerAgent'''

    @Core.receiver('onstart')
    def start(self, sender, **kwargs):
        '''Handle the starting of the agent.
        
        Subscribe to all points in the topics_prefix_to_watch tuple
        defined in settings.py.
        '''
        writer = '~~~~~~~~~~THIS IS SOME TEXT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

        sys.stdout.write(writer)

        now = datetime.utcnow().isoformat(' ') + 'Z'
        headers = {
            # 'AgentID': self._agent_id,
            headers_mod.CONTENT_TYPE: headers_mod.CONTENT_TYPE.PLAIN_TEXT,
            headers_mod.DATE: now,
        }

        self.vip.pubsub.publish(
            peer='pubsub',
            topic='/django/test',
            headers=headers,
            message=writer)

        exit(0)

if  __name__ == '__main__':
    try:
        # If stdout is a pipe, re-open it line buffered
        if utils.isapipe(sys.stdout):
            # Hold a reference to the previous file object so it doesn't
            # get garbage collected and close the underlying descriptor.
            stdout = sys.stdout
            sys.stdout = os.fdopen(stdout.fileno(), 'w', 1)
        
        print(remote_url())
        agent = StandAloneListener(address=remote_url(),
                                   identity='django')

        task = gevent.spawn(agent.core.run)
        try:
            task.join()
        finally:
            task.kill()
    except KeyboardInterrupt:
        pass