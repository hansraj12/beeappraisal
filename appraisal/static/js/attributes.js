function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
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
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$(document).ready(function(){
	
	$(".employee").change(function(){
		var selectedValue=$(this).val();
		$(".form-submit").show();
		var uname=window.location.href 
		uname=uname.split('/')[4]
		console.log(selectedValue);
		$.ajax({
			url : "../app_role_select/"+uname,
  			type : "POST",
  			data : {"id" : selectedValue},
	  		dataType : "json",
	  		success : function(response){
	  			appendData(response);
	  			
	  		}
	});
	
});
	$(".form-submit").click(function(){
		var invalid = false;
		$.each($($("form.attributes").find("select.rating")),function(){
			console.log($(this).val());
			if(!$(this).val()){
				invalid = true;
				return false;
			}
		});
		if(!invalid){
			$(".attributes").submit();
		}else{
			alert("Please Select all the ratings");
		}
		
		
	});
	
});

function appendData(data){
	$(".tasks").empty();
	var append = ' <tr class="" id="task-table-header" style="height:30px;">\
		<th class="col-sm-7 text-center"  style="border: 1px solid #999"> Atrribute</th>\
		<th class="col-sm-3 text-center"  style="border: 1px solid #999">Weightage</th>\
		<th class="col-sm-2 text-center"  style="border: 1px solid #999">Rating</th></tr>';
	for(var key in data){

		append +='<tr  class="items" id="'+data[key]["id"]+'" style="height:30px;background-color: #FFF6CC;">\
		<td class="col-sm-10 text-center title " style="border: 1px solid #999;"> <textarea readonly  style="width:100%;border:none;resize:none;background-color: #FFF6CC;" name="attribute" value="'+data[key]["attribute"]+'">'+data[key]["attribute"]+'</textarea></td>\
		<td class="col-sm-1 text-center title " style="border: 1px solid #999;"> <textarea readonly  style="width:100%;border:none;resize:none;background-color: #FFF6CC;" name="weightage" value="'+data[key]["weightage"]+'">'+data[key]["weightage"]+'</textarea></td>\
				        <td class="col-sm-1 text-center rating" style="border: 1px solid #999;">\
				        	<select class="rating validate[required]" name="ratings">\
				  				<option selected disabled class="col-sm-3" value="">Select Rating</option>\
					  			<option  value="1" >1</option>\
					  			<option  value="3" >3</option>\
					  			<option  value="4" >4</option>\
					  			<option  value="5" >5</option>\
					  			<option  value="7" >7</option>\
							</select>\
						</td></tr>';
	}
	$(".tasks").append(append);
		
}
