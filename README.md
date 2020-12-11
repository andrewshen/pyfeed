# pyfeed

A simple command line script that helps you keep track of site updates.

## Dependencies

**First-party modules**

- `os`
- `argparse`

**Third-party modules**

- `requests`
- `beautifulsoup4`
- `validators`
- `python-slugify`

## Usage

First, make sure you've installed all the third-party modules with `pip install -r requirements.txt`.

Add a site `example.com` to your watchlist with `python3 pyfeed.py -a example.com`. Run `python3 pyfeed.py` to check for site updates since you last ran the script. If a site on your watchlist has been updated, it will appear in the output.
