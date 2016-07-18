from ..util.temporal import sim2realtime as s2r

class Flow(object):
    """Defines a Flow that can be exported"""
    def __init__(self, start, dur, proto, sip, sp, dip, dp, iflags, uflags, pkt, oct):
        self.stime = start
        self.dur = dur
        self.etime = start + dur

        self.proto = proto
        self.sip = sip
        self.sp = sp
        self.dip = dip
        self.dp = dp
        self.iflags = iflags
        self.uflags = uflags
        self.pkt = pkt
        self.oct = oct

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (s2r(self.stime), s2r(self.etime), self.dur, self.proto,
                                                        self.sip, self.sp, self.dip, self.dp,
                                                        self.iflags, self.uflags, self.pkt, self.oct)

    @staticmethod
    def header():
        return 'stime|etime|dur|pro|sip|sp|dip|dp|iflags|uflags|pkt|oct'


