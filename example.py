from src.Chocopy import Chocopy

def onclick():
    choco.alert("You clicked a button!")

state = {
    "checked": 0
}

def onchange_checkbox(this):
    if state["checked"] == 0:
        this["setChecked"](1)
        state["checked"] = 1
    else:
        this["setChecked"](0)
        state["checked"] = 0

choco = Chocopy("My App", (400.0, 430.0), opaque=False)
choco.set_max_size((600.0, 680.0))
choco.button("This is a button", (10.0, 10.0), (120.0, 50.0), onclick=onclick)
choco.label("This is a big label", (10.0, 70.0), (100.0, 50.0), 20)
choco.textfield("This is text field", (50.0, 120.0), (150.0, 60.0))
choco.label("This is a small label", (10.0, 200.0), (100.0, 50.0))
choco.progress((10, 10), (100, 90), 100.00)
choco.slider((10, 250), (100, 50), 50.00)
choco.checkbox((10, 260), (150, 140), "Checkbox", onchange=onchange_checkbox)
choco.panel((100, 300), (120, 120), "panel1", border="etched")
choco.panel((300, 300), (90, 90), "panel2", border="normal")
choco.button("This is inside a panel", (10, 10), (100, 100), content_id="panel1")
choco.run()
