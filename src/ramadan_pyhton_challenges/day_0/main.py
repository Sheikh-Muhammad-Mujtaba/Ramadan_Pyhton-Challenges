import random


# ANSI Escape Codes for Colors
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    
def display_banner():
    """
    Display a colorful banner for the Reverse Shell Generator.
    """
    banner = f"""
{Colors.RED}███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗{Colors.RESET}           
{Colors.RED}████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗{Colors.RESET}          
{Colors.RED}██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝{Colors.RESET}          
{Colors.RED}██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗{Colors.RESET}          
{Colors.RED}██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║{Colors.RESET}          
{Colors.MAGENTA}╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝{Colors.RESET}          
                                                                
{Colors.GREEN} ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗███╗   ██╗ ██████╗{Colors.RESET} 
{Colors.GREEN}██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔════╝ {Colors.RESET}
{Colors.GREEN}██║  ███╗██║   ██║█████╗  ███████╗███████╗██║██╔██╗ ██║██║  ███╗{Colors.RESET}
{Colors.GREEN}██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██║██║╚██╗██║██║   ██║{Colors.RESET}
{Colors.GREEN}╚██████╔╝╚██████╔╝███████╗███████║███████║██║██║ ╚████║╚██████╔╝{Colors.RESET}
{Colors.MAGENTA} ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ {Colors.RESET}
                                                                
{Colors.CYAN} ██████╗  █████╗ ███╗   ███╗███████╗{Colors.RESET}                            
{Colors.CYAN}██╔════╝ ██╔══██╗████╗ ████║██╔════╝{Colors.RESET}                            
{Colors.CYAN}██║  ███╗███████║██╔████╔██║█████╗ {Colors.RESET}                             
{Colors.CYAN}██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  {Colors.RESET}                            
{Colors.CYAN}╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗ {Colors.RESET}                           
{Colors.MAGENTA} ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ {Colors.RESET}                           
                                                                
{Colors.BOLD}{Colors.CYAN}Welcome to the number guessing game!{Colors.RESET}
{Colors.BOLD}{Colors.YELLOW}Author: XD$4{Colors.RESET}
{Colors.BOLD}{Colors.GREEN}For Fun Purposes Only 😉!{Colors.RESET}
    """
    print(banner)




def num_guessing_game():
    """
    Number Guessing Game
    """
chances = 5
guess_count = 0
number_to_guess = random.randrange(50, 100)
display_banner()
print(f"{Colors.BOLD}{Colors.BLUE}I'm thinking of a number between 50 and 100 🤔{Colors.RESET}")
print(f"{Colors.BOLD}{Colors.BLUE}You have 5 chances to guess the number. Good Luck! 🍀{Colors.RESET}")

while guess_count < chances:
    guess = int(input(f"{Colors.MAGENTA}Enter your guess:{Colors.RESET} "))
    print(f"{Colors.UNDERLINE}{Colors.CYAN}You have {chances - guess_count - 1} chances left.{Colors.RESET}")
    guess_count += 1
    if guess == number_to_guess:
        print(f"{Colors.GREEN}Congratulations! You guessed the number {number_to_guess} in {guess_count} tries. 🎉{Colors.RESET}")
        break
    elif guess != number_to_guess and guess_count == chances:
        print(f"{Colors.RED}Sorry! You didn't guess the number {number_to_guess} in {chances} tries. 😔{Colors.RESET}")
        break
    elif guess > number_to_guess:
        print(f"{Colors.YELLOW}Your guess is too high, Try again 😕{Colors.RESET}")
    elif guess < number_to_guess:
        print(f"{Colors.YELLOW}Your guess is too low, Try again 😕{Colors.RESET}")

        