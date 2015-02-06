import re
import znc


class BitlbeeTweaks(znc.Module):
    description = "Helpful tweaks for Bitlbee"
    module_types = [znc.CModInfo.NetworkModule]

    def OnChanMsg(self, nick, chan, msg):
        if nick.GetNick() == "root" and re.search("Message from unknown participant", msg.s):
            matches = re.match("Message from unknown participant ([^:]+): ", msg.s).groups()
            if matches:
                new_msg = re.sub("^[^:]+:", "", msg.s)
                self.PutUser(":{0}!{1}@{2} PRIVMSG {3} :{4}".format(
                    re.sub(' +', '', matches[0]),
                    nick.GetIdent(),
                    nick.GetHost(),
                    chan,
                    new_msg
                ))
                return znc.HALTCORE
