# pyfeed

A simple command line script that lets you keep track of site updates

## Dependencies

### First-party modules

- os
- argparse
- requests

### Third-party modules

- beautifulsoup4
- validators
- slugify

## Usage

Add a site `example.com` to your watchlist with `pyfeed.py -a example.com`. Run `pyfeed.py` to check for site updates since the last run. If a site on your watchlist has been updated, it will appear in the output.
