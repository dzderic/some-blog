$(function() {
  $(".nav-tabs a[href='#tab-preview']").on('show', function() {
    $("#content-preview").html('<div class="loading-spinner">&nbsp;</div>');
    $.post("/p/md/", $("#content").val(), function(data) {
      $("#content-preview").html(data.result);
    }, "json");
  });
});
