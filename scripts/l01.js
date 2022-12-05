$(document).ready(function(){
    // console.log("hi");
    //enableBlur($("#background-main"), 16);
    //$(document.body)
    // $(".div1").css("background-image", "url(\"../data/portal.png\")");
    // $(".div1").css("background-repeat", "no-repeat");
    // $(".div1").css("background-position", "center");
    // $(".div1").css("background-size", "contain");
    // $(".div1").css("filter", "none");
    $("#background-main").css("background-image", "url({{ url_for('static', filename="data/Viking.ttf") }})");
});