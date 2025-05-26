import requests as http
from decouple import config

SUPABASE_URL = config('SUPABASE_URL')
SUPABASE_KEY = config('SUPABASE_KEY')
SUPABASE_TABLE = config('SUPABASE_TABLE')

def get_data():
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
    }
    response = http.get(f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}', headers=headers)
    return response.json()

def insert_data(data):
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }
    response = http.post(f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}', headers=headers, json=data)
    return response.json()


def get_grade_by_student(student_id):
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
    }
    params = {
        'student_id': f'eq.{student_id}'
    }
    response = http.get(
        f'{SUPABASE_URL}/rest/v1/grade',
        headers=headers,
        params=params
    )
    return response.json()



def insert_report(student_id, name, report_text, subject_name):
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }

    data = {
        "student_id": student_id,
        "name": name,
        "report": report_text,
        "subject_name": subject_name
    }

    response = http.post(f'{SUPABASE_URL}/rest/v1/report', headers=headers, json=data)
    return response.json()


def get_reported_subjects(student_id):
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
    }
    params = {
        'student_id': f'eq.{student_id}'
    }
    response = http.get(
        f'{SUPABASE_URL}/rest/v1/report',
        headers=headers,
        params=params
    )
    reports = response.json()
    return [r["subject_name"] for r in reports]
