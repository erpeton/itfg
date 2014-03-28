import sys

if len(sys.argv) == 2:
    replay = open(sys.argv[1], "rb")

    replay.seek(158,0)
    get_seed1 = replay.read(1)
    seed1     = int(get_seed1.encode("hex"), 16)

    replay.seek(159,0)
    get_seed2   = replay.read(1)
    seed2       = int(get_seed2.encode("hex"), 16)

    seed = seed1 + 256*seed2

    replay.close()

    print seed
else:
    sys.exit('Usage: %s replay.itr' % sys.argv[0])
