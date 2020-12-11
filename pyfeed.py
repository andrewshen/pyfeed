import os  # for storing site data
import argparse  # for parsing arguments
import validators  # for validating urls
from slugify import slugify  # processing urls
from urllib.parse import urlparse  # parsing urls
from bs4 import BeautifulSoup  # parsing html
import requests  # for making HTTP requests


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
    parser.add_argument("-a", metavar="url", help="Add new site to pyfeed")

    if not os.path.exists(".sitedata"):
        os.makedirs(".sitedata")

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


def extract_url(filename):
    """
    Extract URL from file

    Args:
        filename (str): the file to get the URL from

    Returns:
        url (str): the corresponding url
    """
    with open(filename) as f:
        url = f.readline()
    return url


def load_site_data(filename):
    """
    Fetches site data from file

    Args:
        filename (str): the file to be referenced

    Returns:
        html (str): the text of the website
    """
    f = open(filename, "r")
    html = f.readlines()[1:]
    f.close()
    return html


def fetch_site_data(filename):
    """
    Fetches new site data from file using beautifulsoup

    Args:
        filename (str): the file to be referenced

    Returns:
        html (str): the text of the website
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
    }
    req = requests.get(extract_url(filename))
    soup = BeautifulSoup(req.text, "html.parser")
    return soup.prettify()


def update_site_data(filename, new_data):
    """
    Updates site data with new html

    Args:
        filename (str): the file to be updated
        new_data (str): the updated html data

    Returns:
        None
    """
    pass


def compare_site_data(filename):
    """
    Compares site data

    Args:
        filename (str): the file to check against updates

    Returns:
        did_update (boolean): whether the site has been updated or not
    """
    existing_data = load_site_data(filename)
    new_data = fetch_site_data(filename)
    update_site_data(filename, new_data)
    return existing_data != new_data


def print_updated_sites():
    """
    Prints all updated sites

    Args:
        None

    Returns:
        None
    """

    directory = os.fsencode(".sitedata")
    updated_sites = set()

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            path = ".sitedata/" + filename
            if compare_site_data(path):
                updated_sites.add(extract_url(path))

    for site in updated_sites:
        print(site)


def main():
    """
    Builds an ArgumentParser object by calling build_parser(),
    adds a new site if specified by the user,
    and then prints the updated sites using print_updated_sites().
    """
    parser = build_parser()
    # Parse command line arguments
    new_site = parser.parse_args().a

    if new_site:
        add_new_site(new_site)
    else:
        print_updated_sites()


if __name__ == '__main__':
    main()
