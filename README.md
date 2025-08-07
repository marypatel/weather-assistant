# weather-assistant
A Python CLI tool that fetches current weather by city and provides outfit and activity suggestions.

## Installation
```bash
git clone https://github.com/marypatel/weather-assistant.git
cd weather-assistant
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install .

## Usage
weather-assistant --city "Mississauga,ON"
# → The temperature in Mississauga is currently 20°C.
#   You should dress in light layers and consider a thin jacket.
#   Recommended activities: go for a hike, bike ride, or picnic.

## Input Format

- **Required**: City,ST (for U.S. state) or City,PR (for Canadian province)  
- Only cities in the **United States** and **Canada** are supported in v0.1.

## Environment Variables

### Windows PowerShell

    $env:OWM_API_KEY = "YOUR_API_KEY"

### macOS/Linux (Bash)

    export OWM_API_KEY="YOUR_API_KEY"

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
