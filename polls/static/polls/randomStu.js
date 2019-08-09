$(function () {


    var $content = $(".table tr");
    for (var i = 1; i < $content.length; i++) {
        $content.eq(i).children("td")[2].innerText = (1 / ($content.length - 1) * 100).toFixed(1) + "%";
    }

    $(".panel-heading a:first").click(function () {
        var $filter_content = $(".table tr:not('.del')");
        // console.log($filter_content);
        var $result = $(".panel-body p span:last");
        var num = $filter_content.length;
        // var $percent = $("#percent li:not('.del')");
        var k = Math.floor(Math.random() * (num - 1) + 1);
        if (num > 1) {
            var $td = $filter_content.eq(k).children("td");
            $result.text($td.eq(1).text());
            $filter_content.eq(k).css("text-decoration", "line-through");
            $filter_content.eq(k).addClass("del");
            $td.eq(2).text("/");
            for (var i = 1; i < $content.length; i++) {
                if (!$filter_content.eq(i).hasClass("del")) {
                    $filter_content.eq(i).children("td").eq(2).text((1 / (num - 2) * 100).toFixed(1) + "%");
                }
            }
        } else {
            $result.text("卡池没卡了");
        }
    });


    function sum(arr, n) {
        return eval(arr.slice(0, n).join("+"))
    }

    var num = $content.length - 1;
    var weight = (new Array(num)).fill(1048576);
    $(".panel-heading a:last").click(function () {
        var w = sum(weight, weight.length);
        var k = Math.floor(Math.random() * w);
        for (var i = 1; i <= num; i++) {
            if (k < sum(weight, i)) {
//							if(#content[i] == "") {}
                $("#result").text($content.eq(i).children("td").eq(1).text());
                weight[i - 1] /= 8;
                weight.map(function (value,index) {
                    weight[index]=value*2
                });
                console.log(weight);

                if (weight[i - 1] < 1) {
                    weight.fill(1048576)
                }
                break;
            }
        }
        w = sum(weight, weight.length);
        for (var i = 1; i <= num; i++) {
            $content.eq(i).children("td").eq(2).text((weight[i - 1] / w * 100).toFixed(1) + "%");
        }
    });


});






