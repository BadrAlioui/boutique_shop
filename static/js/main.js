// Initialize tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));

document.addEventListener("DOMContentLoaded", function () {
  const closeButtons = document.querySelectorAll(".alert .btn-close");
  
  closeButtons.forEach(button => {
    button.addEventListener("click", function () {
      // Refresh the page after a short delay to allow the alert to disappear
      setTimeout(() => {
        location.reload();
      }, 500);
    });
  });
});