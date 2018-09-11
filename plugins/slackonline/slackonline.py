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

        print
        return 'It *works* !'
