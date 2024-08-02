
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
    'predict_radio': send_domino_data_to_predic
}

function add_domino() {

    var n = get_stack_max_size()
    if (up.length < n) {

        domino = $(this)
        domino_src = domino.attr('src')

        var empty_id = 'empty_' + up.length
        var empty = $('#' + empty_id)
        empty_src = empty.attr('src')

        var start_offset = domino.offset()
        var start_top = start_offset['top']
        var start_left = start_offset['left']

        var finish_offset = empty.offset()
        var finish_top = finish_offset['top']
        var finish_left = finish_offset['left']
        
        var domin_clone = domino.clone()
        domin_clone.appendTo('body')
        domin_clone.offset({'top': start_top, 'left': start_left})

        domin_clone.animate({'top': finish_top, 'left': finish_left}, 300, function() {this.remove(); empty.attr('src', domino_src)});
   
        stack.push(empty)

        add_domino_data(domino.attr('up'), domino.attr('down'))

        if (up.length == n) {
            send_data()
        }

    }
}

function send_domino_data_to_analize() {    

    var header = {
        'url': '/ordered_check',
        'type': 'post',
        'headers': {'Content-Type': "application/json"},
        'data': JSON.stringify({
            first: up,
            second: down
        })
    }

    AjaxQuery.info(header, function(data) {
        order_check_class = cl_class[data['ordered_check']]
        $('#table').addClass(order_check_class)
    })

}

function send_domino_data_to_predic() {

    var header = {
        'url': '/predict',
        'type': 'post',
        'headers': {'Content-Type': "application/json"},
        'data': JSON.stringify({
            first: up,
            second: down
        })
    }

    AjaxQuery.info(header, function(data) {
        console.log(data, '!!!!!!!!!!!!!!!!')
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
    var radio = $('input[name="mode"]:checked').attr('id')
    var send_data_func = send_domino_funcs[radio]
    send_data_func()
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