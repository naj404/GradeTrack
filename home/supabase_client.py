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


def get_all_reports():
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
    }
    response = http.get(f"{SUPABASE_URL}/rest/v1/report", headers=headers)
    return response.json()


def update_grade(student_id, subject_column, new_grade):
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'application/json',
    }

    update_payload = {subject_column.lower(): new_grade}

    response = http.patch(
        f"{SUPABASE_URL}/rest/v1/grade?student_id=eq.{student_id}",
        headers=headers,
        json=update_payload
    )

    return response.status_code == 200 or response.status_code == 204


def delete_report_by_id(report_id):
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
    }

    url = f"{SUPABASE_URL}/rest/v1/report?id=eq.{report_id}"
    response = http.delete(url, headers=headers)
    return response.status_code == 200 or response.status_code == 204


def insert_history(student_id, history_text):
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }

    data = {
        "student_id": student_id,
        "history": history_text
    }

    response = http.post(f"{SUPABASE_URL}/rest/v1/history", headers=headers, json=data)
    return response.status_code == 201


def get_all_history():
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
    }

    response = http.get(f"{SUPABASE_URL}/rest/v1/history?order=created_at.desc", headers=headers)
    return response.json()
