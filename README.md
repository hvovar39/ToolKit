# ToolKit
A tool kit full of useful pentesting free, and for most of them open source, tools.
This list is not intended to be exhaustive, but useful: only tool we are using ;)

## Table Of Content

- [ToolKit](#toolkit)
  - [Table Of Content](#table-of-content)
- [Recon](#recon)
  - [OSINT](#osint)
  - [DNS](#dns)
- [Scanning](#scanning)
  - [Network](#network)
  - [Web](#web)
- [Exploit](#exploit)
  - [Web](#web-1)
  - [Usefull websites](#usefull-websites)
  - [Frameworks](#frameworks)
- [Post-exploit](#post-exploit)
  - [Privilege escalation](#privilege-escalation)
  - [Windows](#windows)
- [Crypto](#crypto)
  - [Wordlist](#wordlist)
  - [Pasword cracking](#pasword-cracking)
- [Homemade scripts](#homemade-scripts)
  - [Crypto](#crypto-1)


# Recon

## OSINT
- **[The Harvester](https://github.com/laramies/theHarvester)**: A CLI data harvester ( emails, names, subdomains, IPs and URLs )
- **[Metagoofil](https://github.com/opsdisk/metagoofil)**: A CLI public document collector using google Dork
- **[ExifTool](https://exiftool.org/)**: A CLI metadata extractor
- **[Google Dorking](https://github.com/hvovar39/ToolKit/blob/main/CheatSheet/%5Bcheetsheat%5DGoogle_dorking.md)**: Google Dorking cheatsheet
- **[Shodan](https://www.shodan.io/)**: IoT search engine
- **[Thingful](https://www.thingful.net/)**: Iot search engine

## DNS
- **[Netcraft](https://searchdns.netcraft.com/)**: Online sub-domains ennumeration
- **[Sublist3r](https://github.com/aboul3la/Sublist3r)**: CLI sub-domains ennumeration tool
- **[DNSEnum](https://github.com/SparrowOchon/dnsenum2)**: multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.


# Scanning

## Network
- **[Nmap](https://nmap.org/)**: The classic network scanner.
  - [[CheatSheer]Nmap.md](CheatSheet/[CheatSheet]Nmap.md)
- **[Masscan](https://github.com/robertdavidgraham/masscan)**: This is an Internet-scale port scanner.

## Web
- **[WPScan](https://github.com/wpscanteam/wpscan)**: Vulnerability scanner fot WordPress website
- **[OpenVAS](https://github.com/greenbone/openvas-scanner)**: Website vulnerability scanner


# Exploit

## Web
- **[JWT_tools](https://github.com/ticarpi/jwt_tool)**: JWT offline manipulation tool.
- **[BeEF](https://beefproject.com/)**: A browser exploitation framework.
- **[BurpSuite](https://portswigger.net/burp/communitydownload)**: Web proxy and attack tool. 
- **[ZAP](https://www.zaproxy.org/)**: OWASP browser proxy.

## Usefull websites
- **[Exploit-db](https://www.exploit-db.com/)**: An online exploit database
- **[CVE Details](https://www.cvedetails.com/)**: An online CVE database

## Frameworks
- **[Metasploit](https://www.metasploit.com/)**: The infamous exploit framework
  - [[CheatSheet]Metasploit.md](CheatSheet/[CheatSheet]Meatsploit.md


# Post-exploit

## Privilege escalation
- **[PEASS-ng](https://github.com/carlospolop/PEASS-ng)**: Privilege escalation tools for Windows and Linux/Unix* and MacOS.
  - [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS): Privilege escalation vulnerability scanner for linux.
  - [WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS): Privilege escalation vulnerability scanner for Windows.

## Windows
- **[Mimikatz](https://github.com/gentilkiwi/mimikatz)**: Credentials dumping tool.
- **[PowerShell Empire](https://github.com/BC-SECURITY/Empire)**: Empire is a post-exploitation and adversary emulation framework that is used to aid Red Teams and Penetration Testers.
- **[LOLBAS](https://lolbas-project.github.io)**: Living Off The Land Binaries, Scripts and Libraries.


# Crypto

## Wordlist
- **[CeWL](https://github.com/digininja/CeWL)**: A CLI Wordlist generator. Generate custom wordlist from a URL or a domain
- **[SecLists](https://github.com/danielmiessler/SecLists)**: A github repo with lots of Wordlist
- **[Weakpass](https://weakpass.com/): For any kind of bruteforce find wordlists...

## Pasword cracking
- **[Hashcat](https://hashcat.net/hashcat/)**: Password cracker.
- **[John](https://github.com/openwall/john)**: Password cracker.
- **[OneRuleToRuleThemAll](https://github.com/NotSoSecure/password_cracking_rules)**: A maxi rule file for mutating password list.


# Homemade scripts

## Crypto
- **[length_to_morse](https://github.com/hvovar39/ToolKit/blob/main/Crypto/length_to_morse.py)**: Get morse code from the length of the word of the given .txt
