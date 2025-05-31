/**
 * Initialize DataTables on a table element
 * @param {string} tableId - The ID of the table element
 */
function initDataTable(tableId) {
  const table = $(`#${tableId}`).DataTable({
    responsive: true,
    dom: '<"row"<"col-sm-12 col-md-6"l><"col-sm-12 col-md-6"f>>' +
         '<"row"<"col-sm-12"tr>>' +
         '<"row"<"col-sm-12 col-md-5"i><"col-sm-12 col-md-7"p>>',
    language: {
      search: "_INPUT_",
      searchPlaceholder: "Search...",
      lengthMenu: "Show _MENU_ entries",
      info: "Showing _START_ to _END_ of _TOTAL_ entries",
      infoEmpty: "Showing 0 to 0 of 0 entries",
      infoFiltered: "(filtered from _MAX_ total entries)",
      paginate: {
        first: "First",
        last: "Last",
        next: "Next",
        previous: "Previous"
      }
    },
    pageLength: 10,
    lengthMenu: [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]],
    order: [[0, "asc"]]
  });

  return table;
}

/**
 * Handle confirmation dialogs for delete actions
 * @param {string} selector - The CSS selector for delete buttons
 */
function initDeleteConfirmation(selector) {
  document.querySelectorAll(selector).forEach(button => {
    button.addEventListener('click', function(e) {
      if (!confirm('Are you sure you want to delete this item? This action cannot be undone.')) {
        e.preventDefault();
      }
    });
  });
}

/**
 * Initialize date pickers for date input fields
 */
function initDatePickers() {
  // Use browser's native date picker for simplicity
  // This function is a placeholder for potential custom date picker implementation
}

/**
 * Initialize the page when DOM content is loaded
 */
document.addEventListener('DOMContentLoaded', function() {
  // Initialize all datatables
  const tables = document.querySelectorAll('.datatable');
  tables.forEach(table => {
    initDataTable(table.id);
  });

  // Initialize delete confirmations
  initDeleteConfirmation('.btn-delete');

  // Initialize date pickers
  initDatePickers();
});
