$(document).ready(function () {
  var tabs = $('.tab');

  tabs.on('click focusin', function () {
    $(this).parent().addClass('active').siblings().removeClass('active');
  });
});