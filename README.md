# Revue

Downloads your revue issues for offline storage. Just in case..

## Install

Install using your choice of package manager, I'm using pipenv. 

    pipenv install

## Usage

Set the REVUE_API_KEY environment variable to your revue API key. Find this at the bottom of your Account Settings > Integrations page. If using pipenv, just add it to a .env file.

Run the script:

    pipenv run python get_revue_issues.py

Issues will be saved as html to your local machine under /issues