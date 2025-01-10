
var up = []
var down = []
var stack = []

var cl_class = {
    0: 'ordered_false',
    1: 'ordered_unknow',
    2: 'ordered_true'
}

var send_domino_funcs = {
    'analize_radio': send_domino_data_to_analize,
    'predict_radio': send_domino_data_to_predict
}

var graph_tumbler_text = {
    0: "Важность признаков",
    1: "Эффективность модели"
}

var graphs = {
    0: "#importanses_graph",
    1: "#effectivity_graph"
}

function add_domino() {

    var n = get_stack_max_size_to_predict()
    if (up.length < n) {

        domino = $(this)
        domino_src = domino.attr('src')
        add_domino_data(domino.attr('up'), domino.attr('down'))
        elem_num = up.length - 1

        var start_offset = domino.offset()
        var start_top = start_offset['top']
        var start_left = start_offset['left']
        
        var domin_clone = domino.clone()

        if (get_actual_size_domino_array() == 6) {
            add_domino_picture(domin_clone, start_top, start_left)
            move_domino(domin_clone, elem_num, send_data, true)
        } else {
            scrollbar_pos = get_scrollbar_pos(elem_num)
            $("#play_area").animate({scrollLeft: scrollbar_pos}, 100, function() {
                add_domino_picture(domin_clone, start_top, start_left)
                move_domino(domin_clone, elem_num, send_data, true)
            })
        }
            

    }
}

function add_domino_picture(domino, top, left) {
    domino.appendTo('body')
    domino.offset({'top': top, 'left': left})
}

function move_domino(domino, domino_ind, function_after, push_empty) {

    var empty_id = 'empty_' + domino_ind
    var empty = $('#' + empty_id)

    if (empty.is(':visible')) {
        var finish_offset = empty.offset()
        var finish_top = finish_offset['top']
        var finish_left = finish_offset['left']        
    } else {
        var finish_top = $('#play_area').top() - 50
        var finish_left = get_win_center()
    }

    domino.animate({'top': finish_top, 'left': finish_left}, 200, function() {
        this.remove(); 
        empty.attr('src', domino.attr('src')); 
        function_after();        
    });
    
    if (push_empty) {
        stack.push(empty)
    }
}

function move_domino_simple(domino, domino_ind) {

    var empty_id = 'empty_' + domino_ind
    var empty = $('#' + empty_id)

    var finish_offset = empty.offset()
    var finish_top = finish_offset['top']
    var finish_left = finish_offset['left']

    domino.animate({'top': finish_top, 'left': finish_left}, 100, function() {this.remove(); empty.attr('src', domino.attr('src'))});
    stack.push(empty)

}

function send_domino_data_to_analize() {    

    var header = {
        'url': '/ordered_check',
        'type': 'post',
        'headers': {'Content-Type': "application/json"},
        'data': JSON.stringify({
            up: up,
            down: down
        })
    }

    AjaxQuery.info(header, function(data) {
        order_check_class = cl_class[data['ordered_check']]
        $('#table').addClass(order_check_class)
    })

}

function send_domino_data_to_predict() {

    var header = {
        'url': '/predict',
        'type': 'post',
        'headers': {'Content-Type': "application/json"},
        'data': JSON.stringify({
            up: up,
            down: down
        })
    }

    AjaxQuery.info(header, function(data) {
        
        domino_img = data['img']

        domino_img = jQuery(domino_img)              
        add_domino_data(data['up'], data['down'])
                
        $("#play_area").animate({scrollLeft: get_scroll_area_width()}, 800, function() {
            add_domino_picture(domino_img, -100, 1300)
            domino_img.addClass('domino_pic')  
            move_domino_simple(domino_img, up.length - 1)
        })
    })
}

function add_domino_data(up_data, down_data) {
    up.push(Number(up_data))
    down.push(Number(down_data))
}

function get_stack_max_size() {
    return Number($('#add_max_size_btn').val())
}


function get_stack_max_size_to_predict() {
    max_size = get_stack_max_size()
    diff = Number($('input[name="mode"]:checked').attr('diff'))
    return max_size - diff
}

function send_data() {
    n = get_stack_max_size_to_predict()
    if (up.length == n) {
        var radio = $('input[name="mode"]:checked').attr('id')
        var send_data_func = send_domino_funcs[radio]
        send_data_func()
    }    
}

function clear_table() {

    var empty_src = get_empty_picture_src()
    $.each(stack, function(i, v) {
        v.attr('src', empty_src)
    })

    up.length = 0
    down.length = 0

    $('#table').removeClass('ordered_false')
    $('#table').removeClass('ordered_true')
    $('#table').removeClass('ordered_unknow')

}

