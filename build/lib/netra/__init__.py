from pkg_resources import resource_filename


def netra_crt():
    return resource_filename(__name__, "ssl/netra.crt")

def netra_key():
    return resource_filename(__name__, "ssl/netra.key")

def netra_pem():
    return resource_filename(__name__, "ssl/keypair.pem")
