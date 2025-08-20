# password-strength-tool
# 🔐 Password Strength Analyzer & Wordlist Generator

A Python tool to analyze password strength and generate custom wordlists using user inputs. Perfect for ethical hacking, cybersecurity research, and password auditing.

## 🚀 Features

- Analyze password strength using `zxcvbn` and entropy
- Generate wordlists from names, pets, dates, etc.
- Includes leetspeak and year suffixes
- Export `.txt` wordlists for cracking tools
- CLI interface (GUI optional)

## 📦 Installation

``bash
pip install -r requirements.txt


 Usage
python password_tool.py --password "MyP@ssw0rd" --inputs Rohan Dog 2000 --output mylist.txt