function domino_rollback() {

    if (up.length > 0) {

        up.pop()
        down.pop()

        var empty_src = get_empty_picture_src()

        var domino_to_remove = stack.pop()
        domino_to_remove.attr('src', empty_src)

        $('#table').removeClass('ordered_false')
        $('#table').removeClass('ordered_true')
        $('#table').removeClass('ordered_unknow')
    }
    
}

function switch_mode() {

    if ($(this).attr('id') == 'predict_radio') {
        $('#table').removeClass('ordered_false')
        $('#table').removeClass('ordered_true')
        $('#table').removeClass('ordered_unknow')
    }
    
    var n = get_stack_max_size_to_predict()
    if (up.length == n) {
        send_data()
    }
}

function get_win_center() {
    return $(window).width() / 2
}

function get_actual_size_domino_array() {
    return $('.empty').length
}



function key_board_funcks(e) {
    if (e.which === 13) {
        change_max_size()
    }
    if (e.which === 8) {
        clear_size_input()
    }
}

function clear_size_input() {
    if (!$("#expected_size_input").is(":focus")) {
        $('#expected_size_input').val('')
        $('#expected_size_input').focus()
    }    
}


function change_max_size() {

    var expected_size_input = $('#expected_size_input')
    val = Number(expected_size_input.val())
    expected_size_input.removeClass('has_error')

    if (val < 6 | val > 18) {
        expected_size_input.addClass('has_error')
        expected_size_input.blur()
        return
    }
    

    $('#add_max_size_btn').val(val)
    var actual_length = get_actual_size_domino_array()

    if (actual_length < val) {
        $('#table').removeClass('ordered_false')
        $('#table').removeClass('ordered_true')
        $('#table').removeClass('ordered_unknow')
        add_empty_picture()
    }

    if (actual_length > val) {
        remove_empty_pic()
        up.length = Math.min(val, up.length)
        down.length = Math.min(val, down.length)
        stack.length = Math.min(val, stack.length)
    
    }

}

function add_empty_picture() {

    if (get_actual_size_domino_array() < get_stack_max_size()) {

        var new_empty = $('<img class="empty">')
        new_empty.attr('id', 'empty_' + get_actual_size_domino_array())
        $('#play_area').append(new_empty)
        $("#play_area").animate({scrollLeft: get_scroll_area_width()}, 1000, add_empty_picture_src)

    } else {
        $('#table').removeClass('ordered_false')
        $('#table').removeClass('ordered_true')
        $('#table').removeClass('ordered_unknow')
        send_data()
    }
   
}

function get_scroll_area_width() {
    return $('#play_area').prop('scrollWidth')
}

function add_empty_picture_src() {

    domino_img = $('<img class="empty">')
    domino_img.attr('src', get_empty_picture_src())

    add_domino_picture(domino_img, -100, get_win_center())
    move_domino(domino_img, get_actual_size_domino_array() - 2, add_empty_picture, false)

}

function remove_empty_pic() {

    if (get_actual_size_domino_array() > get_stack_max_size()) {

        domino = $('.empty').last()
        domino.removeAttr('src')

        var start_offset = domino.offset()
        var start_top = start_offset['top']
        var start_left = start_offset['left']

        var domin_clone = domino.clone()
        add_domino_picture(domin_clone, start_top, start_left)

        domin_clone.animate({'top': -300, 'left': get_win_center()}, 200, function() {
            domin_clone.remove()
            domino.remove();
            remove_empty_pic()
        })
    } else {
        $('#table').removeClass('ordered_false')
        $('#table').removeClass('ordered_true')
        $('#table').removeClass('ordered_unknow')
        send_data()
    }
}

function get_empty_picture_src() {
    return $('#empty_picture_src').val()
}

function get_scrollbar_pos(elem_num) {

    if (elem_num < 6) {
        return 0
    }

    scroll_width = get_scroll_area_width()
    stack_max_size = get_stack_max_size()

    if (elem_num < 12 & stack_max_size > 12) {

        if (stack_max_size < 16) {
            return scroll_width / 2.3
        }

        return scroll_width / 3
        
    }

    return scroll_width
}

function switch_graph() {

    var actual_state = Number($(this).attr('state'))
    var new_state = 1 - actual_state
    var actual_graph_id = graphs[actual_state]
    var new_graph_id = graphs[new_state]

    $(actual_graph_id).addClass('empty_src')
    $(new_graph_id).removeClass('empty_src')

    $(this).text(graph_tumbler_text[actual_state])
    $(this).attr('state', new_state)
}