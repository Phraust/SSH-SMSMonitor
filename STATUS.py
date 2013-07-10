#! /usr/bin/env python

from os import system
from socket import socket
from sys import argv
from time import asctime

from googlevoice import Voice
from googlevoice.util import input

def usage():
    print('%s <server-info> <phone-number>\n' % (argv[0]))
    print('\tphone-number\tphone number to send sms\n')

def tcp_test(server_info):
    cpos = server_info.find(':')
    if cpos < 1 or cpos == len(server_info) - 1:
        print('You need to give server info as hostname:port.')
        usage()
        return True
    try:
        sock = socket()
        sock.connect((server_info[:cpos], int(server_info[cpos+1:])))
        sock.close
        return True
    except:
        return False


def send_error(server_info, phone_number):
    voice = Voice()
    voice.login()

    text = server_info + ' NEEDS HELP. :('

    voice.send_sms(phone_number, text)
    voice.logout()

if __name__ == '__main__':
    if len(argv) != 3:
        print('Wrong number of arguments.')
        usage()
    elif not tcp_test(argv[1]):
        send_error(argv[1], argv[2])
