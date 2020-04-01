// script for the filter

$("index.html").ready(function () {
    $('#send').on('click', function() {

        // todo dRE UN CONTROLLO per controllare tutti campi piena o no
    if($("#name").val() == "" && $("#email").val() == "" && $("#phone").val() == "" && $("#message").val() ==  ""){
        alert("Complete all the models");
    }
    else{
        $.ajax({
            type: "GET",
            url: "/feedback",
            data: {
                name: $("#name").val(),
                email: $("#email").val(),
                phone: $("#phone").val(),
                msg: $("#message").val(),
                csrfmiddlewaretoken : "{{ csrf_token }}"
            },
            success: function (response) {
                console.log(response);       
                document.getElementById('success').innerHTML=response;
            },
            error: function (response){
                console.error(response);
            }
        });
    }
        });
});