function f1(req , title){   
        $.ajax({
            type: "GET",
            url: "photos",
            data: {
                selected : req,
            },
            success: function (response) {
                //console.log(response);      
                document.getElementById('body').innerHTML=response; 
            },
            error: function (response){
                console.error(response);
            }
        });

    document.getElementById('title').innerHTML=title; 
}