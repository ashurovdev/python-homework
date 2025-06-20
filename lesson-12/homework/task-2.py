import sqlite3
import requests
from bs4 import BeautifulSoup
import csv

def fetch_jobs():
    main_link = 'https://realpython.github.io/fake-jobs/'
    res = requests.get(main_link)
    main_soup = BeautifulSoup(res.text, 'html.parser')

    job_titles = main_soup.find_all('h2', class_='title is-5')
    job_companies = main_soup.find_all('h3', class_='subtitle is-6 company')
    job_locations = main_soup.find_all('p', class_='location')
    job_desc_links = main_soup.find_all('a', href=True, string='Apply')
    job_learn_links = main_soup.find_all('a', href=True, string='Learn')

    job_descs = []
    for job in job_desc_links:
        link = job['href']
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        desc_p = soup.find('p')
        job_descs.append(desc_p.text.strip() if desc_p else 'No description')

    return zip(job_titles, job_companies, job_locations, job_descs, job_learn_links)


def create_table():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                job_title TEXT NOT NULL,
                job_company TEXT NOT NULL,
                job_location TEXT NOT NULL,
                job_desc TEXT NOT NULL,
                job_link TEXT NOT NULL,
                UNIQUE(job_title, job_company, job_location)
            )
        ''')
        conn.commit()


def insert_or_update_jobs(jobs):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        for title, company, location, desc, link in jobs:
            job_title = title.text.strip()
            job_company = company.text.strip()
            job_location = location.text.strip()
            job_desc = desc
            job_link = link['href']

            cursor.execute('''
                SELECT job_desc, job_link FROM jobs
                WHERE job_title=? AND job_company=? AND job_location=?
            ''', (job_title, job_company, job_location))
            row = cursor.fetchone()

            if row:
                # If job exists, check if it has been updated
                if row[0] != job_desc or row[1] != job_link:
                    cursor.execute('''
                        UPDATE jobs
                        SET job_desc=?, job_link=?
                        WHERE job_title=? AND job_company=? AND job_location=?
                    ''', (job_desc, job_link, job_title, job_company, job_location))
            else:
                # If job doesn't exist, insert it
                cursor.execute('''
                    INSERT INTO jobs (job_title, job_company, job_location, job_desc, job_link)
                    VALUES (?, ?, ?, ?, ?)
                ''', (job_title, job_company, job_location, job_desc, job_link))

        conn.commit()


def filter_jobs(location=None, company=None):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()

        query = 'SELECT * FROM jobs WHERE 1=1'
        params = []

        if location:
            query += ' AND job_location LIKE ?'
            params.append(f'%{location}%')
        if company:
            query += ' AND job_company LIKE ?'
            params.append(f'%{company}%')

        cursor.execute(query, params)
        return cursor.fetchall()


def export_to_csv(filtered_jobs, filename='filtered_jobs.csv'):
    headers = ['Title', 'Company', 'Location', 'Description', 'Link']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(filtered_jobs)
    print(f"✅ Exported to {filename}")



create_table()
jobs = fetch_jobs()
insert_or_update_jobs(jobs)

filtered = filter_jobs(location='Stewartbury, AA')
export_to_csv(filtered, 'filtered_jobs.csv')
