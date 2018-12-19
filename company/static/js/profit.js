function verify() {
    var input = $('#inputbrowsers')
    console.log(input.val())
    if (input.val()){

        return true
    }
    else{

        alert('请填写年份')
        return false
    }
}


// function yearchange() {
//     var input = $('#inputbrowsers')
//     var year = input.val()
//     window.location.href="/admin/company/profit/?year=" + year
//     // console.log(year)
// }

function deldata() {
    var input = $('#inputbrowsers')
    var year = input.val()
    window.location.href="/admin/company/deldata/?year=" + year + '&model=profit' 
    // console.log(year)
}


window.onload=function(){
    var input = $('input');
    input.on('input propertychange',function(event){
        var jthis = $(event.target);
        var name = jthis.attr("name");
        
        n1 = name[0]
        n2 = name.slice(1)
        jthis.val(jthis.val().replace(",",""))

        if (n1 == 'c'){
            if (n2 == 7 | n2 == 8)
            {
                c5()
                c6()
                c24()
                c29()
                c31()
            }
            else if (n2 ==13 | n2==14 | n2==15 | n2==17 | n2==20)
            {
                c9()
                c24()
                c29()
                c31()
            }        
            else if (n2 == 11 | n2 == 12)
            {
                c10()
                c9()
                c24()
                c29()
                c31()
            }
            else if (n2 == 21 | n2 == 22)
            {
                c24()
                c29()
                c31()
            }
            else if (n2 == 25 | n2 == 27)
            {
                c29()
                c31()
            }
            else if (n2 == 30)
            {
                c31()
            }
        }

        if (n1 == 'd'){
            if (n2 == 7 | n2 == 8)
            {
                d5()
                d6()
                d24()
                d29()
                d31()
            }
            else if (n2 ==13 | n2==14 | n2==15 | n2==17 | n2==20)
            {
                d9()
                d24()
                d29()
                d31()
            }        
            else if (n2 == 11 | n2 == 12)
            {
                d10()
                d9()
                d24()
                d29()
                d31()
            }
            else if (n2 == 21 | n2 == 22)
            {
                d24()
                d29()
                d31()
            }
            else if (n2 == 25 | n2 == 27)
            {
                d29()
                d31()
            }
            else if (n2 == 30)
            {
                d31()
            }
        }




        
    });
    c5()
    c6()
    c10()
    c9()
    c24()
    c29()
    c31()

    d5()
    d6()
    d10()
    d9()
    d24()
    d29()
    d31()

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
function c24() {
    cal('c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c20,-c21,-c22,c24')
}
function c29() {
    cal('c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c20,-c21,-c22,c25,-c27,c29')
}
function c31() {
    cal('c7,c8,-c11,-c12,-c13,-c14,-c15,-c17,-c20,-c21,-c22,c25,-c27,-c30,c31')
}

function d5() {
    cal('d7,d8,d5')
}
function d6() {
    cal('d7,d8,d6')
}
function d10() {
    cal('d11,d12,d10')
}
function d9() {
    cal('d11,d12,d13,d14,d15,d17,d19,d9')
}
function d24() {
    cal('d7,d8,-d11,-d12,-d13,-d14,-d15,-d17,-d20,-d21,-d22,d24')
}
function d29() {
    cal('d7,d8,-d11,-d12,-d13,-d14,-d15,-d17,-d20,-d21,-d22,d25,-d27,d29')
}
function d31() {
    cal('d7,d8,-d11,-d12,-d13,-d14,-d15,-d17,-d20,-d21,-d22,d25,-d27,-d30,d31')
}





function refreshdata() {
    c5()
    c6()
    c10()
    c9()
    c24()
    c29()
    c31()

    d5()
    d6()
    d10()
    d9()
    d24()
    d29()
    d31()
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
    $("." + res_s + " span").text(total.toFixed(2))
}



var wb;//读取完成的数据
var rABS = false; //是否将文件读取为二进制字符串

function importf(obj) {//导入
    if(!obj.files) {
        return;
    }
    var f = obj.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
        var data = e.target.result;
        if(rABS) {
            wb = XLSX.read(btoa(fixdata(data)), {//手动转化
                type: 'base64'
            });
        } else {
            wb = XLSX.read(data, {
                type: 'binary'
            });
        }
        //wb.SheetNames[0]是获取Sheets中第一个Sheet的名字
        //wb.Sheets[Sheet名]获取第一个Sheet的数据
        deal_excel(wb)
    };
    if(rABS) {
        reader.readAsArrayBuffer(f);
    } else {
        reader.readAsBinaryString(f);
    }
}

function fixdata(data) { //文件流转BinaryString
    var o = "",
        l = 0,
        w = 10240;
    for(; l < data.byteLength / w; ++l) o += String.fromCharCode.apply(null, new Uint8Array(data.slice(l * w, l * w + w)));
    o += String.fromCharCode.apply(null, new Uint8Array(data.slice(l * w)));
    return o;
}

function deal_excel(wb) {
    var ce=XLSX.utils.sheet_to_formulae(wb.Sheets[wb.SheetNames[2]]);
    var dic = new Array();
    for (var i=0;i<ce.length;i++){
        var c = ce[i].split('=')
        if (c.length == 2){
            dic[c[0]] = c[1].toLowerCase() 
        }
        else{
            window.alert(i + '  '+ ce[i]);
        }
    }
    for (let item in $(".input input")){
        console.log($(item).attr('name'))
    }
    var input = $(".input input")
    for (var i=0;i<input.length;i++){
        _name = $(input[i]).attr('name').toUpperCase().replace(/^(\s|\xA0)+|(\s|\xA0)+$/g, '')
        $(input[i]).val(dic[_name])
    }
    refreshdata()
}