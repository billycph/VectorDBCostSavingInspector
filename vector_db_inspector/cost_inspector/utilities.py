import sys

def print_header(text):
    print(f"\n\033[1m{text}\033[0m")
    print("=" * 60)

def print_warning(text):
    print(f"\033[93m[!] {text}\033[0m")

def print_success(text):
    print(f"\033[92m[+] {text}\033[0m")

def print_money(text):
    print(f"\033[92m\033[1m$$$ {text} $$$\033[0m")

def get_user_input(prompt, default=None):
    if default:
        user_in = input(f"{prompt} [{default}]: ")
        return user_in.strip() if user_in.strip() else default
    return input(f"{prompt}: ").strip()
