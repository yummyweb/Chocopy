import src.Chocopy
from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

choco = src.Chocopy.Chocopy("Simple Screen", (500.0, 470.0))
choco.label("Simple Screen", (150.0, 350.0), (200.0, 50.0), 30)
choco.button("Simple Button", (190.0, 250.0), (120.0, 50.0))
choco.run()
