import distribution as db
from ..flow import flow

class Generator(object):
    def __init__(self, env, profile, source_ip):
        """
        A flow generator based on probability distributions (cumulative density function)
        :param profile: The path to the .info file.
        """

        # Maybe in the future make this a distribution.
        self.sip = source_ip

        # GENERATORS (initialize)
        self.mk_dip = None      # destination ip
        self.mk_sp = None       # source port
        self.mk_dp = None       # destination port

        self.mk_ppf = None      # packets per flow
        self.mk_bpp = None      # bytes per packet

        self.mk_dur = None      # duration

        self.mk_proto = None    # protocol

        self.generate_response = False
        self.mk_rprob = None    # response probability
        self.mk_rdelay = None   # response delay
        self.mk_rppf = None     # response packets per flow
        self.mk_rbpp = None     # response bytes per packet

        self.flow = self.mk_flow(env)


    def mk_flow(self, env):
        while True:
            sip = self.sip
            dip = next(self.mk_dip)
            sp = next(self.mk_sp)
            dp = next(self.mk_dp)

            dur = next(self.mk_dur)

            proto = next(self.mk_proto)

            pkt = next(self.mk_ppf)
            oct = int(next(self.mk_bpp) * pkt)

            if self.generate_response:
                rprob = next(self.mk_rprob)
                rdelay = next(self.mk_rdelay)
                rppf = next(self.mk_rppf)
                rbpp = next(self.mk_rbpp)

            yield flow.Flow(env.now, dur, proto, sip, sp, dip, dp, proto, iflags, uflags, pkt, oct)


