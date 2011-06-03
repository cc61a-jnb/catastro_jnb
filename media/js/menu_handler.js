$(function() {
    $('.menu_choice_field').change(function() {
        combobox_change_handler($(this))
    })
    $('#selector_form').submit(function() {
        combobox = $('.last_choice_field')
        entity_id = combobox.val()
        model_name = combobox.attr('id')
        url = "/" + model_name + "/" + entity_id
        $(this).attr("action", url)
    })
    
    combobox_change_handler($('.menu_choice_field').first())
})

function combobox_change_handler(combobox) {
    model_name = combobox.attr('id')
    model_id = combobox.val()
    
    url = "/data/" + model_name + "/" + model_id + "/get_related/"
    
    $.getJSON(url, function(data) {
        next_combobox = combobox.siblings('select').first()
        next_combobox.empty();
        $.each(data, function() {
            next_combobox.append(new Option(this.name, this.id));
        });

    }) 
}


