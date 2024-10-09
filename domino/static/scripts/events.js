

var main = (function () {

     // Привязка событий
     function _bindHandlers() {

      console.log('GUPUUHwwUH!!!!')

        $('#main').on('click.main', '.domino_pic', add_domino)
        $('#main').on('click.main', '#clean', clear_table)
        $('#main').on('click.main', '#domino_rollback', domino_rollback)
        $('#main').on('click.main', '#analize_radio', switch_mode)
        $('#main').on('click.main', '#predict_radio', switch_mode)
        $('#main').on('click.main', '#add_max_size_btn', change_max_size)
        $('#graphs_area').on('click.main', '#graph_tumbler', switch_graph)

        $(document).keyup(function(e) {
          key_board_funcks(e)
        })
    }

    // Инициализация приложения
    function init() {
      _bindHandlers();
    }

    // Возвращаем наружу
    return {
      init: init
    }

})();

$(document).ready(main.init);