$(function() {
    $('.menu_choice_field').change(function() {
        combobox_change_handler($(this))
    })
    
    combobox_change_handler($('.menu_choice_field').first())
})

function combobox_change_handler(combobox) {
    model_name = combobox.attr('id')
    model_id = combobox.val()
    console.log(model_name)
    console.log(model_id)
}


