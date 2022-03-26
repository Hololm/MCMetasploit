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

The program will ask for a specific directory. The start directory is in the Holographic Displays plugin folder located at ``./plugins/Holographic Displays``. By using ``../`` one time, it will go back to the plugins folder located ``./plugins``. Another ``../`` and you'll be in the default Minecraft server folder where all files are located.
