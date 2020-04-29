import argparse
import sqlite3
import imageio
import cv2


def code():
    password = "danish"
    connect = input("Whats your Password\n")

    while connect != password:
        connect = input("Whats your Password\n")
        if connect == "q":
            break
    if connect == password:
        conn = sqlite3.connect('safe.db')
        try:
            conn.execute('''CREATE TABLE SAFE
                (FULL_NAME TEXT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                EXTENSION TEXT NOT NULL,
                FILES TEXT NOT NULL);''')
            print("Your safe has been created!\nWhat would you like to store in it today?")
        except:
            print("You have a safe, what would you like to do today?")
    while True:
        print("\n" + "*" * 15)
        print("Commands:")
        print("q = quit program")
        print("o = open file")
        print("s = store file")
        print("*" * 15)
        input_ = input(":")

        if input_ == "q":
            break
        if input_ == "o":
            # open the file
            file_type = input("What is the filetype of the file you want to open?\n")
            file_name = input("What is the name of the file you want to open?\n")
            FILE_ = file_name + "." + file_type

            cursor = conn.execute("SELECT * from SAFE WHERE FULL_NAME=" + '"' + FILE_ + '"')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("password",help="The password to create the database and to create the database",type=str)
    parser.add_argument("-o", "--output", help="Output result for the file", action="store_true")
    args = parser.parse_args()
    res = code()

if __name__ == "__main__":
    main()
