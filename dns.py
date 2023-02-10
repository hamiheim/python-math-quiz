#!/usr/bin/env python3

import socket
domain = "hamiheim.com"


def get_dns_records(domain):
    try:
        result = socket.getaddrinfo(domain, None)
        dns_records = []
        for item in result:
            dns_records.append(item[4][0])
        return dns_records
    except socket.gaierror:
        print("DNS lookup failed!")


get_dns_records(domain)
