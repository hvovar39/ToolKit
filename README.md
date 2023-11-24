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
    - [Active Directory](#active-directory)
  - [Crypto](#crypto)
    - [Wordlist](#wordlist)
    - [Pasword cracking](#pasword-cracking)
  - [Reverse Engineering](#reverse-engineering)
    - [Disassembler and Decompiler](#disassembler-and-decompiler)
    - [Debugging](#debugging)
  - [Homemade scripts](#homemade-scripts)
    - [Crypto](#crypto-1)

## Recon

### OSINT

- **[The Harvester](https://github.com/laramies/theHarvester)**: A CLI data harvester ( emails, names, subdomains, IPs and URLs )
- **[Metagoofil](https://github.com/opsdisk/metagoofil)**: A CLI public document collector using google Dork
- **[ExifTool](https://exiftool.org/)**: A CLI metadata extractor
- **[Google Dorking](https://github.com/hvovar39/ToolKit/blob/main/CheatSheet/%5Bcheetsheat%5DGoogle_dorking.md)**: Google Dorking cheatsheet
- **[Shodan](https://www.shodan.io/)**: IoT search engine
- **[Thingful](https://www.thingful.net/)**: Iot search engine

### DNS

- **[Netcraft](https://searchdns.netcraft.com/)**: Online sub-domains ennumeration
- **[Sublist3r](https://github.com/aboul3la/Sublist3r)**: CLI sub-domains ennumeration tool
- **[DNSEnum](https://github.com/SparrowOchon/dnsenum2)**: multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.

## Scanning

### Network

- **[Nmap](https://nmap.org/)**: The classic network scanner.
  - [[CheatSheet]Nmap.md](CheatSheet/[CheatSheet]Nmap.md)
- **[Masscan](https://github.com/robertdavidgraham/masscan)**: This is an Internet-scale port scanner.

### Web

- **[WPScan](https://github.com/wpscanteam/wpscan)**: Vulnerability scanner fot WordPress website
- **[OpenVAS](https://github.com/greenbone/openvas-scanner)**: Website vulnerability scanner
- **[Feroxbuster](https://github.com/epi052/feroxbuster)**: Feroxbuster is a Rust based tool designed to perform Forced Browsing.

## Exploit

### Web

- **[JWT_tools](https://github.com/ticarpi/jwt_tool)**: JWT offline manipulation tool.
- **[BeEF](https://beefproject.com/)**: A browser exploitation framework.
- **[BurpSuite](https://portswigger.net/burp/communitydownload)**: Web proxy and attack tool.
- **[ZAP](https://www.zaproxy.org/)**: OWASP browser proxy.

### Usefull websites

- **[Exploit-db](https://www.exploit-db.com/)**: An online exploit database
- **[CVE Details](https://www.cvedetails.com/)**: An online CVE database

### Frameworks

- **[Metasploit](https://www.metasploit.com/)**: The infamous exploit framework
  - [[CheatSheet]Metasploit.md](CheatSheet/[CheatSheet]Meatsploit.md)

## Post-exploit

### Privilege escalation

- **[PEASS-ng](https://github.com/carlospolop/PEASS-ng)**: Privilege escalation tools for Windows and Linux/Unix* and MacOS.
  - [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS): Privilege escalation vulnerability scanner for linux.
  - [WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS): Privilege escalation vulnerability scanner for Windows.
- **[GTFOBins](https://gtfobins.github.io/)**: A database of linux binaries that can be abuse to elevate privileges and/or escape restricted environments.

### Windows

- **[Mimikatz](https://github.com/gentilkiwi/mimikatz)**: Credentials dumping tool.
- **[PowerShell Empire](https://github.com/BC-SECURITY/Empire)**: Empire is a post-exploitation and adversary emulation framework that is used to aid Red Teams and Penetration Testers.
- **[LOLBAS](https://lolbas-project.github.io)**: Living Off The Land Binaries, Scripts and Libraries.
- **[PowerSploit](https://github.com/PowerShellMafia/PowerSploit)**: A collection of Microsoft PowerShell modules that can be used to aid penetration testers during all phases of an assessment.
- **[Evil-winrm](https://github.com/Hackplayers/evil-winrm)**: Winrm shell ++

### Active Directory

- **[BloodHound](https://github.com/BloodHoundAD/BloodHound)**: BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory or Azure environment.
- **[CrackMapExec](https://github.com/Porchetta-Industries/CrackMapExec)**: CrackMapExec is a swiss army knife for pentesting Windows/Active Directory environments.

## Crypto

### Wordlist

- **[CeWL](https://github.com/digininja/CeWL)**: A CLI Wordlist generator. Generate custom wordlist from a URL or a domain
- **[SecLists](https://github.com/danielmiessler/SecLists)**: A github repo with lots of Wordlist
- **[Weakpass](https://weakpass.com/)**: For any kind of bruteforce find wordlists...

### Pasword cracking

- **[hash-identifier](https://github.com/blackploit/hash-identifier)**: CLI python hash identifier.
- **[Hashcat](https://hashcat.net/hashcat/)**: Password cracker.
- **[John](https://github.com/openwall/john)**: Password cracker.
- **[OneRuleToRuleThemAll](https://github.com/NotSoSecure/password_cracking_rules)**: A maxi rule file for mutating password list.

## Reverse Engineering

### Disassembler and Decompiler

- **[Ghidra](https://ghidra-sre.org/)**: NSA open-source disassemble/decompiler written in Java.
- **[IDA](https://www.hex-rays.com/ida-free/)**: Proprietary disassembler/decompiler base on plugins.

### Debugging

- **[GDB](https://www.sourceware.org/gdb/)**: Well ... lets start with the basics.
- **[PEDA](https://github.com/longld/peda)**: Python Exploit Development Assistance for GDB is a handfull set of usefull gdb improvement.
- **[objdump](https://linux.die.net/man/1/objdump)**: command line utilies to display informations about object files.
- **[ImmunityDebugger](https://www.immunityinc.com/products/debugger/)**: A GUI debugger usefull on windows, with a python script engine.
- **[Mona](https://github.com/corelan/mona)**: Mona.py is a python script that can be used to automate and speed up specific searches while developing exploits (typically for the Windows platform).

## Homemade scripts

### Crypto

- **[length_to_morse](https://github.com/hvovar39/ToolKit/blob/main/Crypto/length_to_morse.py)**: Get morse code from the length of the word of the given .txt
