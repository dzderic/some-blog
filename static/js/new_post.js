$(function() {
  $(".nav-tabs a[href='#tab-preview']").on('show', function() {
    $.post("/p/md", $("#content").val(), function(data) {
      $("#content-preview").html(data.result);
    }, "json");
  });
});
