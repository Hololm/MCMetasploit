# MCMetasploit

MCMetasploit is a project intended to scan for vulnerabilities in a Minecraft server using a headless client.

Currently, there are three exploits with more to be added in the future.

Note that this program only works with unmigrated accounts. If you migrated your account to Microsoft, it will not work.

## How to Use

Create a ``.env`` file and write
```
EMAIL=<Email>
PASSWORD=<Password>
```
This is so your client can log in to execute the exploit.

![image](https://user-images.githubusercontent.com/71950247/160255222-2dc73f09-67e6-435f-8e1d-d35e7c2e9297.png)

Choose from the table above with the specified **ID**. You will be asked to input a **server ip** and **port**.

## Holographics

The module will ask for a specific directory. The start directory is in the Holographic Displays plugin folder located at ``./plugins/Holographic Displays``. By using ``../`` one time, it will go back to the plugins folder located ``./plugins``. Another ``../`` and you'll be in the default Minecraft server folder where all files are located.

## Litebans

This module will ask for a SQL query in relation to the Litebans DB.

The schema for the DB is:
- litebans_bans
- litebans_history
- litebans_kicks
- litebans_mutes
- litebans_servers
- litebans_sync
- litebans_warnings

The command executed (/litebans sqlexec <query>) parses the query, and executes it, sending the results in a table format in that.

Example:
```
[22:31:26] [Client thread/INFO]: [CHAT] +--+-----------------------+---------+------------------------------------+------------+
[22:31:26] [Client thread/INFO]: [CHAT] |ID|DATE                   |NAME     |UUID                                |IP          |
[22:31:26] [Client thread/INFO]: [CHAT] +--+-----------------------+---------+------------------------------------+------------+
[22:31:26] [Client thread/INFO]: [CHAT] |1 |2022-03-17 13:22:38.924|CONSOLE  |CONSOLE                             |#           |
[22:31:26] [Client thread/INFO]: [CHAT] +--+-----------------------+---------+------------------------------------+------------+
[22:31:26] [Client thread/INFO]: [CHAT] |2 |2022-03-17 13:24:39.78 |Dog      |4fd3a2a8-bfe6-4144-94ac-bd04bb2e505b|127.0.0.1   |
[22:31:26] [Client thread/INFO]: [CHAT] +--+-----------------------+---------+------------------------------------+------------+
[22:31:26] [Client thread/INFO]: [CHAT] |3 |2022-03-17 13:25:58.758|cat      |8b476e65-a1c9-4677-867b-6712382c537f|127.0.0.1   |
[22:31:26] [Client thread/INFO]: [CHAT] +--+-----------------------+---------+------------------------------------+------------+
```

# Log4J

This module is a POC for CVE-2021-44228. This allows remote code execution on vulnerable java applications. Simply start the module, and it will return a shell from a victim.

# Adding more modules

If you would like to add more modules for yourself, or the project, simply make a new python file in the modules folder. Make a new class and name it Exploit, with it being a child class of BaseExploit. This child class provides base functionality for writing exploit modules. Pass through the client parent class parameter, and start writing away. Use our modules (especially holographics) for examples on how to write a module.
