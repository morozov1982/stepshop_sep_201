window.onload = function () {
    const inp = $('.basket_list');

    function change_inp(t_href, current) {
        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
            data: {'is_ajax': true},
            success: function (data) {
                if (t_href.value > 0) {
                    $('.basket_summary').replaceWith(data.result);
                    current.parent().next().text("$" + data.product_price);
                } else {
                    current.parent().parent().detach();
                }
            },
        });
    };

    inp.on('input', 'input[type=number]', function (e) {
        change_inp(e.target, $(this));
    });
}