document.getElementById('loginBtn').addEventListener('click', function() {
    document.getElementById('loginModal').style.display = 'block';
});

function closeModal() {
    document.getElementById('loginModal').style.display = 'none';
}

function login() {
    // Implement your login logic here
    alert('Login button clicked');
    closeModal();
}
