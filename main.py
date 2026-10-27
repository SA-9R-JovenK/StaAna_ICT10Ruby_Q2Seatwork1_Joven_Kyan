from pyscript import document

def candidate_checker(e):
    classes = [
        "SCOUT",
        "SOLDIER",
        "PYRO",
        "DEMOMAN",
        "HEAVY",
        "ENGINEER",
        "MEDIC",
        "SNIPER",
        "SPY"
    ]
    name = document.getElementById("name").value.strip()
    class_checker = name.upper() in classes
    messages = (f"INTRUDER ALERT! ENEMY {name.upper()} IN THE BASE!",f"{name.upper()} registered... Mission Begins in 30 Seconds."
    )

    document.getElementById("result").innerHTML = messages[class_checker]