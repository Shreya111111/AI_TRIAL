
import colorama
from colorama import Fore, Style
from textblob import TextBlob
# Initialize colorama for colored output
colorama.init()
# Emojis for the start of the program print(f"{Fore.CYAN)
Welcome to Sentiment Spy! {Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip() if not user_name:
user_name = "Mystery Agent" # Fallback if user doesn't provide a name
# Store conversation as a list of tuples: (text, polarity, sentiment_type) conversation_history = []
print(f"\n{Fore. CYAN}Hello, Agent {user_name}!")
print (f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment. print("Type {Fore. YELLOW}'reset'{Fore.CYAN}, {Fore. YELLOW}'history' {Fore.CYAN},
f"or {Fore. YELLOW}'exit' {Fore.CYAN} to quit. {Style.RESET_ALL}\n")
while True:
user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
if not user_input:
print("{Fore.RED}Please enter some text or a valid command. {Style.RESET_ALL}")
continue
# Check for commands
if user_input.Lower() = "exit":
print("\n{Fore.BLUE) Exiting Sentiment Spy. Farewell, Agent {user_name}! {Style. RESET_ALL}")
break
elif user_input.lower() = "reset":
conversation_history.clear()
print(f" {Fore.CYAN) ALL conversation history cleared! {Style.RESET_ALL}") continue
elif user_input.lower() = "history":
if not conversation_history:
else:
print(f"{Fore. YELLOW} No conversation history yet. {Style.RESET_ALL}")
print("{Fore.CYAN) Conversation History: {Style. RESET_ALL}")
for idx, (text, polarity, sentiment_type) in enumerate (conversation_history, start=1):
continue
# Choose color & emoji based on sentiment
if sentiment_type = "Positive":
color Fore.GREEN
emoji = ""
elif sentiment_type = "Negative":
else:
color = Fore.RED
emoji =
color Fore. YELLOW
emoji =
print("{idx}. {color}{emoji} {text}
# Analyze sentiment
f" (Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
polarity = TextBlob (user_input).sentiment.polarity
if polarity> 8.25:
sentiment_type = "Positive"
color Fore.GREEN
emoji =
elif polarity< -0.25:
sentiment type = "Negative"
