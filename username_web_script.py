import webbrowser
import subprocess
import time

# enter path to preferred browser
env_variable = 'set Browser=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'


def set_env_variable(variable):
    subprocess.call(variable, shell=True)


def connect_user_main():
    username_list = raw_input("Enter usernames e.g. user1 user2 userN: ")
    username_list = username_list.split()
    for i in username_list:
        url = "www.test.com" + i + "%25&client=%25" + i + "%25"
        webbrowser.open_new_tab(url)
        time.sleep(3)


def connect_user_documents():
    username_list = raw_input("Enter usernames e.g. user1 user2 userN: ")
    username_list = username_list.split()
    for i in username_list:
        document_url = "www.test.com" + i + "%25&client=%25" + i + "%25"
        webbrowser.open_new_tab(document_url)
        time.sleep(3)


set_env_variable(env_variable)

menu = 1
while menu:
    print '###MENU###'
    print "1. Username main page"
    print "2. Username document page"
    print "3. Exit"
    meniu = raw_input("Enter selection: ")

    if meniu == '1':
        connect_user_main()
    if meniu == '2':
        connect_user_documents()
    if meniu == '3':
        menu = 0
