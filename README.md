# ReconRad

ReconRad is a colorful command line interface for performing a variety of
Open Source Intelligence (OSINT) tasks using free APIs. The tool is written in
Python and ships with several modules that can easily be extended.

## Features

- **IP information** via [ipinfo.io](https://ipinfo.io)
- **Breach lookup** via [Have I Been Pwned](https://haveibeenpwned.com)
- **Domain search** via [domainsdb.info](https://domainsdb.info)
- **GitHub user info** via the public GitHub API
- **Subdomain enumeration** via [hackertarget.com](https://hackertarget.com)
- **Solana wallet lookup** via the public Solscan API

## Usage

```bash
python -m osint_tool.cli <module> <query>
```

Available modules:

- `ipinfo` – lookup information about an IP address
- `hibp` – check if an email account has been breached (requires `HIBP_KEY`)
- `domain` – search for registered domains
- `github` – fetch information about a GitHub user
- `subdomains` – list subdomains of a domain
- `solana` – inspect a Solana wallet address

For example:

```bash
export HIBP_KEY=your_api_key
python -m osint_tool.cli ipinfo 8.8.8.8
```

## Installation

Run the included setup script to install dependencies (requires internet
access):

```bash
./setup.sh
```

## License

See [LICENSE.md](LICENSE.md) for license information.
