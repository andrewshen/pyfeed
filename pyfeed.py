import os  # for storing site data
import argparse  # for parsing arguments
import validators  # for validating urls
from slugify import slugify  # processing urls
from urllib.parse import urlparse  # parsing urls
from bs4 import BeautifulSoup  # parsing html


def build_parser():
    """
    Builds an ArgumentParser with the specified parameters.

    Args:
        None

    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description="Displays sites that have been updated")
    parser.add_argument('-a', metavar="url", help="Add new site to pyfeed")

    if not os.path.exists('.sitedata'):
        os.makedirs('.sitedata')

    return parser


def add_new_site(url):
    """
    Adds a new site to watch for updates

    Args:
        url (str): the website to be added

    Returns:
        None
    """
    if validators.url(url):
        filename = ".sitedata/" + slugify(url) + ".txt"
        if os.path.exists(filename):
            print("Site already exists!")
        else:
            f = open(filename, "w")
            f.write(url)
            print("Site added!")
    else:
        print("Please enter a valid URL")


def load_site_data(filename):
    """
    Fetches site data from file

    Args:
        filename (str): the file to be referenced

    Returns:
        html (str): the text of the website
    """
    pass


def fetch_site_data(filename):
    """
    Fetches new site data from file using beautifulsoup

    Args:
        filename (str): the file to be referenced

    Returns:
        html (str): the text of the website
    """
    pass


def update_site_data(url):
    """
    Updates site data with new html

    Args:
        url (str): the website to be updated

    Returns:
        None
    """
    pass


def compare_site_data(url):
    """
    Compares site data

    Args:
        site (str): the website to be checked for updates

    Returns:
        did_update (boolean): whether the site has been updated or not
    """
    pass


def print_updated_sites():
    """
    Prints all updated sites

    Args:
        None

    Returns:
        None
    """

    directory = os.fsencode(".sitedata")
    updated_sites = {}

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            existing_data = load_site_data(filename)
            new_data = fetch_site_data(filename)
            continue


def main():
    """
    Builds an ArgumentParser object by calling build_parser(),
    adds a new site if specified by the user,
    and then prints the updated sites using print_updated_sites().
    """
    parser = build_parser()
    # Parse command line arguments
    new_site = parser.parse_args().a

    # Load data from url and then print the data
    if new_site:
        add_new_site(new_site)
    else:
        print_updated_sites()


if __name__ == '__main__':
    main()
