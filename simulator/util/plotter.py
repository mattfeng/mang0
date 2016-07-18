import seaborn as sns
import colors

sns.set_style('whitegrid')
DATASET = ''
cgen = colors.colorgen('rainbow', UNIQ_COLORS=12)

def dataset(s):
    global DATASET
    DATASET = s

def label(xl='time (s)', yl='', t=''):
    sns.plt.xlabel(xl)
    sns.plt.ylabel(yl)
    sns.plt.title(t + '\nDataset: %s' % DATASET)

def plot_dict(d):
    if isinstance(d, list):
        for di in d:
            sns.plt.plot(di.keys(), di.values(), lw=0.5, color=next(cgen))
    else:
        sns.plt.plot(d.keys(), d.values(), lw=0.5, color=next(cgen))

def plot_ts(d, ts):
    """Plot a timeseries (ts)"""
    if isinstance(d, list):
        for di in d:
            sns.plt.plot(ts, di, lw=0.5, color=next(cgen))
    else:
        sns.plt.plot(ts, d, lw=0.5, color=next(cgen))

def l(s):
    if s == 'bpp':
        label(yl='number of bytes', t='Bytes Per Packet (bpp) Time Series')
    elif s == 'ppf':
        label(yl='number of packets', t='Packets Per Flow (ppf) Time Series')
    elif s == 'sipps':
        label(yl='number of ips', t='Unique Source IPs (sipps) Time Series')
    elif s == 'pps':
        label(yl='number of packets', t='Packets Per Second (pps) Time Series')
    elif s == 'bps':
        label(yl='number of bytes', t='Bytes Per Second (bps) Time Series')
    elif s == 'dur':
        label(yl='frequency', t='Flow Durations (dur) (in seconds)')

def p(d):
    plot_dict(d)