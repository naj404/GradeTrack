// Custom Alert Function (replaces browser's alert)
function showCustomAlert(message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'fixed top-5 left-1/2 -translate-x-1/2 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-[1001] transition-all duration-300 ease-out opacity-0 transform -translate-y-full';
    alertDiv.textContent = message;
    document.body.appendChild(alertDiv);

    setTimeout(() => {
        alertDiv.classList.remove('opacity-0', '-translate-y-full');
        alertDiv.classList.add('opacity-100', 'translate-y-0');
    }, 50);

    setTimeout(() => {
        alertDiv.classList.remove('opacity-100', 'translate-y-0');
        alertDiv.classList.add('opacity-0', '-translate-y-full');
        alertDiv.addEventListener('transitionend', () => alertDiv.remove());
    }, 3000);
}

// Grade update logic (real backend request + delete report)
document.querySelectorAll('.grade-update-form button').forEach(button => {
    button.addEventListener('click', async (event) => {
        const card = event.target.closest('.request-card');
        const studentInfo = card.querySelector('h3').textContent.trim();
        const studentName = studentInfo.split('(')[0].trim();
        const studentId = studentInfo.split('(')[1].replace(')', '').trim();

        const subjectTag = card.querySelector('.subject-tag').textContent;
        const subjectName = subjectTag.split(':')[1].trim();

        const reportId = card.getAttribute("data-report-id");  // 🆕 get report ID from HTML

        const newGradeInput = card.querySelector('input[type="number"]');
        const newGrade = parseInt(newGradeInput.value);

        if (isNaN(newGrade) || newGrade < 0 || newGrade > 100) {
            showCustomAlert('Please enter a valid new grade (0-100).');
            return;
        }

        try {
            const response = await fetch("/update-grade/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    student_id: studentId,
                    subject_name: subjectName,
                    new_grade: newGrade,
                    report_id: reportId  // 🆕 include for deletion
                })
            });

            const result = await response.json();
            if (result.success) {
                showCustomAlert(`✅ Grade for ${studentName} updated to ${newGrade}!`);
                card.remove();  // 🧹 remove card from page
                updateNoRequestsMessage(); // refresh "no requests" state
            } else {
                showCustomAlert("❌ Update failed.");
            }
        } catch (err) {
            showCustomAlert("🚫 Network error");
        }
    });
});

// Show/hide "no requests" message
function updateNoRequestsMessage() {
    const requestContainer = document.getElementById('request-cards-container');
    const noRequestsMessage = document.getElementById('no-requests-message');
    if (requestContainer.children.length === 0) {
        noRequestsMessage.style.display = 'block';
    } else {
        noRequestsMessage.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', updateNoRequestsMessage);
