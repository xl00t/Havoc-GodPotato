# GodPotato script for Havoc C2

![Havoc Logo](https://github.com/HavocFramework/Havoc/blob/master/docs/logo.png)

## Description
This script is intended to facilitate usage of GodPotato exploit using Havoc `DotnetInlineExecute` feature.

## Installation
1. Go to your Havoc folder
2. `cd data/extensions/`
3. `git clone https://github.com/xl00t/Havoc-GodPotato && cd Havoc-GodPotato/`
4. `bash install.sh`
5. ![install1.png](assets/imgs/install1.png)
6. Click script manager
7. Click load script
8. And then choose GodPotato.py file.


## Usage
```
21/12/2023 17:50:09 [xl00t] Demon » help godpotato

 - Command       :  godpotato
 - Description   :  Inline Execute GodPotato in order to abuse SeImpersonatePrivilege and run commands as SYSTEM
 - Usage         :  godpotato -cmd "cmd /c command"
 - Example       :  godpotato -cmd "cmd /c whoami"
```