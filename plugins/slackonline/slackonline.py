from errbot import BotPlugin, botcmd


class Slackonline(BotPlugin):
    """
    Slackオンラインのゲームプラグイン
    """

    @botcmd  # flags a command
    def so(self, msg, args):  # a command callable with !so
        """
        Slackオンラインボットへの!soコマンド
        """

        self.log.info('きたよ')
        self.log.debug(msg)
        self.log.debug(args)
        self.log.debug(self.rooms())

        for room in self.rooms():
            self.log.debug(room)
            for occupant in room.occupants:
                self.log.debug(occupant)
                self.log.debug(occupant.username)

        return 'It *works* !'

    def my_callback(self):
        self.log.debug('I am called every minute')

    def activate(self):
        super().activate()
        self.start_poller(60, self.my_callback)
