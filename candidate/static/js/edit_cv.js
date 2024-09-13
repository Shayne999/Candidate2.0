// Function to get the CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Set up CSRF token for AJAX requests
const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', () => {
    // Function to add a new item to a list
    function addItem(button) {
        const listId = button.getAttribute('data-list-id');
        const list = document.getElementById(listId);
        const newItem = document.createElement('li');
        newItem.innerHTML = `
            <input type="text" name="${listId.slice(0, -5)}" />
            <button type="button" class="remove-item">-</button>
        `;
        list.appendChild(newItem);
    }

    // Function to remove an item from a list
    function removeItem(button) {
        button.parentElement.remove();
    }

    // Event delegation for dynamically added buttons
    document.body.addEventListener('click', (event) => {
        if (event.target.classList.contains('add-item-button')) {
            addItem(event.target);
        } else if (event.target.classList.contains('remove-item')) {
            removeItem(event.target);
        }
    });

    // Add CSRF token to form submission via AJAX
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission
            const formData = new FormData(form);
            fetch(form.action, {
                method: form.method,
                headers: {
                    'X-CSRFToken': csrftoken
                },
                body: formData
            }).then(response => {
                if (response.ok) {
                    window.location.href = response.url; // Redirect on success
                } else {
                    console.error('Form submission failed');
                }
            }).catch(error => console.error('Error:', error));
        });
    });
});







