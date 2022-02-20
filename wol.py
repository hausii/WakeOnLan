#!/usr/bin/env python
# wol.py

import socket
import struct
import yaml


def wake_on_lan(MAC_address):
    """ Switches on remote computers using WOL. """

    # Check the MAC address format and try to compensate.
    if len(MAC_address) == 12:
        pass
    elif len(MAC_address) == 12 + 5:
        MAC_address = MAC_address.replace(MAC_address[2], '')
    else:
        raise ValueError('Incorrect MAC address format')

    # Pad the synchronization stream.
    data = ''.join(['FFFFFFFFFFFF', MAC_address * 20])
    send_data = b''

    # Split up the hex values and pack.
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data,
                              struct.pack('B', int(data[i: i + 2], 16))])

    # Broadcast it to the LAN.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, ('<broadcast>', 7))


if __name__ == '__main__':
    with open("wol_config.yml", "r") as stream:
        try:
            conf = yaml.safe_load(stream)
            for key in conf:
                wake_on_lan(conf[key]['MAC_address'])
                print(conf[key]['hostname'], 'should be awake now')
        except yaml.YAMLError as exc:
            print(exc)
