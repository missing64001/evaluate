

console.log('aaa')

window.onload=function(){
    var input = $('input');
    input.on('input propertychange',function(event){
        var jthis = $(event.target);
        var name = jthis.attr("name");
        
        n1 = name[0]
        n2 = name.slice(1)
        jthis.val(jthis.val().replace(",",""))

        if (n1 == 'd'){
            if (n2 < 9)
            {
                d9()

            }
            if (n2 < 14)
            {
                d14()
                d15()
                g21()
            }
            else if (n2 < 21)
            {
                d21()
            }
            else if (n2 < 25)
            {
                d25()
            }

            if (n2 < 26 && n2 > 14){
                d26()
            }
            if (n2<31 && n2>27){
                d31()
            }
            if (n2<35 && n2>31){
                d35()
            }
            if (n2<35 && n2>27){
                d36()
            }
            d38()
        }
        else if(n1 == 'g'){
            if (n2 < 21){
                g21()
                g22()
            }
            if (n2<38 && n2>33){
                g38()
            }
        }

    });



    d9()
    d14()
    d15()
    d21()
    d25()
    d26()
    d31()
    d35()
    d36()
    d38()
    g21()
    g22()
    g38()

}

function d9() {
    cal('d6,d7,d8,d9')
}
function d14() {
    cal('d10,d11,d12,d13,d14')
}
function d15() {
    cal('d9,-d14,d15')
}
function d21() {
    cal('d17,d18,d19,d20,d21')
}
function d25() {
    cal('d22,d23,d24,d25')
}
function d26() {
    cal('d21,-d25,d26')
}

function d31() {
    cal('d28,d29,d30,d31')
}
function d35() {
    cal('d32,d33,d34,d35')
}
function d36() {
    cal('d31,-d35,d36')
}
function d38() {
    cal('d15,d26,d36,d37,d38')
}

function g21(){
    cal('d15,-g6,-g7,-g8,-g9,-g9,-g10,-g11,-g12,-g13,-g14,-g15,-g16,-g17,-g18,-g19,-g20,g21')
}
function g22(){
    cal('g6,g7,g8,g9,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20,g22')
}
function g38(){
    cal('g34,g35,g36,g37,g38')
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
        else if(parseFloat($('.'+s).text())){
            total = total + parseFloat($('.'+s).text()) * sign
        }
    }
    $("." + res_s + " span").text(total.toFixed(2))
}