import ipaddress


def is_valid_ipv4(ipv4):
    try:
        ipaddress.IPv4Address(ipv4)
        return True
    except ipaddress.AddressValueError:
        return False


print(is_valid_ipv4("192.168.1.1"))
