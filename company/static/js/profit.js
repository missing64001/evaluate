

console.log('aaa')

window.onload=function(){
    var input = $('input');
    input.on('input propertychange',function(event){
        var jthis = $(event.target);
        var name = jthis.attr("name");
        
        n1 = name[0]
        n2 = name.slice(1)
        jthis.val(jthis.val().replace(",",""))


        if (n2 == 7 | n2 == 8)
        {
            c5()
            c6()
            c23()
            c28()
            c30()
        }
        else if (n2 ==13 | n2==14 | n2==15 | n2==17 | n2==19)
        {
            c9()
            c23()
            c28()
            c30()
        }        
        else if (n2 == 11 | n2 == 12)
        {
            c10()
            c9()
            c23()
            c28()
            c30()
        }
        else if (n2 == 20 | n2 == 21)
        {
            c23()
            c28()
            c30()
        }
        else if (n2 == 24 | n2 == 26)
        {
            c28()
            c30()
        }
        else if (n2 == 29)
        {
            c30()
        }



        
    });
    c5()
    c6()
    c10()
    c9()
    c23()
    c28()
    c30()

}

function c5() {
    cal('c7,c8,c5')
}
function c6() {
    cal('c7,c8,c6')
}
function c10() {
    cal('c11,c12,c10')
}
function c9() {
    cal('c11,c12,c13,c14,c15,c17,c19,c9')
}
function c23() {
    cal('c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c19,-c20,-c21,c23')
}
function c28() {
    cal('c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c19,-c20,-c21,c24,-c26,c28')
}
function c30() {
    cal('c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c19,-c20,-c21,c24,-c26,-c29,c30')
}

function cal(str) {
    var total = 0
    var lst_s = str.split(',')
    var res_s = lst_s[lst_s.length-1]
    lst_s = lst_s.slice(0,lst_s.length-1)
    for (var i=0;i<lst_s.length;i++){
        var s = lst_s[i]
        var sign = 1
        if (s[0] == '-'){
            sign = -1
            s = s.slice(1)
        }
        if ($('.input .'+s).val()){
            total = total + parseFloat($('.input .'+s).val()) * sign
        }
    }
    $("." + res_s + " span").text(total)
}