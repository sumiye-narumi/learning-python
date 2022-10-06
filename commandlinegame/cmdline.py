#ohohoh >.> borg drones.. like you gotta manage a cube of drones (That are all malfunctioning for some reason)
#Hunk of broken ship drifting and someone or somethin gets a to close and gibs oppertunity to repair engines

"""

playerStats: = {
    sheilds_cur: Int
    sheilds_max: Int
    structure_cur: Int
    structure_max: Int
    speed_cur: Int
    speed_max: Int
    drones_total: list[0, 10, 20]
    drone_free: list[0, 10, 20]
    power_cur: Int
    power_max: Int
    materials_cur: Int
    materials_max: Int
    powerCoreSmall_cur: Int
    powerCoreSmall_max: Int
    powerCoreBig_cur: Int
    powerCoreBig_max: Int

    }

"""
#Base Drone turns into Repair drone / Combat drone /
#Materials = Misc metals ETC ETC
#Power Cores small = Drone cores
#Power Cores big = Ship cores

import inquirer

iq = inquirer

questions = [
    iq.Text(name='idRequest', message="Emergency power-up detected, state your designation"),
    iq.Text(name='idConfirm', message="Welcome {name}")
]

answers = inquirer.prompt(questions)