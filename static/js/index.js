// todo fare i controlli per ogni campo
//! dare messaggio di errori se insermenti sbagliati
//* risettare i campi


$("index.html").ready(function () {
    $('#feed').on('click', function() {

        if($("#name").val() == "" || $("#email").val() == "" || $("#phone").val() == "" || $("#message").val() ==  ""){
            alert("Complete all the forms");
        }

        else{
            $.ajax({
                type: "GET",
                url: "feedback",
                data: {
                    name: $("#name").val(),
                    email: $("#email").val(),
                    phone: $("#phone").val(),
                    msg: $("#message").val(),           
                },
                success: function (response) {
                    var name = response.name;
                    $("#name").val(""),
                    $("#email").val(""),
                    $("#phone").val(""),
                    $("#message").val(""),  
                    alert("Thank you " + name );
                    console.log(response.name);   
                },
                error: function (response){
                    console.log(response);  
                }
            });
        }
    });
});