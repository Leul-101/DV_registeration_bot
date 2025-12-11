document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('image-modal');
    const modalImg = document.getElementById('modal-image');
    const closeModal = document.querySelector('.close-modal');

    // Open modal to view full image
    document.querySelectorAll('.payment-image img').forEach(img => {
        img.addEventListener('click', function() {
            modal.style.display = 'block';
            modalImg.src = this.dataset.fullSrc;
        });
    });

    // Close modal
    if(closeModal) {
        closeModal.onclick = function() {
            modal.style.display = 'none';
        }
    }
    if(modal) {
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        }
    }


    // Handle payment status updates
    document.querySelectorAll('.btn-approve, .btn-reject').forEach(button => {
        button.addEventListener('click', function() {
            const applicationId = this.dataset.id;
            const action = this.classList.contains('btn-approve') ? 'Paid' : 'Rejected';
            
            updatePaymentStatus(applicationId, action);
        });
    });

    function updatePaymentStatus(applicationId, status) {
        fetch('/update_family_payment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                application_id: applicationId,
                status: status
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const card = document.getElementById(`payment-card-${applicationId}`);
                if (card) {
                    card.classList.add('fading-out');
                    // Wait for the animation to finish before removing the element
                    setTimeout(() => {
                        card.remove();
                        // Check if grid is empty
                        const grid = document.getElementById('payments-grid');
                        if (grid && grid.children.length === 0) {
                            grid.innerHTML = `
                                <div class="empty-state">
                                    <h2>All caught up!</h2>
                                    <p>There are no pending payments to review.</p>
                                </div>`;
                        }
                    }, 300);
                }
            } else {
                alert('Failed to update payment status: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating the payment status.');
        });
    }
});
