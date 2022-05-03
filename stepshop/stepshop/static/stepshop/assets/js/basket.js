window.onload = function () {
    $('.basket_list').on('click', 'input[type=number]', function (e) {
        let t_href = e.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
            data: {'is_ajax': true},
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
        e.preventDefault();
    });
}