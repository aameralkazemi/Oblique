from game import TheGame
ob = TheGame()
while ob.running:
    ob.current_menu.display()
    ob.loop()