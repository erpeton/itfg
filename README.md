**Floor generator**

Very simple program to generate floors for given seed (compatibel with Icy Tower 1.4/1.5)

**Screenshots**

<img src='https://raw.github.com/erpeton/itfg/master/floor.png'/>

**Requirements**

* python 2.5.2 (or higher)
* pygame 1.7.1 (or higher)

**Usage**

    # if you don't know replay seed, you can run get_seed.py to get it
    $ python get_seed.py Boru_1079666_1051_1034.itr 
    $ 9639

    # edit floor_generator.py, set variables:
    # seed        = 9639
    # begin_floor = 0
    # end_floor   = 170
    # moverate    = 10

    # run floor_generator.py
    $ python floor_generator.py
