# Hogger
- Simple Tool Written In Python3 Works On Scraping User's Github Repositories And Pass Them Into truffleHog To Scan Them Against Possible Data Leaks.
- This Tool Has Been Build To Automate [truffleHog](https://github.com/dxa4481/truffleHog) Scans.

## Installation
```
git clone https://github.com/DEMON1A/Hogger
cd Hogger/
pip install trufflehog
python3 main.py [ARGS]
```

## How To Use?

### Basic
- You Can Start The Automated Scan Without Probems With Something Like The Example Below. The Output Folder Will Be `output` And The Time Delay Between Every Scan Will Be `5` For Default

```
python3 main.py --username DEMON1A
```

### Output
- You Can Select The Output Folder Name. That Will Be Created On Any Path You Run The Tool From. Just Use `-o` Option Like The Example Below

```
python3 main.py --username DEMON1A -o output-folder
```

### Delay
- To Avoid High Usage. And Keep Your Eyes On The Respositories That Got Scanned You Can Add a Time Delay Between Every Scan Using `-d` Option. See The Example Below

```
python3 main.py --username DEMON1A -d 12
```

## How It Works?
- Hogger Is Using Github Developers API To Scrap The Repos On The User's Accounts. Tha Max Results For The API Per Page Is 100 Repos. So Hogger Creates a While Loop On The `page` Parameter To Get All Of The Respos. When The Page Doesn't Contains Respos Any More. Github API Returns Empty List `[]`. That Breaks The Loop And truffleHog Job Starts To Work.

## Messages
- `You Didn't Select a Username` - You Should Add The Username Using `-u` Or `--username` Options
- `Can't Request Github Developer API` - Maybe The Timeout Of The Response Exceeds Or Gitub API Isn't Working.
- `Leaks Search is Done On {URL}` - Leaks Has Been Found On This Repo. Go And Check The Output Folder From Another Tap.
- `There's No Leaks Has Been Found On {URL}` - No Possible Leaks Has Been Found On This Repo.
