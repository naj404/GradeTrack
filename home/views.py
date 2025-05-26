from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .supabase_client import get_data
from .supabase_client import get_data, insert_data, get_grade_by_student
from .supabase_client import insert_report
import json
from .supabase_client import get_grade_by_student, get_reported_subjects

def index(request):
    return render(request, 'home/index.html')

def home_view(request):
    return render(request, 'home/home.html')

def custom_admin_view(request):
    if not request.session.get("admin_logged_in"):
        return redirect("index")
    return render(request, 'home/admin.html')



from django.http import JsonResponse
from .supabase_client import get_data, insert_data


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        student_number = data.get("student_number")

        students = get_data()  # fetch all records
        for student in students:
            if student["student_id"] == student_number:
                request.session["student_id"] = student["student_id"]
                request.session["student_name"] = student["student_name"]
                return JsonResponse({"success": True})

        return JsonResponse({"success": False, "message": "Student number not found."})
    
@csrf_exempt
def admin_login_view(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        password = data.get('password', '')

        if password.strip() == "Super Bass":
            request.session["admin_logged_in"] = True
            return JsonResponse({"success": True})
        return JsonResponse({"success": False})

    
    


def home_view(request):
    if "student_id" not in request.session:
        return redirect("index")

    student_id = request.session["student_id"]
    student_name = request.session["student_name"]

    grade_data = get_grade_by_student(student_id)
    grade = grade_data[0] if grade_data else {"se2": "N/A", "cisco": "N/A", "gvelec": "N/A"}

    # New: get reported subjects list
    reported_subjects = get_reported_subjects(student_id)

    return render(request, "home/home.html", {
        "student_name": student_name,
        "grade_se2": grade.get("se2", "N/A"),
        "grade_cisco": grade.get("cisco", "N/A"),
        "grade_gvelec": grade.get("gvelec", "N/A"),
        "reported_subjects": reported_subjects  # ← NEW
    })




@csrf_exempt
def submit_report_view(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        report_text = data.get("report", "").strip()
        subject_name = data.get("subject_name", "").strip()

        student_id = request.session.get("student_id")
        student_name = request.session.get("student_name")

        if not report_text or not student_id or not student_name or not subject_name:
            return JsonResponse({"success": False, "message": "Missing data"})

        insert_report(student_id, student_name, report_text, subject_name)
        return JsonResponse({"success": True})

    








