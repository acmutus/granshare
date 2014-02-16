$(document).ready(function() {
    $("#accordion").accordion({ header: "h3", collapsible: true, active: false });
  });

var getUserInfo = function() {
	//$.getJSON("/getUser", function(data){});

	var data = {
		"name": "Alican",
		"phone": "+12152758878",
		"groups": ["roommates", "classmates"]
	};

	data.groups.forEach(function(group){
		alert("added: "+ group);
		$("#groups").append("<a href ='index.html'><li>"+group+"</li></a>");
	});
};

window.onload = getUserInfo();

var addExpense = function() {
	var name = $("#name").val();
	var price = $("#price").val();
	var description = $("#description").val();
	

	var object = {
		"name": name,
		"price": price,
		"desc": description,
	};

	$.post("/addExpense", object);


}
