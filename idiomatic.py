for i in range(6):
    print(i*i)


# Looping backwards

colors = ['red', 'green', 'blue']
for color in reversed(colors):
    print(color)


# Looping with indices

for i, color in enumerate(colors):
    print(i, '-->', color)


# Looping over 2 collections, could be diff length: izip over zip

names = ['a', 'b']
for name, color in izip(names, colors):
    print(name, '-->', color)

# Sorted order

for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)

print(sorted(colors, key=len))

# Call a function until a sentinel value

blocks = []

while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)


blocks = []

for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

# Distinguishing multiple exit points in loops

def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

# Looping over dictionary keys

for k in d:
    print(k)


for k, v in d.iteritems():
    print(k, '-->', v)

d = dict(izip(names, colors))
d = dict(enumerate(names))

# counting
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# grouping

d = defaultdict(list)

for name in names:
    key = len(name)
    d[key].append(name)

while d:
    key, value = d.popitem()
    print(key, '-->', value)

# Merge dict

d = ChainMap(d1, d2, d3)

# Use keyword argument

TestResults = namedtuple('TestResults', ['failed', 'attemptd'])

# Umpacking sequences => destructuring
# Simultanious update variables

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()


def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

# Context manager

with localcontext(Context(prec=50)):
    print(Decimal(355) / Decimal(113))

with open('data.txt') as f:
    data = f.read()

# Thread lock
with lock:
    print('Critical section 1')
    print('Critical section 2')

with ignored(OSError):
    os.remove('somefile.tmp')

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

with redirect_stdout(f):
    pass

@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = oldstdout

print(sume([i**2 for i in range(10)]))
print(sume(i**2 for i in range(10)))
