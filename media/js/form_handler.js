var formset_suffix = '_set'

$(function() {
    $('input[type="submit"]').click(function(event) {
        var button_name = $(this).attr('name')
        var prefix_index = button_name.indexOf(formset_suffix)
        if (prefix_index >= 0) {
            var prefix = '#' + button_name.substring(0, prefix_index + formset_suffix.length)
            $(this).parents('form').get(0).setAttribute('action', prefix)
        }
    })
})
