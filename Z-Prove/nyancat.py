#   0 = Nero       8 = Grigio
#    1 = Blu scuro        9 = Blu
#    2 = Verde       A = Verde limone
#    3 = Verde acqua        B = Azzurro
#    4 = Bordeaux         C = Rosso
#    5 = Viola      D = Fucsia
#    6 = Verde oliva      E = Giallo
#    7 = Grigio chiaro       F = Bianco
import os
import time

i=0
while True:
   os.system("color 0C")
   os.system("color 0E")
   os.system("color 0A")
   os.system("color 0B")
   os.system("color 09")
   os.system("color 0D")
   #os.system("start nyancat.py")
   #break
   time.sleep(0.025)
   os.system("cls")
   print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠛⠂⠀⠀⢰⠇⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⣰⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⣀⣀⡀⠀⠀
⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⠀⠀⢰⡇⠀⣿⠁⠀⠉⠻⣦⡀⠠⠟⠀⠀⠀⠀⣿⣧⣶⠿⠛⠙⣿⠀⠀
⣿⡋⠉⠙⠛⠷⣦⣄⠀⠀⣿⡇⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠈⠻⣦⣀⣀⣀⣀⣰⣿⠟⠁⠀⠀⠀⣿⠀⠀
⠸⣷⡀⠀⠀⠀⠈⠛⣷⡄⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⣿⡀⠀
⠀⠘⢿⣆⠀⠀⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠀⠐⠟⠀⠀⠀⠀⡀⠀⢀⣴⡿⠃⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠙⣷⡄
⠀⠀⠀⠙⢷⣤⡀⠀⠀⠈⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠇⠀⣼⡏⠀⠀⠀⠀⣾⣅⣀⣿⠀⠀⠀⠀⠀⠀⠀⣾⣅⢈⣷⠀⠀⠈⣿
⠀⠀⠀⠀⠀⠙⠿⣦⣀⠀⢸⡇⠀⠀⠀⠀⣰⡄⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠘⠻⠿⠟⠀⠀⠠⣖⢒⡶⠀⠙⠿⠿⠟⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣾⡇⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⢈⣏⠀⠀⠀⠀⡀⠀⠀⠀⢀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠀⠀⠀⠠⡆⠀⠀⠀⢰⡆⠀⠀⢻⣧⡀⠀⠀⠀⠀⠈⠻⠶⣤⡴⠟⠙⠶⣤⡤⠞⠁⠀⠀⢀⣾⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣧⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣙⣿⣶⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣶⠿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠉⠉⠛⣿⠛⢻⠿⠿⠿⠿⣿⡿⠿⠛⠛⠛⠛⠛⣿⠛⠉⠙⠛⣿⠛⠛⣿⠟⠛⠛⢻⡏⠉⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⣀⣤⡾⠃⠀⣿⣀⣀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⢿⣄⣀⣀⣴⠟⠀⠀⣿⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠙⠷⠶⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀
""")
   time.sleep(0.025)
   os.system("cls")
   print("""
         
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠛⠂⠀⠀⢰⠇⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⣰⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⣀⣀⡀⠀⠀
⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⠀⠀⢰⡇⠀⣿⠁⠀⠉⠻⣦⡀⠠⠟⠀⠀⠀⠀⣿⣧⣶⠿⠛⠙⣿⠀⠀
⣿⡋⠉⠙⠛⠷⣦⣄⠀⠀⣿⡇⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠈⠻⣦⣀⣀⣀⣀⣰⣿⠟⠁⠀⠀⠀⣿⠀⠀
⠸⣷⡀⠀⠀⠀⠈⠛⣷⡄⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⣿⡀⠀
⠀⠘⢿⣆⠀⠀⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠀⠐⠟⠀⠀⠀⠀⡀⠀⢀⣴⡿⠃⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠙⣷⡄
⠀⠀⠀⠙⢷⣤⡀⠀⠀⠈⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠇⠀⣼⡏⠀⠀⠀⠀⣾⣅⣀⣿⠀⠀⠀⠀⠀⠀⠀⣾⣅⢈⣷⠀⠀⠈⣿
⠀⠀⠀⠀⠀⠙⠿⣦⣀⠀⢸⡇⠀⠀⠀⠀⣰⡄⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠘⠻⠿⠟⠀⠀⠠⣖⢒⡶⠀⠙⠿⠿⠟⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣾⡇⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⢈⣏⠀⠀⠀⠀⡀⠀⠀⠀⢀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠀⠀⠀⠠⡆⠀⠀⠀⢰⡆⠀⠀⢻⣧⡀⠀⠀⠀⠀⠈⠻⠶⣤⡴⠟⠙⠶⣤⡤⠞⠁⠀⠀⢀⣾⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣧⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣙⣿⣶⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣶⠿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠉⠉⠛⣿⠛⢻⠿⠿⠿⠿⣿⡿⠿⠛⠛⠛⠛⠛⣿⠛⠉⠙⠛⣿⠛⠛⣿⠟⠛⠛⢻⡏⠉⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⣀⣤⡾⠃⠀⣿⣀⣀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⢿⣄⣀⣀⣴⠟⠀⠀⣿⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠙⠷⠶⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀
""")
   