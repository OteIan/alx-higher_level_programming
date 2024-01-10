$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $('#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
