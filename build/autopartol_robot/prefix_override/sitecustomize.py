import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rosking/chapt7/chapt7_ws/install/autopartol_robot'
