from colorama import Fore, Style

def success(msg):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")
    
def error(msg):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")
    
def warning(msg):
    print(f"{Fore.YELLOW}⚠️ {msg}{Style.RESET_ALL}")

def info(msg):
    print(f"{Fore.CYAN}ℹ️ {msg}{Style.RESET_ALL}")