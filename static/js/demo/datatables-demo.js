// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});

$('#datepicker').datepicker({
  uiLibrary: 'bootstrap4',
  locale: 'es-es',
});
