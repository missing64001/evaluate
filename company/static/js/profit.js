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
function refreshdata() {
    c5()
    c6()
    c10()
    c9()
    c23()
    c28()
    c30()
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