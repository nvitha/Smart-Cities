import sys
import os
from datetime import datetime

from volttron.platform.vip.agent import Agent, Core, PubSub, RPC
from volttron.platform.messaging import headers as headers_mod
from volttron.platform.agent import utils
from settings import remote_url, topics_prefixes_to_watch, heartbeat_period

import gevent

# utils.setup_logging()
# _log = logging.getLogger(__name__)

class TesterAgent(Agent):

    @Core.receiver('onstart')
    def onstart(self, sender, **kwargs):

        writer = 'Start thrashing test.'

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

        exit(1)

    @PubSub.subscribe('pubsub', '')
    def on_match(self, peer, sender, bus,  topic, headers, message):
        pass


# def main():
#     print(remote_url())
#     agent = TesterAgent(address=remote_url(), identity='django_test')
#     task = gevent.spawn(agent.core.run)
#     task.join()


def remote():
    try:
        # If stdout is a pipe, re-open it line buffered
        # if utils.isapipe(sys.stdout):
        #     # Hold a reference to the previous file object so it doesn't
        #     # get garbage collected and close the underlying descriptor.
        #     stdout = sys.stdout
        #     sys.stdout = os.fdopen(stdout.fileno(), 'w', 1)

        print(remote_url())
        agent = TesterAgent(address=remote_url(),
                                   identity='django')
        task = gevent.spawn(agent.core.run)
        try:
            task.join()
        finally:
            task.kill()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    try:
        # If stdout is a pipe, re-open it line buffered
        # if utils.isapipe(sys.stdout):
        #     # Hold a reference to the previous file object so it doesn't
        #     # get garbage collected and close the underlying descriptor.
        #     stdout = sys.stdout
        #     sys.stdout = os.fdopen(stdout.fileno(), 'w', 1)

        print(remote_url())
        agent = TesterAgent(address=remote_url(),
                                   identity='django')
        task = gevent.spawn(agent.core.run)
        try:
            task.join()
        finally:
            task.kill()
    except KeyboardInterrupt:
        pass