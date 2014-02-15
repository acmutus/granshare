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