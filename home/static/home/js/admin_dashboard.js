
 


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
        // Dummy JS for submit buttons (for demonstration)
        document.querySelectorAll('.grade-update-form button').forEach(button => {
            button.addEventListener('click', (event) => {
                const card = event.target.closest('.request-card');
                const studentId = card.dataset.requestId;
                const studentName = card.querySelector('h3').textContent.trim().split('(')[0].trim();
                const currentGrade = card.querySelector('.current-grade-display').textContent.trim();
                const newGradeInput = card.querySelector('input[type="number"]');
                const newGrade = newGradeInput.value;

                if (!newGrade || newGrade < 0 || newGrade > 100) {
                    showCustomAlert('Please enter a valid new grade (0-100).');
                    return;
                }

                console.log(`Submitting grade update for ${studentName} (ID: ${studentId}):`);
                console.log(`Current Grade: ${currentGrade}, New Grade: ${newGrade}`);
                showCustomAlert(`Grade for ${studentName} updated to ${newGrade}!`);
                // In a real application, you would send this data to a backend.
            });
        });

        // Function to check if there are requests and show/hide message
        function updateNoRequestsMessage() {
            const requestContainer = document.getElementById('request-cards-container');
            const noRequestsMessage = document.getElementById('no-requests-message');
            if (requestContainer.children.length === 0) {
                noRequestsMessage.style.display = 'block';
            } else {
                noRequestsMessage.style.display = 'none';
            }
        }

        // Initial call to update message on load
        document.addEventListener('DOMContentLoaded', updateNoRequestsMessage);