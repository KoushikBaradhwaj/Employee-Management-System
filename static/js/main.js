/**
 * Employee Management System
 * Main JavaScript file for general functionality
 */

// DOM Content Loaded Event Listener
document.addEventListener('DOMContentLoaded', function() {
  
  // Initialize Bootstrap tooltips
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function(tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Initialize Bootstrap popovers
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  popoverTriggerList.map(function(popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
  });

  // Auto-close alerts after 5 seconds
  const alerts = document.querySelectorAll('.alert-dismissible');
  alerts.forEach(function(alert) {
    setTimeout(function() {
      const closeButton = alert.querySelector('.btn-close');
      if (closeButton) {
        closeButton.click();
      }
    }, 5000);
  });

  // Add required indicator to form labels
  const requiredInputs = document.querySelectorAll('input[required], select[required], textarea[required]');
  requiredInputs.forEach(function(input) {
    const label = document.querySelector(`label[for="${input.id}"]`);
    if (label && !label.classList.contains('required')) {
      label.classList.add('required');
    }
  });

  // Toggle sidebar in mobile view
  const sidebarToggleBtn = document.querySelector('#sidebarToggle');
  if (sidebarToggleBtn) {
    sidebarToggleBtn.addEventListener('click', function() {
      document.querySelector('.sidebar').classList.toggle('show');
    });
  }

  // Form validation using HTML5 validation API
  const forms = document.querySelectorAll('.needs-validation');
  Array.from(forms).forEach(function(form) {
    form.addEventListener('submit', function(event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });

  // Dynamic field validation
  const emailFields = document.querySelectorAll('input[type="email"]');
  emailFields.forEach(function(field) {
    field.addEventListener('blur', function() {
      validateEmail(field);
    });
  });

  const phoneFields = document.querySelectorAll('input[type="tel"]');
  phoneFields.forEach(function(field) {
    field.addEventListener('blur', function() {
      validatePhone(field);
    });
  });

  // Initialize datetime fields with browser-native controls
  const dateFields = document.querySelectorAll('input[type="date"]');
  dateFields.forEach(function(field) {
    if (!field.value) {
      // Set default to today if no value
      // Commented out to avoid automatically setting dates
      // const today = new Date().toISOString().split('T')[0];
      // field.value = today;
    }
  });

});

/**
 * Validate email format
 * @param {HTMLElement} field - The email input field
 */
function validateEmail(field) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(field.value) && field.value !== '') {
    field.setCustomValidity('Please enter a valid email address');
    field.reportValidity();
  } else {
    field.setCustomValidity('');
  }
}

/**
 * Validate phone number format
 * @param {HTMLElement} field - The phone input field
 */
function validatePhone(field) {
  const phoneRegex = /^\d{10}$/; // Simple 10-digit validation
  if (!phoneRegex.test(field.value) && field.value !== '') {
    field.setCustomValidity('Please enter a 10-digit phone number');
    field.reportValidity();
  } else {
    field.setCustomValidity('');
  }
}

/**
 * Format a date for display
 * @param {string} dateString - The date string to format
 * @returns {string} Formatted date string
 */
function formatDate(dateString) {
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
}

/**
 * Format currency for display
 * @param {number} amount - The amount to format
 * @returns {string} Formatted currency string
 */
function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(amount);
}

/**
 * Calculate date difference in days
 * @param {string} startDate - Start date string
 * @param {string} endDate - End date string
 * @returns {number} Number of days
 */
function calculateDateDiff(startDate, endDate) {
  const start = new Date(startDate);
  const end = new Date(endDate);
  const diffTime = Math.abs(end - start);
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
}
