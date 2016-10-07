function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
     // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}




$(document).ready(function(){
	$('.register' ).click(function() {
		var arr = [];
		e = {};
		var id=$(".appraiser-names").val()
		var username = $("#inputusername").val();
		console.log(username)
		var email = $("#inputEmail").val();
		var password = $("#inputPassword").val();
		e['id']=id;
		e['name']=username;
		e['email']=email;
		e['password']=password;
		arr.push(e);
		console.log(arr);
		

//		$.ajax({url:"../home",type: 'POST', accepts: "application/json; charset=utf-8",
//            beforeSend: function(xhr, settings) {
//        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//            xhr.setRequestHeader("X-CSRFToken", csrftoken);
//        }
//    },
//    
//           data:{'i[]':JSON.stringify(arr)},
//           dataType: "json",
//           success: function(){
//            
//           }
//       });
		
	});
	
});
