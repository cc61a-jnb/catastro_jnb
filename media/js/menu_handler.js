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
    
    if(model_name && model_id){
        url = "/data/" + model_name + "/" + model_id + "/get_related/"
        
        $.getJSON(url, function(data) {
            next_combobox = combobox.siblings('select').first()
            next_combobox.empty();
            $.each(data, function() {
                // Reference: http://groups.google.com/group/jquery-en/browse_thread/thread/887c03f088ffb302
                next_combobox[0].options[next_combobox[0].length] = new Option(this.name, this.id); 
            })
        })
    }
}


