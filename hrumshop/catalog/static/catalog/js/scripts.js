$(document).ready(function(){
	let cart_id = $('#cart_id').val();
	let cart_id_array = [];
	let cart_price_str_array = ($('#cart_price').val()).replace(/,/g, ".").split(' ');
	let cart_price_array = [];
	cart_price_str_array.forEach(function(elem) {
		cart_price_array.push(Number(elem))
	});

	if (cart_id.length == 0) {
		$('.total_quantity').text(cart_id_array.length)
	}
	else {
		cart_id_array = cart_id.split(' ');
        $('.total_quantity').text(cart_id_array.length)
    }

    if (cart_id.length == 0) {
    	$('.bt_order').css('display', 'none');
    }


function all_total_price(price_array, id_array, id){
	let all_total_price = 0;
	for (i = 0; i < price_array.length; i++){
		all_total_price += price_array[i]
	}
	$('.total_price').text((all_total_price.toFixed(1) + ' ₽').replace(/\./g, ","))
};

function cart_change(form_id){
	let form = $('#form_cart_product_'+ form_id)
	let quantity = $(form).find('#quantity').val();
	let submit_btn = $(form).find('#submit_btn');
	let id =  submit_btn.data("id");
	let price = submit_btn.data("price").replace(/,/g, ".");
	cart_price_array[cart_id_array.indexOf(String(id))] = Number(quantity*price);
	all_total_price(cart_price_array, cart_id_array, id);
	let data = {};
	data.id = id;
	data.quantity = quantity;
	let csrf_token = $('.form_cart_product [name="csrfmiddlewaretoken"]').val();
	data["csrfmiddlewaretoken"] = csrf_token;

	$.ajax ({
		url: 'add/',
		type: 'POST',
		data: data,
		cache: true,
		});
};

$(document).ready(function(){
// Убавляем кол-во по клику
$('.quantity_inner .bt_minus').click(function() {
    let $input = $(this).parent().find('.input_quantity');
    let count = parseInt($input.val()) - 1;
    count = count < 1 ? 1 : count;
    $input.val(count);
    let id = $(this).parent().find('.bt_del').data('id');
    if (typeof(id) == "number") {
    	cart_change(id)
    } 
});

// Прибавляем кол-во по клику
$('.quantity_inner .bt_plus').click(function() {
    let $input = $(this).parent().find('.input_quantity');
    let count = parseInt($input.val()) + 1;
    count = count > parseInt($input.data('max-count')) ? parseInt($input.data('max-count')) : count;
    $input.val(parseInt(count));
    let id = $(this).parent().find('.bt_del').data('id');
    if (typeof(id) == "number") {
    	cart_change(id)
    } 


}); 
// Убираем все лишнее и невозможное при изменении поля
$('.quantity_inner .input_quantity').bind("change keyup input click", function() {
    if (this.value.match(/[^0-9]/g)) {
        this.value = this.value.replace(/[^0-9]/g, '');
    }
    if (this.value == "") {
        this.value = 1;
    }
    if (this.value > parseInt($(this).data('max-count'))) {
        this.value = parseInt($(this).data('max-count'));
    }
	});
});

	
$('.form_buy_product').on('submit', function(e){
		let form_id = $(this).attr('id');
		let form = $('#'+form_id);
	
		e.preventDefault();
		let quantity = $(this).find('#quantity').val();
		let submit_btn = $(this).find('#submit_btn');
		let id =  submit_btn.data("id");
		let price = submit_btn.data("price").replace(/,/g, ".");

        if (cart_id_array.includes(String(id))) {
        	cart_price_array[cart_id_array.indexOf(String(id))] = Number(quantity*price)
        	all_total_price(cart_price_array, cart_id_array, id)}
        else {
            cart_id_array.push(String(id))
            cart_price_array[cart_id_array.indexOf(String(id))] = Number(quantity*price)
        	$('.total_quantity').text(cart_id_array.length);
        	all_total_price(cart_price_array, cart_id_array, id)}

		let data = {};
		data.id = id;
		data.quantity = quantity;
		let csrf_token = $('.form_buy_product [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		let url = form.attr('action');
		$.ajax ({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			});
		});

$('.form_cart_product').on('submit', function(e){
		let form_id = $(this).attr('id');
		let form = $('#'+form_id);

		e.preventDefault();
		let quantity = $(this).find('#quantity').val();
		let submit_btn = $(this).find('#submit_btn');
		let id =  submit_btn.data("id");
		let price = submit_btn.data("price").replace(/,/g, ".");

		let index_id = cart_id_array.indexOf(String(id));
		cart_id_array.splice(index_id, 1);
		cart_price_array.splice(index_id, 1);

		$('.total_quantity').text(cart_id_array.length);
		all_total_price(cart_price_array, cart_id_array, id);

		let data = {};
		data.id = id;
		let csrf_token = $('.form_cart_product [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		let url = form.attr('action');

		let parent_form_id = $(this).parent().parent().attr('id')
		$('#'+parent_form_id).remove();
		$.ajax ({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			});
		});
});
