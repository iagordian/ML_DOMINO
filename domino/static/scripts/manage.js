
var up = []
var down = []
var stack = []
var empty_src

var cl_class = {
    0: 'ordered_false',
    1: 'ordered_unknow',
    2: 'ordered_true'
}

var send_domino_funcs = {
    'analize_radio': send_domino_data_to_analize,
    'predict_radio': send_domino_data_to_predict
}

function add_domino() {

    var n = get_stack_max_size()
    if (up.length < n) {

        domino = $(this)
        domino_src = domino.attr('src')
        add_domino_data(domino.attr('up'), domino.attr('down'))

        var empty_id = 'empty_' + up.length
        var empty = $('#' + empty_id)
        empty_src = empty.attr('src')

        var start_offset = domino.offset()
        var start_top = start_offset['top']
        var start_left = start_offset['left']
        
        var domin_clone = domino.clone()
        add_domino_picture(domin_clone, start_top, start_left)

        move_domino(domin_clone, send_data)           

    }
}

function add_domino_picture(domino, top, left) {
    domino.appendTo('body')
    domino.offset({'top': top, 'left': left})
}

function move_domino(domino, function_after) {

    var empty_id = 'empty_' + (up.length - 1)
    var empty = $('#' + empty_id)
    empty_src = empty.attr('src')

    var finish_offset = empty.offset()
    var finish_top = finish_offset['top']
    var finish_left = finish_offset['left']

    domino.animate({'top': finish_top, 'left': finish_left}, 200, function() {this.remove(); empty.attr('src', domino.attr('src')); function_after()});
    stack.push(empty)

}

function move_domino_simple(domino) {

    var empty_id = 'empty_' + (up.length - 1)
    var empty = $('#' + empty_id)
    empty_src = empty.attr('src')

    var finish_offset = empty.offset()
    var finish_top = finish_offset['top']
    var finish_left = finish_offset['left']

    domino.animate({'top': finish_top, 'left': finish_left}, 200, function() {this.remove(); empty.attr('src', domino.attr('src'))});
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
        add_domino_picture(domino_img, -100, 1300)
        domino_img.addClass('domino_pic')        
        add_domino_data(data['up'], data['down'])
        move_domino_simple(domino_img, get_stack_max_size)         
    })
}

function add_domino_data(up_data, down_data) {
    up.push(Number(up_data))
    down.push(Number(down_data))
}


function get_stack_max_size() {
    N = Number($('input[name="mode"]:checked').attr('n'))
    return N
}

function send_data() {
    n = get_stack_max_size()
    if (up.length == n) {
        var radio = $('input[name="mode"]:checked').attr('id')
        var send_data_func = send_domino_funcs[radio]
        send_data_func()
    }    
}

function clear_table() {

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

        var domino_to_remove = stack.pop()
        domino_to_remove.attr('src', empty_src)

        $('#table').removeClass('ordered_false')
        $('#table').removeClass('ordered_true')
        $('#table').removeClass('ordered_unknow')
    }
    
}

function switch_to_analize() {
    var n = get_stack_max_size()
    if (up.length == n) {
        send_data()
    }
}

function switch_to_predict() {

    $('#table').removeClass('ordered_false')
    $('#table').removeClass('ordered_true')
    $('#table').removeClass('ordered_unknow')
    
    var n = get_stack_max_size()
    if (up.length == n) {
        send_data()
    }
}