// script for the filter

$("basic.temp.html").ready(function () {
    $('#filter').on('click', function() {
    $.ajax({
        type: "GET",
        url: "quotes_filter",
        data: {
            selected : $("#selection").val(),
            book : $('#book').val(),
            csrfmiddlewaretoken : "{{ csrf_token }}"
        },
        success: function (response) {
            console.log(response);       
        document.getElementById('quotes').innerHTML=response;
        },
        error: function (response){
            console.error(response);
        }
    });
	});
});