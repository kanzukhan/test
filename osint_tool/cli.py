import argparse
import json
from colorama import Fore, Style, init
from .modules import (
    ipinfo,
    hibp,
    domain_info,
    github_user,
    subdomains,
    solana,
)

MODULES = {
    "ipinfo": ipinfo.lookup,
    "hibp": hibp.lookup,
    "domain": domain_info.lookup,
    "github": github_user.lookup,
    "subdomains": subdomains.lookup,
    "solana": solana.lookup,
}

BANNER = f"""{Fore.CYAN}
 ____                        ____           _ 
|  _ \ ___  ___ ___  _ __   |  _ \ ___  ___| |
| |_) / _ \/ __/ _ \| '_ \  | |_) / _ \/ __| |
|  _ <  __/ (_| (_) | | | | |  _ <  __/ (__| |
|_| \_\___|\___\___/|_| |_| |_| \_\___|\___|_|
{Style.RESET_ALL}"""


def main():
    init()  # colorama
    print(BANNER)

    parser = argparse.ArgumentParser(description="ReconRad OSINT multitool")
    parser.add_argument("module", choices=MODULES.keys(), help="Module to run")
    parser.add_argument(
        "query", help="Query term (IP, email, user, domain, or address)"
    )
    args = parser.parse_args()

    func = MODULES[args.module]
    data = func(args.query)
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
