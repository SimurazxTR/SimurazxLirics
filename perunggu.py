import sys
import time
def jalan_lirik():
    lirik = [
        ("membawamu kesiniii", 0.1),
        ("kami pernah disitu", 0.1),
        ("di posisimuuu", 0.1),
        ("helakan kesanmuh", 0.1),

        ("diantara pusaran niiiiiiirfungsiiiiiii", 0.1),
        ("petakan semuaaaaaa lagiiii", 0.1),
        ("titiiiik tuju yang tlah terpati", 0.1),
        ("melamban bukanlah hal yaaaaaaaaaang tabuuuu", 0.1),
        ("kadang itu yang kau butuh", 0.1),
        ("bersandar hibahkan bebanmuuuuuuuuuu", 0.1),

    ]
    delay = [2.6, 2.0, 1.5, 6.5, 3.0, 2.5, 3.5, 4.5, 2.5,3.0]
    print("~perunggu 33x~")
    time.sleep(3)
    for i, (baris_lagu, delay_char) in enumerate(lirik):
         for char in baris_lagu:
             print(char, end='')
             sys.stdout.flush()
             time.sleep(delay_char)
         time.sleep(delay[i])
         print('')
    print("//Code By amekk")
jalan_lirik()