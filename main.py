import requests
from datetime import datetime, timedelta
from colorama import Fore, Style

# Set the base URL for GitHub REST API
base_url = "https://api.github.com"

# Calculate the date one week ago from today
one_week_ago = (datetime.now() - timedelta(weeks=1)).isoformat()

# Construct the endpoint URL for retrieving most starred repos
endpoint = f"{base_url}/search/repositories?q=created:>{one_week_ago}&sort=stars&order=desc"

# Send GET request to GitHub API
response = requests.get(endpoint)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the top 10 most starred repositories from the response
    most_starred_repos = data['items'][:10]

    # Define dictionary for mapping language to icons
    icons = {
        "Python": "🐍",
        "JavaScript": "🌐",
        "Java": "☕",
        "Ruby": "💎",
        "Go": "🔍",
        "C++": "⚙️",
        "C#": "🔢",
        "TypeScript": "📜",
        "Shell": "💻",
        "CSS": "🎨",
        "HTML": "📝",
        "PHP": "🔌",
        "Swift": "🚀",
        "Kotlin": "📱",
        "Rust": "🔒",
        "Vue": "🖼️",
        "Scala": "🧠",
        "Perl": "🐪",
        "Objective-C": "📱",
        "Jupyter Notebook": "🔬",
        "TeX": "📄",
        "PowerShell": "💻",
        "Lua": "🌙",
        "Haskell": "🔺",
        "MATLAB": "🔬",
        "R": "📊",
        "Dart": "🎯",
        "Vue.js": "🖼️",
        "CoffeeScript": "☕",
        "Elixir": "🔧",
        "Clojure": "🚿"
    }

    # Display the details of the top 10 most starred repositories with color, icons, and emojis
    print(f"{Fore.YELLOW}Top 10 Most Starred Repositories in the Last Week:{Style.RESET_ALL}\n")
    for i, repo in enumerate(most_starred_repos, start=1):
        print(f"{Fore.CYAN}Repository {i}:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Repository Name:{Style.RESET_ALL} {repo['name']}")
        print(f"{Fore.GREEN}Repository Owner:{Style.RESET_ALL} {repo['owner']['login']}")
        print(f"{Fore.GREEN}Number of Stars:{Style.RESET_ALL} {repo['stargazers_count']}")
        print(f"{Fore.BLUE}Repository URL:{Style.RESET_ALL} {repo['html_url']}")
        print(f"{Fore.MAGENTA}Language:{Style.RESET_ALL} {icons.get(repo['language'], 'Unknown')} {repo['language']}\n")
else:
    print("Failed to fetch most starred repositories. Response code:", response.status_code)